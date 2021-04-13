# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import pydaily

PKG_NAME = "pydaily"
VERSION = pydaily.__version__
DESCRIPTION = "Daily python utility functions."
HOMEPAGE = "https://github.com/PingjunChen/pydaily"
LICENSE = "Apache"
AUTHOR_NAME = "Pingjun Chen"
AUTHOR_EMAIL = "pingjunchen@ieee.org"

REQS = ""
with open('requirements.txt') as f:
    REQS = [pkg.replace("==", ">=") for pkg in f.read().splitlines()]

CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Topic :: Scientific/Engineering',
]

args = dict(
    name=PKG_NAME,
    version=VERSION,
    description=DESCRIPTION,
    url=HOMEPAGE,
    license=LICENSE,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=REQS,
    classifiers= CLASSIFIERS,
)

setup(**args)
