#!/usr/bin/env python
# -*- coding: utf-8 -*-
# License: BSD-3 (https://tldrlegal.com/license/bsd-3-clause-license-(revised))
# Copyright (c) 2016-2021, Cabral, Juan; Luczywo, Nadia
# All rights reserved.

# =============================================================================
# DOCS
# =============================================================================

"""MCDA methods."""

# =============================================================================
# IMPORTS
# =============================================================================

from ._electre import ELECTRE1, electre1
from ._maut import WeightedProductModel, WeightedSumModel, wpm, wsm
from ._moora import (
    FullMultiplicativeForm,
    MultiMOORA,
    RatioMOORA,
    ReferencePointMOORA,
    fmf,
    multimoora,
    ratio,
    refpoint,
)
from ._similarity import TOPSIS, topsis
from ._simus import SIMUS, simus

# =============================================================================
# ALL
# =============================================================================

__all__ = [
    "ELECTRE1",
    "FullMultiplicativeForm",
    "MultiMOORA",
    "RatioMOORA",
    "ReferencePointMOORA",
    "SIMUS",
    "TOPSIS",
    "WeightedSumModel",
    "WeightedProductModel",
    "electre1",
    "fmf",
    "multimoora",
    "ratio",
    "refpoint",
    "simus",
    "topsis",
    "wpm",
    "wsm",
]