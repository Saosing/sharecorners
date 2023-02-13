
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


with open("requirements.txt") as f:
    requirements = [line.strip() for line in f]


setuptools.setup(
    name="pdf2images",
    version="0.0.6",
    author="Xinyu Zhou",
    author_email="zxytim@gmail.com",
    description="Convert PDF file to image files ROBUSTLY.",
    long_description=long_description,
    long_description_content_type="text/markdown",