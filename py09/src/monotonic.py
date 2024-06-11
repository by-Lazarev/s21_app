# monotonic.py

import os
import ctypes
import time

def monotonic():
    if os.name == 'posix':
        # Linux, MacOS
        class timespec(ctypes.Structure):
            _fields_ = [
                ('tv_sec', ctypes.c_long),
                ('tv_nsec', ctypes.c_long),
            ]

        # Using clock_gettime from libc
        librt = ctypes.CDLL('librt.so.1' if os.uname().sysname == 'SunOS' else 'librt.so', use_errno=True)
        CLOCK_MONOTONIC = 1  # Usually 1, but can vary based on the system
        timespec = timespec()

        if librt.clock_gettime(CLOCK_MONOTONIC, ctypes.byref(timespec)) != 0:
            errno = ctypes.get_errno()
            raise OSError(errno, os.strerror(errno))

        return timespec.tv_sec + timespec.tv_nsec / 1e9

    elif os.name == 'nt':
        # Windows
        class LARGE_INTEGER(ctypes.Structure):
            _fields_ = [("QuadPart", ctypes.c_longlong)]

        freq = LARGE_INTEGER()
        counter = LARGE_INTEGER()

        ctypes.windll.kernel32.QueryPerformanceFrequency(ctypes.byref(freq))
        ctypes.windll.kernel32.QueryPerformanceCounter(ctypes.byref(counter))

        return counter.QuadPart / freq.QuadPart

    else:
        raise NotImplementedError("Unsupported OS")

# Пример использования
if __name__ == "__main__":
    print(monotonic())

