
# PixWin

`PixWin` is a fast Python API for retrieving RGB values of a pixel on Windows. It uses Python ctypes to access [GetPixel()](https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-getpixel) within the Win32 API.

## Installation

```bash
pip install git+https://github.com/winstxnhdw/PixWin
```

## Benchmarks

Similar to PixWin, [PyScreeze](https://github.com/asweigart/pyscreeze) retrieves pixel values via the Win32 API. Here's how PixWin fare against it.

### Single-pixel retrieval

```python
import cProfile as profile
from pixwin import PixWin


def pixwin():

    with PixWin() as pw:
        pw.get_pixel(0, 0)

profile.run('pixwin()')
```

```txt
33 function calls in 0.001 seconds

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.001    0.001 <string>:1(<module>)
    1    0.000    0.000    0.000    0.000 __init__.py:340(__init__)
    1    0.000    0.000    0.000    0.000 __init__.py:368(_FuncPtr)
    3    0.000    0.000    0.000    0.000 __init__.py:384(__getattr__)
    3    0.000    0.000    0.000    0.000 __init__.py:391(__getitem__)
    1    0.000    0.000    0.000    0.000 __init__.py:441(__getattr__)
    1    0.000    0.000    0.000    0.000 main.py:18(__enter__)
    1    0.000    0.000    0.000    0.000 main.py:28(__exit__)
    1    0.000    0.000    0.000    0.000 main.py:36(__init__)
    1    0.000    0.000    0.000    0.000 main.py:46(__enter__)
    1    0.000    0.000    0.000    0.000 main.py:52(__exit__)
    1    0.001    0.001    0.001    0.001 main.py:57(get_pixel)
    1    0.000    0.000    0.000    0.000 main.py:6(__init__)
    1    0.000    0.000    0.001    0.001 test.py:6(main)
    1    0.000    0.000    0.000    0.000 {built-in method _ctypes.LoadLibrary}
    1    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
    1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
    3    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
    4    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    4    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
```

```python
import cProfile as profile
import pyscreeze as ps


def pyscreeze():

    ps.pixel(0,0)

profile.run('pyscreeze()')
```

```txt
41 function calls in 0.007 seconds

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.007    0.007 <string>:1(<module>)
    2    0.000    0.000    0.000    0.000 __init__.py:110(__win32_openDC)
    1    0.000    0.000    0.000    0.000 __init__.py:340(__init__)
    1    0.000    0.000    0.000    0.000 __init__.py:368(_FuncPtr)
    3    0.000    0.000    0.000    0.000 __init__.py:391(__getitem__)
    1    0.000    0.000    0.000    0.000 __init__.py:441(__getattr__)
    1    0.007    0.007    0.007    0.007 __init__.py:601(pixel)
    4    0.000    0.000    0.000    0.000 __init__.py:613(<genexpr>)
    1    0.000    0.000    0.000    0.000 contextlib.py:102(__init__)
    1    0.000    0.000    0.000    0.000 contextlib.py:130(__enter__)
    1    0.000    0.000    0.000    0.000 contextlib.py:139(__exit__)
    1    0.000    0.000    0.000    0.000 contextlib.py:279(helper)
    1    0.000    0.000    0.007    0.007 test.py:12(gay)
    1    0.000    0.000    0.000    0.000 {built-in method _ctypes.LoadLibrary}
    1    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
    1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
    1    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
    3    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
    2    0.000    0.000    0.000    0.000 {built-in method builtins.next}
    4    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    1    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
    4    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
```

### Multi-pixel retrieval

```python
import cProfile as profile
from pixwin import PixWin


def pixwin():

    with PixWin() as pw:
        for _ in range(100):
            pw.get_pixel(0,0)

profile.run('pixwin()')
```

```txt
139 function calls

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.690    0.690 <string>:1(<module>)     
    1    0.000    0.000    0.000    0.000 __init__.py:24(__exit__)
    100  0.689    0.007    0.689    0.007 __init__.py:29(get_pixel)
    2    0.000    0.000    0.000    0.000 __init__.py:340(__init__)
    2    0.000    0.000    0.000    0.000 __init__.py:368(_FuncPtr)
    3    0.000    0.000    0.000    0.000 __init__.py:384(__getattr__)
    3    0.000    0.000    0.000    0.000 __init__.py:391(__getitem__)
    2    0.000    0.000    0.000    0.000 __init__.py:441(__getattr__)
    1    0.000    0.000    0.000    0.000 __init__.py:8(__init__)
    1    0.000    0.000    0.000    0.000 open_device_context.py:18(__enter__)
    1    0.000    0.000    0.000    0.000 open_device_context.py:28(__exit__)
    1    0.000    0.000    0.000    0.000 open_device_context.py:6(__init__)
    1    0.000    0.000    0.690    0.690 test.py:5(pixwin)
    2    0.000    0.000    0.000    0.000 {built-in method _ctypes.LoadLibrary}
    2    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
    1    0.000    0.000    0.690    0.690 {built-in method builtins.exec}
    3    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
    5    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    5    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
```

```python
import cProfile as profile
import pyscreeze as ps


def pyscreeze():

    for _ in range(100):
        ps.pixel(0, 0)

profile.run('pyscreeze()')
```

```txt
1526 function calls

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.690    0.690 <string>:1(<module>)
    200  0.003    0.000    0.003    0.000 __init__.py:110(__win32_openDC)
    1    0.000    0.000    0.000    0.000 __init__.py:340(__init__)
    1    0.000    0.000    0.000    0.000 __init__.py:368(_FuncPtr)
    3    0.000    0.000    0.000    0.000 __init__.py:384(__getattr__)
    3    0.000    0.000    0.000    0.000 __init__.py:391(__getitem__)
    1    0.000    0.000    0.000    0.000 __init__.py:441(__getattr__)
    100  0.685    0.007    0.690    0.007 __init__.py:601(pixel)
    400  0.000    0.000    0.000    0.000 __init__.py:613(<genexpr>)
    100  0.000    0.000    0.000    0.000 contextlib.py:102(__init__)
    100  0.000    0.000    0.002    0.000 contextlib.py:130(__enter__)
    100  0.000    0.000    0.002    0.000 contextlib.py:139(__exit__)
    100  0.000    0.000    0.000    0.000 contextlib.py:279(helper)
    1    0.000    0.000    0.690    0.690 test.py:5(pyscreeze)
    1    0.000    0.000    0.000    0.000 {built-in method _ctypes.LoadLibrary}
    1    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
    1    0.000    0.000    0.690    0.690 {built-in method builtins.exec}
    100  0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
    3    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
    200  0.000    0.000    0.004    0.000 {built-in method builtins.next}
    4    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    100  0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
    4    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
```