from ctypes import windll, wintypes


class Win32OpenDC:
    """
    Summary
    -------
    Context manager for opening a device context.

    Attributes
    ----------
    window_handle (int) : handle to the window
    device_context_handle (int) : handle to the device context
    user32 (WinDLL): user32 library

    Methods
    -------
    __init__(window_handle: int) -> self
        initialise the Win32OpenDC object with a window handle

    __enter__() -> int
        open the device context and return the handle
    """
    def __init__(self, window_handle: int):

        self.window_handle = window_handle
        self.device_context_handle = 0

        self.user32 = windll.user32
        self.user32.GetDC.argtypes     = [wintypes.HWND]
        self.user32.GetDC.restype      = wintypes.HDC
        self.user32.ReleaseDC.argtypes = [wintypes.HWND, wintypes.HDC]
        self.user32.ReleaseDC.restype  = wintypes.INT


    def __enter__(self) -> int:
        
        self.device_context_handle = self.user32.GetDC(self.window_handle)

        if self.device_context_handle == 0:
            raise WindowsError('[User32.dll] GetDC failed.')

        return self.device_context_handle


    def __exit__(self, *_):

        if self.user32.ReleaseDC(self.window_handle, self.device_context_handle) == 0:
            raise WindowsError('[User32.dll] ReleaseDC failed.')
