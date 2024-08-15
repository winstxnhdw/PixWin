from __future__ import annotations

from pixwin.device_context import Win32OpenDC
from pixwin.get_pixel import (
    get_blue_value,
    get_green_value,
    get_red_value,
    get_rgb,
)
from pixwin.types import Blue, Green, Pixel, Red


class PixWin:
    """
    Summary
    -------
    Context manager for retrieving pixel values from a window

    Attributes
    ----------
    open_device_context (Win32OpenDC) : Win32OpenDC object used to open the device context
    window_device_context_handle (int) : handle to the device context

    Methods
    -------
    get_pixel(x: int, y: int) -> tuple[Red, Green, Blue]
        get the RGB value of a pixel at a given x, y coordinate

    get_red_value(x: int, y: int) -> Red | None
        get the red value of a pixel at a given x, y coordinate

    get_green_value(x: int, y: int) -> Green | None
        get the green value of a pixel at a given x, y coordinate

    get_blue_value(x: int, y: int) -> Blue | None
        get the blue value of a pixel at a given x, y coordinate
    """

    __slots__ = 'open_device_context', 'window_device_context_handle'

    def __init__(self, window_handle: int = 0):
        self.open_device_context = Win32OpenDC(window_handle)
        self.window_device_context_handle = self.open_device_context.__enter__()

    def __enter__(self) -> PixWin:
        return self

    def __exit__(self, *_):
        self.open_device_context.__exit__()

    def get_pixel(self, x: int, y: int) -> Pixel | None:
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
        red (int?) : red value of the pixel
        green (int?) : green value of the pixel
        blue (int?) : blue value of the pixel
        """
        return get_rgb(self.window_device_context_handle, x, y)

    def get_red_value(self, x: int, y: int) -> Red | None:
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
        red (int?) : red value of the pixel
        """
        return get_red_value(self.window_device_context_handle, x, y)

    def get_green_value(self, x: int, y: int) -> Green | None:
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
        blue (int?) : blue value of the pixel
        """
        return get_green_value(self.window_device_context_handle, x, y)

    def get_blue_value(self, x: int, y: int) -> Blue | None:
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
        green (int?) : green value of the pixel
        """
        return get_blue_value(self.window_device_context_handle, x, y)
