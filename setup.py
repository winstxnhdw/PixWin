from distutils.core import Extension, setup

setup (
    ext_modules=[
        Extension(
            'pixwin.libs.get_pixel',
            ['pixwin/libs/get_pixel/get_pixel.c'],
            libraries=['gdi32']
        )
    ],
)
