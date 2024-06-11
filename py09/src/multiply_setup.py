# setup.py

from setuptools import setup
from Cython.Build import cythonize

setup(
    name='matrix',
    ext_modules=cythonize("multiply.pyx"),
    zip_safe=False,
)

