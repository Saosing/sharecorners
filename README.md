# pdf2images

[![Build Status](https://img.shields.io/circleci/build/github/zxytim/pdf2images)](https://circleci.com/gh/zxytim/pdf2images)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0d229594113d431fb2d97adeb8cd0f7d)](https://www.codacy.com/manual/zxytim/pdf2images?utm_source=github.com&utm_medium=referral&utm_content=zxytim/pdf2images&utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/zxytim/pdf2images/branch/master/graph/badge.svg)](https://codecov.io/gh/zxytim/pdf2images)
[![PyPI - License](https://img.shields.io/pypi/l/pdf2images)](https://github.com/zxytim/pdf2images/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/pdf2images.svg)](https://badge.fury.io/py/pdf2images)
[![Requires.io](https://img.shields.io/requires/github/zxytim/pdf2images)](https://requires.io/github/zxytim/pdf2images/requirements/?branch=master)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pdf2images)](https://pypi.org/project/pdf2images/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pdf2images)

Convert PDF file to image files **ROBUSTLY**.

## Example

```bash
$ pdf2images -h
usage: pdf2images [-h] [--max-size MAX_SIZE] pdf_file output_dir

positional arguments:
  pdf_file
  output_dir

optional arguments:
  -h, --help           show this help message and exit
  --max-size MAX_SIZE  max size of either side of the image
```

## Why another "pdf-to-image" package

Once in a while, I need to convert a pdf file (usually slides or academic
paper) into image files (thumbnails) in order to get a fast glance to the
readers without downloading the pdf file.

However, I found all the pdf2image solutions cannot robustly process all the
pdf files, since man