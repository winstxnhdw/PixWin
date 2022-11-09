from ctypes import windll, wintypes


class Win32OpenDC:

    def __init__(self, window_handle: int):

        self.hWnd = window_handle
        self.hDC = 0

        self.user32 = windll.user32
        self.user32.GetDC.argtypes     = [wintypes.HWND]
        self.user32.GetDC.restype      = wintypes.HDC
        self.user32.ReleaseDC.argtypes = [wintypes.HWND, wintypes.HDC]
        self.user32.ReleaseDC.restype  = wintypes.INT


    def __enter__(self) -> int | None:
        
        self.hDC = self.user32.GetDC(self.hWnd)

        if self.hDC == 0:
            raise WindowsError('[User32.dll] GetDC failed.')

        return self.hDC

    
    def __exit__(self, *_):

        if self.user32.ReleaseDC(self.hWnd, self.hDC) == 0:
            raise WindowsError('[User32.dll] ReleaseDC failed.')