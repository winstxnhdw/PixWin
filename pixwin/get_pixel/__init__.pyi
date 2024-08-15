# pylint: skip-file

from pixwin.types import Blue, Green, Pixel, Red

def get_rgb(device_context_handle: int, x: int, y: int) -> Pixel | None:
    """
    get the RGB value of a pixel at the specified coordinates

    Parameters
    ----------
    device_context_handle (int) : handle to the device context
    x (int) : x-coordinate of the pixel
    y (int) : y-coordinate of the pixel

    Returns
    -------
    Pixel | None : RGB value of the pixel at the specified coordinates
    """
    ...

def get_red_value(device_context_handle: int, x: int, y: int) -> Red | None:
    """
    get the red value of a pixel at the specified coordinates

    Parameters
    ----------
    device_context_handle (int) : handle to the device context
    x (int) : x-coordinate of the pixel
    y (int) : y-coordinate of the pixel

    Returns
    -------
    Red | None : red value of the pixel at the specified coordinates
    """
    ...

def get_blue_value(device_context_handle: int, x: int, y: int) -> Blue | None:
    """
    get the blue value of a pixel at the specified coordinates

    Parameters
    ----------
    device_context_handle (int) : handle to the device context
    x (int) : x-coordinate of the pixel
    y (int) : y-coordinate of the pixel

    Returns
    -------
    Blue | None : blue value of the pixel at the specified coordinates
    """
    ...

def get_green_value(device_context_handle: int, x: int, y: int) -> Green | None:
    """
    get the green value of a pixel at the specified coordinates

    Parameters
    ----------
    device_context_handle (int) : handle to the device context
    x (int) : x-coordinate of the pixel
    y (int) : y-coordinate of the pixel

    Returns
    -------
    Green | None : green value of the pixel at the specified coordinates
    """
    ...
