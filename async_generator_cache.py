import asyncio

from typing import AsyncGenerator

class AsyncGeneratorCacheManager:
    def __init__(self, async_gen: AsyncGenerator):
        """
        Class for caching items from an asynchronous generator.

        :param async_gen: The asynchronous generator whose results are to be cached.
        """
        self.async_gen = async_gen
        self.cache_queue = asyncio.Queue()
        self.caching_complete = asyncio.Event()

    async def start_caching(self):
        """
        Begins caching items from the asynchronous generator. 
        If an error occurs during iteration, it logs the error and ensures caching completes.
        """
        try:
            async for item in self.async_gen:
                await self.cache_queue.put(item)
        except Exception as e:
            # Handle the exception here, e.g., log the error
            print(f"An error occurred during caching: {e}")
        finally:
            self.caching_complete.set()

    async def get_cached_generator(self):
        """
        Provides a generator that yields cached items.
        Continues yielding until caching is complete and the queue is empty.
        """
        while not self.caching_complete.is_set() or not self.cache_queue.empty():
            item = await self.cache_queue.get()
            yield item
            self.cache_queue.task_done()
