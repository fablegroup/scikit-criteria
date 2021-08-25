#!/usr/bin/env python
# -*- coding: utf-8 -*-
# License: BSD-3 (https://tldrlegal.com/license/bsd-3-clause-license-(revised))
# Copyright (c) 2016-2021, Cabral, Juan; Luczywo, Nadia
# All rights reserved.

# =============================================================================
# DOCS
# =============================================================================

"""test for skcriteria.madm._moora."""

# =============================================================================
# IMPORTS
# =============================================================================

import numpy as np


import pytest

import skcriteria
from skcriteria.data import RankResult
from skcriteria.madm import (
    FullMultiplicativeFormMOORA,
    RatioMOORA,
    ReferencePointMOORA,
)
from skcriteria.preprocessing import VectorScaler

# =============================================================================
# TESTS
# =============================================================================


def test_RatioMOORA_kracka2010ranking():
    """
    Data From:
        KRACKA, M; BRAUERS, W. K. M.; ZAVADSKAS, E. K. Ranking
        Heating Losses in a Building by Applying the MULTIMOORA . -
        ISSN 1392 - 2785 Inz
    """
    dm = skcriteria.mkdm(
        matrix=[
            [33.95, 23.78, 11.45, 39.97, 29.44, 167.10, 3.852],
            [38.9, 4.17, 6.32, 0.01, 4.29, 132.52, 25.184],
            [37.59, 9.36, 8.23, 4.35, 10.22, 136.71, 10.845],
            [30.44, 37.59, 13.91, 74.08, 45.10, 198.34, 2.186],
            [36.21, 14.79, 9.17, 17.77, 17.06, 148.3, 6.610],
            [37.8, 8.55, 7.97, 2.35, 9.25, 134.83, 11.935],
        ],
        objectives=[min, min, min, min, max, min, max],
        anames=["A1", "A2", "A3", "A4", "A5", "A6"],
        cnames=["x1", "x2", "x3", "x4", "x5", "x6", "x7"],
    )

    expected = RankResult(
        "RatioMOORA",
        ["A1", "A2", "A3", "A4", "A5", "A6"],
        [5, 1, 3, 6, 4, 2],
        {
            "score": [
                -1.62447867,
                -0.25233889,
                -0.84635037,
                -2.23363519,
                -1.18698242,
                -0.77456208,
            ],
        },
    )

    transformer = VectorScaler(target="matrix")
    dm = transformer.transform(dm)

    ranker = RatioMOORA()
    result = ranker.rank(dm)

    assert result.equals(expected)
    assert result.method == expected.method
    assert np.allclose(result.e_.score, expected.e_.score)


def test_ReferencePointMOORA_kracka2010ranking():
    """
    Data From:
        KRACKA, M; BRAUERS, W. K. M.; ZAVADSKAS, E. K. Ranking
        Heating Losses in a Building by Applying the MULTIMOORA . -
        ISSN 1392 - 2785 Inz
    """
    dm = skcriteria.mkdm(
        matrix=[
            [33.95, 23.78, 11.45, 39.97, 29.44, 167.10, 3.852],
            [38.9, 4.17, 6.32, 0.01, 4.29, 132.52, 25.184],
            [37.59, 9.36, 8.23, 4.35, 10.22, 136.71, 10.845],
            [30.44, 37.59, 13.91, 74.08, 45.10, 198.34, 2.186],
            [36.21, 14.79, 9.17, 17.77, 17.06, 148.3, 6.610],
            [37.8, 8.55, 7.97, 2.35, 9.25, 134.83, 11.935],
        ],
        objectives=[min, min, min, min, max, min, max],
        anames=["A1", "A2", "A3", "A4", "A5", "A6"],
        cnames=["x1", "x2", "x3", "x4", "x5", "x6", "x7"],
    )

    expected = RankResult(
        "ReferencePointMOORA",
        ["A1", "A2", "A3", "A4", "A5", "A6"],
        [4, 5, 1, 6, 2, 3],
        {
            "score": [
                0.68934931,
                0.69986697,
                0.59817104,
                0.85955696,
                0.6002238,
                0.61480595,
            ],
            "reference_point": [
                0.34587742,
                0.08556044,
                0.26245184,
                0.00011605,
                0.77343790,
                0.34960423,
                0.81382773,
            ],
        },
    )

    transformer = VectorScaler(target="matrix")
    dm = transformer.transform(dm)

    ranker = ReferencePointMOORA()
    result = ranker.rank(dm)

    assert result.equals(expected)
    assert result.method == expected.method
    assert np.allclose(result.e_.score, expected.e_.score)
    assert np.allclose(result.e_.reference_point, expected.e_.reference_point)


def test_FullMultiplicativeFormMOORA_kracka2010ranking():
    """
    Data From:
        KRACKA, M; BRAUERS, W. K. M.; ZAVADSKAS, E. K. Ranking
        Heating Losses in a Building by Applying the MULTIMOORA . -
        ISSN 1392 - 2785 Inz
    """
    dm = skcriteria.mkdm(
        matrix=[
            [33.95, 23.78, 11.45, 39.97, 29.44, 167.10, 3.852],
            [38.9, 4.17, 6.32, 0.01, 4.29, 132.52, 25.184],
            [37.59, 9.36, 8.23, 4.35, 10.22, 136.71, 10.845],
            [30.44, 37.59, 13.91, 74.08, 45.10, 198.34, 2.186],
            [36.21, 14.79, 9.17, 17.77, 17.06, 148.3, 6.610],
            [37.8, 8.55, 7.97, 2.35, 9.25, 134.83, 11.935],
        ],
        objectives=[min, min, min, min, max, min, max],
        anames=["A1", "A2", "A3", "A4", "A5", "A6"],
        cnames=["x1", "x2", "x3", "x4", "x5", "x6", "x7"],
    )

    expected = RankResult(
        "FullMultiplicativeFormMOORA",
        ["A1", "A2", "A3", "A4", "A5", "A6"],
        [5, 1, 3, 6, 4, 2],
        {
            "score": np.log(
                [3.4343, 148689.356, 120.3441, 0.7882, 16.2917, 252.9155]
            ),
        },
    )

    transformer = VectorScaler(target="matrix")
    dm = transformer.transform(dm)

    ranker = FullMultiplicativeFormMOORA()
    result = ranker.rank(dm)

    assert result.equals(expected)
    assert result.method == expected.method
    assert np.allclose(result.e_.score, expected.e_.score, atol=1e-4)


def test_FullMultiplicativeFormMOORA_only_minimize():
    dm = skcriteria.mkdm(
        matrix=[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ],
        objectives=[min, min, min],
    )

    expected = RankResult(
        "FullMultiplicativeFormMOORA",
        ["A0", "A1", "A2"],
        [1, 2, 3],
        {
            "score": np.log([398.42074767, 19.92103738, 4.74310414]),
        },
    )

    transformer = VectorScaler(target="matrix")
    dm = transformer.transform(dm)

    ranker = FullMultiplicativeFormMOORA()
    result = ranker.rank(dm)

    assert result.equals(expected)
    assert result.method == expected.method
    assert np.allclose(result.e_.score, expected.e_.score, atol=1e-4)


def test_FullMultiplicativeFormMOORA_only_maximize():
    dm = skcriteria.mkdm(
        matrix=[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ],
        objectives=[max, max, max],
    )

    expected = RankResult(
        "FullMultiplicativeFormMOORA",
        ["A0", "A1", "A2"],
        [3, 2, 1],
        {
            "score": np.log([0.00682264, 0.13645283, 0.57310187]),
        },
    )

    transformer = VectorScaler(target="matrix")
    dm = transformer.transform(dm)

    ranker = FullMultiplicativeFormMOORA()
    result = ranker.rank(dm)

    assert result.equals(expected)
    assert result.method == expected.method

    assert np.allclose(result.e_.score, expected.e_.score, atol=1e-4)


def test_FullMultiplicativeFormMOORA_with0_fail():
    dm = skcriteria.mkdm(
        matrix=[[1, 2, 3], [4, 0, 6]],
        objectives=[max, max, max],
    )

    ranker = FullMultiplicativeFormMOORA()
    with pytest.raises(ValueError):
        ranker.rank(dm)
