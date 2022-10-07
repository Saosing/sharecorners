
import io
import traceback
import shutil
from typing import List, Dict
import os
import tempfile
from loguru import logger

from wand.image import Image


def pdf_data_to_thumbnails(
    pdf_data: bytes,
    pages: List[int],
    width_max: int,
    height_max: int,
    *,
    use_last_resort: bool = True
) -> Dict[int, bytes]:
    """
    Convert given pdf data to a set of images.

    :return: a dict map from page number to the binary data of image (which can be directly write to disk)
    """

    pdf_thumbnailing_funcs = [
        ("preview_generator", pdf_data_to_thumbnails_by_preview_generator),
        ("imagemagick", pdf_data_to_thumbnails_by_imagemagick),
    ]

    if use_last_resort:
        pdf_thumbnailing_funcs.append(("qpdf", pdf_data_to_thumbnails_by_qpdf))

    exceptions = []
    for name, func in pdf_thumbnailing_funcs:
        logger.info("Try using converter `{}`".format(name))
        try:
            return func(pdf_data, pages, width_max, height_max)
        except Exception as e:
            traceback.print_exc()
            logger.info("Converter `{}` failed".format(name))
            exceptions.append(e)

    # if not returned
    raise ValueError("Error generating thumbnails: ", exceptions)


# generate pdf text for search
def pdf_data2text(pdf_data):
    # The commandline tool `pdftotext` from `xpdf` package generates text that
    # is more search friendly, while the python package `pdftotext` generates
    # text that preserves the layout in original pdf, which is better for
    # text-only-view, but hard to search.
    from plumbum.cmd import pdftotext as pdftotext_exe

    return (pdftotext_exe["-", "-"] << pdf_data)()


# --- Implementations


def pdf_data_to_thumbnails_by_imagemagick(
    pdf_data: bytes, pages: List[int], width_max: int, height_max: int
):
    """
    Convert pdf data to set of images using imagemagick (via wand).

    :return: dict: index -> png_data
    """