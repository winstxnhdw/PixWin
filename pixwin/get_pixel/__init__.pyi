# pylint: skip-file

from pixwin.types import Blue, Green, Pixel, Red

def get_rgb(device_context_handle: int, x: int, y: int) -> Pixel | None: ...


def get_red_value(device_context_handle: int, x: int, y: int) -> Red | None: ...


def get_blue_value(device_context_handle: int, x: int, y: int) -> Blue | None: ...


def get_green_value(device_context_handle: int, x: int, y: int) -> Green | None: ...
