
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


with open("requirements.txt") as f:
    requirements = [line.strip() for line in f]


setuptools.setup(
    name="pdf2images",
    version="0.0.6",
    author="Xinyu Zhou",