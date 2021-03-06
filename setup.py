#!/usr/bin/env python

from setuptools import setup, find_packages
from os.path import join, dirname, abspath
from sys import path

srcdir = join(dirname(abspath(__file__)), "src/")
path.insert(0, srcdir)

setup(name="streamcurse",
      version='1.0.0',
      description="streamcurse is a curses stream launcher, inspired by gapatos livestreamer-curses.",
      url="http://github.com/RadicalEd360/stream-curse",
      author="Radical Edward",
      author_email="Radical.Ed360@gmail.com",
      license="MIT",
      packages = ['streamcurse','streamcurse.modules'],
      package_dir={ "": "src" },
      package_data={"": "*.txt" },
      install_requires=["streamlink"],
      entry_points={
          "console_scripts": ["streamcurse=streamcurse.main:main"]
      },
      classifiers=["Operating System :: POSIX",
                  "Programming Language :: Python :: 3",
                   "Environment :: Console :: Curses",
                   "Topic :: Utilities"]
)
