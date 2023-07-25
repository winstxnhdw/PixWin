from typing import Self

from pixwin.libs import (Win32OpenDC, get_blue_value, get_green_value,
                         get_red_value, get_rgb)
from pixwin.types import Blue, Green, Pixel, Red


class NoDeviceContextError(Exception):
    """
    Summary
    -------
    exception raised when a device context is not open
    """
    def __init__(self):

        super().__init__(
            "Please use the context manager to call PixWin()."
        )


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
    get_pixel(x: int, y: int) -> tuple[int, int, int]
        get the RGB value of a pixel at a given x, y coordinate

    get_red_value(x: int, y: int) -> int
        get the red value of a pixel at a given x, y coordinate

    get_green_value(x: int, y: int) -> int
        get the green value of a pixel at a given x, y coordinate

    get_blue_value(x: int, y: int) -> int
        get the blue value of a pixel at a given x, y coordinate
    """
    __slots__ = 'open_device_context', 'window_device_context_handle'

    def __init__(self, window_handle: int=0):

        self.open_device_context = Win32OpenDC(window_handle)
        self.window_device_context_handle = None


    def __enter__(self) -> Self:

        self.window_device_context_handle = self.open_device_context.__enter__()
        return self


    def __exit__(self, *_):

        self.open_device_context.__exit__()


    def get_pixel(self, x: int, y: int) -> Pixel:
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
        try:
            return get_rgb(self.window_device_context_handle, x, y) # type: ignore

        except SystemError as error:
            raise NoDeviceContextError from error


    def get_red_value(self, x: int, y: int) -> Red:
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
        try:
            return get_red_value(self.window_device_context_handle, x, y) # type: ignore

        except SystemError as error:
            raise NoDeviceContextError from error


    def get_green_value(self, x: int, y: int) -> Green:
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
        try:
            return get_green_value(self.window_device_context_handle, x, y) # type: ignore

        except SystemError as error:
            raise NoDeviceContextError from error


    def get_blue_value(self, x: int, y: int) -> Blue:
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
        try:
            return get_blue_value(self.window_device_context_handle, x, y) # type: ignore

        except SystemError as error:
            raise NoDeviceContextError from error
