from setuptools import setup, find_packages

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name = "pyutil", 
  version = "1.0.0",
  author = "Samuel Souik",
  author_email = "me@samuelsouik.com", 
  description = "Collection of utility functions to be used in Python projects",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = "https://github.com/SSouik/pyutil",
  packages = [
      "pyutil",
      "pyutil/dictionary",
      "pyutil/iterators",
      "pyutil/string"
  ],
  classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10"
  ],
  python_requires=">=3.4, <=3.10"
)
