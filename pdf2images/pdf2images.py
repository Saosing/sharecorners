
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