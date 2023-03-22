
# PixWin

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![main.yml](https://github.com/winstxnhdw/PixWin/actions/workflows/main.yml/badge.svg)](https://github.com/winstxnhdw/PixWin/actions/workflows/main.yml)

`PixWin` is a fast Python API for retrieving RGB values of a pixel on Windows. It uses Python C extensions and ctypes to access [GetPixel()](https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-getpixel) within the Win32 API.

## Installation

```bash
pip install git+https://github.com/winstxnhdw/PixWin
```

## Usage

```python
from pixwin import PixWin


def loop(pixwin: PixWin):

    while True:
        print(pixwin.get_pixel(420, 69))        # e.g. (42, 21, 13)
        print(pixwin.get_red_value(420, 69))    # e.g. 42
        print(pixwin.get_blue_value(420, 69))   # e.g. 21
        print(pixwin.get_green_value(420, 69))  # e.g. 13


def main():

    with PixWin() as pixwin:
        try:
            loop(pixwin)

        except KeyboardInterrupt:
            print('Manual exit detected.')


if __name__ == '__main__':
    main()
```

## Benchmarks

Similar to PixWin, [PyScreeze](https://github.com/asweigart/pyscreeze) retrieves pixel values via the Win32 API. PixWin is ~15000x faster than [PyScreeze](https://github.com/asweigart/pyscreeze).

### Single-pixel retrieval

PixWin

```python
import cProfile as profile
from pixwin import PixWin


with PixWin() as pw:
    def pixwin():

        pw.get_pixel(0, 0)


if __name__ == '__main__':
    profile.run('pixwin()')
```

```txt
6 function calls in 0.000 seconds

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    1    0.000    0.000    0.000    0.000 __init__.py:33(get_pixel)
    1    0.000    0.000    0.000    0.000 test.py:5(pixwin)
    1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
    1    0.000    0.000    0.000    0.000 {built-in method pixwin.libs.get_pixel.get_rgb}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

PyScreeze

```python
import cProfile as profile
import pyscreeze as ps


def pyscreeze():

    ps.pixel(0, 0)

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
    1    0.000    0.000    0.007    0.007 test.py:12(pyscreeze)
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

PixWin

```python
import cProfile as profile
from pixwin import PixWin


with PixWin() as pw:
    def pixwin():

        [pw.get_pixel(0, 0) for _ in range(10000)]


if __name__ == '__main__':
    profile.run('pixwin()')
```

```txt
20005 function calls in 0.006 seconds

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.006    0.006 <string>:1(<module>)
10000    0.002    0.000    0.004    0.000 __init__.py:33(get_pixel)
    1    0.000    0.000    0.006    0.006 test.py:5(pixwin)
    1    0.002    0.002    0.006    0.006 test.py:6(<listcomp>)
    1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
10000    0.003    0.000    0.003    0.000 {built-in method pixwin.libs.get_pixel.get_rgb}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

PyScreeze

```python
import cProfile as profile
import pyscreeze as ps


def pyscreeze():

    [ps.pixel(0, 0) for _ in range(10000)]

if __name__ == '__main__':
    profile.run('pyscreeze()')
```

```txt
150027 function calls in 89.460 seconds

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000   89.460   89.460 <string>:1(<module>)
20000    0.310    0.000    0.310    0.000 __init__.py:110(__win32_openDC)
    1    0.000    0.000    0.000    0.000 __init__.py:340(__init__)
    1    0.000    0.000    0.000    0.000 __init__.py:368(_FuncPtr)
    3    0.000    0.000    0.000    0.000 __init__.py:384(__getattr__)
    3    0.000    0.000    0.000    0.000 __init__.py:391(__getitem__)
    1    0.000    0.000    0.000    0.000 __init__.py:441(__getattr__)
10000   88.936    0.009   89.440    0.009 __init__.py:601(pixel)
40000    0.044    0.000    0.044    0.000 __init__.py:613(<genexpr>)
10000    0.029    0.000    0.035    0.000 contextlib.py:102(__init__)
10000    0.010    0.000    0.123    0.000 contextlib.py:130(__enter__)
10000    0.029    0.000    0.241    0.000 contextlib.py:139(__exit__)
10000    0.014    0.000    0.049    0.000 contextlib.py:279(helper)
    1    0.000    0.000   89.460   89.460 test.py:5(pyscreeze)
    1    0.019    0.019   89.460   89.460 test.py:7(<listcomp>)
    1    0.000    0.000    0.000    0.000 {built-in method _ctypes.LoadLibrary}
    1    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
    1    0.000    0.000   89.460   89.460 {built-in method builtins.exec}
10000    0.006    0.000    0.006    0.000 {built-in method builtins.getattr}
    3    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
20000    0.015    0.000    0.325    0.000 {built-in method builtins.next}
    4    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
10000    0.048    0.000    0.048    0.000 {method 'format' of 'str' objects}
    4    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
```
