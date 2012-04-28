#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='idleproc',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="Report if a process gets idle",
    long_description="Watch a process and report when its load on the CPU gets below a threshold. This is useful to spot daemons which get bored.",
    scripts=['idleproc'],
    data_files=[('share/man/man1', ['idleproc.1'])],
)
