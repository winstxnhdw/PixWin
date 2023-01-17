from ctypes import windll, wintypes

from typing_extensions import Self

from pixwin.libs import (Win32OpenDC, get_blue_value, get_green_value,
                         get_red_value, get_rgb)


class PixWin:
    """
    Summary
    -------
    Context manager for retrieving pixel values from a window

    Attributes
    ----------
    open_device_context (Win32OpenDC) : Win32OpenDC object used to open the device context
    window_device_context_handle (int) : handle to the device context
    gdi32 (WinDLL): gdi32 library.

    Methods
    -------
    __init__(window_handle: int=0) -> self
        initialise the PixWin object with a window handle

    __enter__() -> self
        open the device context and return the object

    get_pixel(x: int, y: int) -> tuple[int, int, int]
        get the RGB value of a pixel at a given x, y coordinate

    get_red_value(x: int, y: int) -> int
        get the red value of a pixel at a given x, y coordinate

    get_green_value(x: int, y: int) -> int
        get the green value of a pixel at a given x, y coordinate

    get_blue_value(x: int, y: int) -> int
        get the blue value of a pixel at a given x, y coordinate
    """
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
        """
        Summary
        -------
        Get the RGB value of a pixel at a given x, y coordinate 

        Parameters
        ----------
        x (int) : x coordinate on the window
        y (int) : y coordinate on the window

        Returns
        -------
        red (int) : red value of the pixel
        green (int) : green value of the pixel
        blue (int) : blue value of the pixel
        """
        return get_rgb(self.window_device_context_handle, x, y)


    def get_red_value(self, x: int, y: int) -> int:
        """
        Summary
        -------
        Get the red value of a pixel at a given x, y coordinate

        Parameters
        ----------
        x (int) : x coordinate on the window
        y (int) : y coordinate on the window

        Returns
        -------
        red (int) : red value of the pixel
        """
        return get_red_value(self.window_device_context_handle, x, y)


    def get_green_value(self, x: int, y: int) -> int:
        """
        Summary
        -------
        Get the green value of a pixel at a given x, y coordinate

        Parameters
        ----------
        x (int) : x coordinate on the window
        y (int) : y coordinate on the window

        Returns
        -------
        blue (int) : blue value of the pixel
        """
        return get_green_value(self.window_device_context_handle, x, y)


    def get_blue_value(self, x: int, y: int) -> int:
        """
        Summary
        -------
        Get the blue value of a pixel at a given x, y coordinate

        Parameters
        ----------
        x (int) : x coordinate on the window
        y (int) : y coordinate on the window

        Returns
        -------
        green (int) : green value of the pixel
        """
        return get_blue_value(self.window_device_context_handle, x, y)
    