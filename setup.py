from setuptools import Extension, setup

setup(
    ext_modules=[Extension('pixwin.get_pixel', ['pixwin/get_pixel/get_pixel.c'], libraries=['gdi32'])],
)
