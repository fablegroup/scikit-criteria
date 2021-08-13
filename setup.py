#!/usr/bin/env python
# -*- coding: utf-8 -*-
# License: BSD-3 (https://tldrlegal.com/license/bsd-3-clause-license-(revised))
# Copyright (c) 2016-2021, Cabral, Juan; Luczywo, Nadia
# All rights reserved.

# =============================================================================
# DOCS
# =============================================================================

"""This file is for distribute scikit-criteria

"""


# =============================================================================
# IMPORTS
# =============================================================================


import os

from setuptools import find_packages, setup

os.environ["__SKCRITERIA_IN_SETUP__"] = "True"
import skcriteria  # noqa

# =============================================================================
# CONSTANTS
# =============================================================================

REQUIREMENTS = [
    "numpy",
    "pandas",
    "pyquery",
    "scipy",
    "jinja2",
    "custom_inherit",
    "matplotlib",
]


# =============================================================================
# FUNCTIONS
# =============================================================================


def do_setup():
    setup(
        name=skcriteria.NAME,
        version=skcriteria.VERSION,
        description=skcriteria.DOC,
        author=skcriteria.AUTHORS,
        author_email=skcriteria.EMAIL,
        url=skcriteria.URL,
        license=skcriteria.LICENSE,
        keywords=skcriteria.KEYWORDS,
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: Implementation :: CPython",
            "Topic :: Scientific/Engineering",
        ],
        packages=[
            pkg for pkg in find_packages() if pkg.startswith("skcriteria")
        ],
        install_requires=REQUIREMENTS,
    )


if __name__ == "__main__":
    do_setup()
