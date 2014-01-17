from distutils.core import setup, Extension

setup(
    name="HLL", 
    version="0.83", 
    description='The Hyper LogLog algorithm written in C.',
    author="Joshua Andersen",
    url='https://github.com/ascv/HLL',
    ext_modules=[
        Extension("HLL", ["hll.c", "murmur3.c"]),
    ],
    headers=['hll.h','mumur3.h']
)
