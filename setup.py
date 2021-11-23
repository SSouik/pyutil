from setuptools import setup, find_packages

with open("README.md", 'r') as fh:
  long_description = fh.read()

setup(
  name = 'pyutil', 
  version = '1.0.0',
  author = 'Samuel Souik',
  author_email = 'samuel.souik@gmail.com', 
  description = 'Functional library for Python',
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = 'https://github.com/SSouik/pyutil',
  packages = find_packages(),
  classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7"
  ],
  python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*"
)