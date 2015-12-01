from distutils.core import setup, Extension

setup(
    ext_modules=[Extension("sherlock", ["sherlockmodule.c", "sherlock.c"])],
    include_dirs="",
)