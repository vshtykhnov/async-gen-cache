# Async Generator Cache

`async_generator_cache` is a Python package that provides a simple way to cache items from an asynchronous generator. This is particularly useful when working with generators that fetch data from slow or resource-intensive sources.

## Installation

Install this package using pip:

```bash
pip install async_generator_cache
```

## Usage

`async_generator_cache` provides a convenient way to cache items from an asynchronous generator, allowing you to perform other asynchronous operations concurrently. This is particularly useful in scenarios where you need to use the generator after completing some time-consuming tasks, such as waiting for a response from an API or executing some intensive code. By using `AsyncGeneratorCacheManager`, you can start caching the generator data in the background and use the cached data once your other tasks are completed, thereby saving time.

Here's a basic example of how to use `async_generator_cache`:

```python
import asyncio
from async_generator_cache import AsyncGeneratorCache

async def slow_data_generator():
    for i in range(5):
        await asyncio.sleep(1)
        yield i

async def perform_some_async_operation():
    # Simulate some async operation
    await asyncio.sleep(2)
    print("Async operation completed")

async def main():
    cache = AsyncGeneratorCache(slow_data_generator())

    # Start caching
    caching_task = asyncio.create_task(cache.cache_generator())

    # Perform some other async operation in the meantime
    await perform_some_async_operation()

    # Access cached items
    async for item in cache.cached_generator():
        print(item)

asyncio.run(main())
```
