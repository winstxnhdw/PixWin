from ctypes import windll, wintypes

from typing_extensions import Self

from pixwin.utils import Win32OpenDC


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

        colour = self.gdi32.GetPixel(self.window_device_context_handle, x, y)
        return (colour & 0xff, (colour >> 8) & 0xff, (colour >> 16) & 0xff)