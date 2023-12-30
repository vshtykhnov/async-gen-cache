from setuptools import setup, find_packages

setup(
    name="AsyncGeneratorCacheManager",
    version="1.0.0",
    author="vsthykhnov",
    author_email="v.shtykhnov@gmail.com",
    description="A simple asynchronous generator cache manager for Python.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vshtykhnov/AsyncGeneratorCacheManager",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[],
)
