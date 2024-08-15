from __future__ import annotations

from sys import platform
from typing import TypedDict

from setuptools import Extension


class Build(TypedDict):
    """
    Summary
    -------
    a typed dictionary for the build

    Attributes
    ----------
    ext_modules (list[Extension]) : a list of extensions
    """

    ext_modules: list[Extension]


def build(kwargs: Build):
    """
    Summary
    -------
    update the setup kwargs with the extension modules
    """
    if platform not in ('win32', 'cygwin', 'cli'):
        raise RuntimeError('keywin only supports Windows!')

    kwargs.update(ext_modules=[Extension('pixwin.get_pixel', ['pixwin/get_pixel/get_pixel.c'], libraries=['gdi32'])])
