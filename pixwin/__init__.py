from ctypes import windll, wintypes

from typing_extensions import Self

from pixwin.libs import (Win32OpenDC, get_blue_value, get_green_value,
                         get_red_value, get_rgb)


class PixWin:

    def __init__(self, window_handle: int=0):
        
        self.open_device_context = Win32OpenDC(window_handle)
        self.window_device_context_handle = None

        self.gdi32 = windll.gdi32
        self.gdi32.GetPixel.argtypes = [wintypes.HDC, wintypes.INT, wintypes.INT]
        self.gdi32.GetPixel.restype  = wintypes.COLORREF


    def __enter__(self) -> Self:
        
        self.window_device_context_handle = self.open_device_context.__enter__()
        return self


    def __exit__(self, *_):

        self.open_device_context.__exit__()


    def get_pixel(self, x: int, y: int) -> tuple[int, int, int]:

        return get_rgb(self.window_device_context_handle, x, y)


    def get_red_value(self, x: int, y: int) -> int:

        return get_red_value(self.window_device_context_handle, x, y)


    def get_green_value(self, x: int, y: int) -> int:

        return get_green_value(self.window_device_context_handle, x, y)


    def get_blue_value(self, x: int, y: int) -> int:

        return get_blue_value(self.window_device_context_handle, x, y)