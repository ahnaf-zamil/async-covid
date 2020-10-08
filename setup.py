# -*- coding: utf-8 -*-
import io
import re
from setuptools import setup

with io.open("README.md") as f:
    long_description = f.read()

with io.open("async_covid/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="async-covid",
    version=version,
    description="An async Python package to get information regarding the novel corona virus provided by Johns Hopkins university and worldometers.info. Based on https://github.com/ahmednafies/covid",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="K.M Ahnaf Zail",
    author_email="ahnafzamil@protonmail.com",
    license="MIT",
    packages=["async_covid", "async_covid.john_hopkins", "async_covid.worldometers"],
    install_requires=["asyncio", "aiohttp", "pydantic", "beautifulsoup4", "typer"],
    extras_require={
        "dev": [
            "pipenv",
            "pytest",
            "coverage",
            "flake8",
            "ipdb",
            "pre-commit",
            "black",
        ]
    },
    project_urls={
        "Source": "https://github.com/ahnaf-zamil/async-covid",
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    zip_safe=False,
    python_requires=">=3.6",
)
