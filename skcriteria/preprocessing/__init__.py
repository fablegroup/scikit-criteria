#!/usr/bin/env python
# -*- coding: utf-8 -*-
# License: BSD-3 (https://tldrlegal.com/license/bsd-3-clause-license-(revised))
# Copyright (c) 2016-2021, Cabral, Juan; Luczywo, Nadia
# All rights reserved.

# =============================================================================
# DOCS
# =============================================================================

"""Multiple data transformation routines."""

# =============================================================================
# IMPORTS
# =============================================================================

from ._add_value_to_zero import AddValueToZero, add_value_to_zero
from ._distance import CenitDistance, cenit_distance
from ._invert_objectives import MinimizeToMaximize, invert
from ._push_negatives import PushNegatives, push_negatives
from ._scalers import (
    MaxScaler,
    MinMaxScaler,
    StandarScaler,
    SumScaler,
    VectorScaler,
    scale_by_max,
    scale_by_minmax,
    scale_by_stdscore,
    scale_by_sum,
    scale_by_vector,
)
from ._weighters import (
    Critic,
    EntropyWeighter,
    EqualWeighter,
    StdWeighter,
    critic_weights,
    entropy_weights,
    equal_weights,
    pearson_correlation,
    spearman_correlation,
    std_weights,
)

# =============================================================================
# ALL
# =============================================================================

__all__ = [
    "AddValueToZero",
    "CenitDistance",
    "Critic",
    "EntropyWeighter",
    "EqualWeighter",
    "MaxScaler",
    "MinMaxScaler",
    "MinimizeToMaximize",
    "PushNegatives",
    "StandarScaler",
    "StdWeighter",
    "SumScaler",
    "VectorScaler",
    "add_value_to_zero",
    "cenit_distance",
    "critic_weights",
    "entropy_weights",
    "equal_weights",
    "invert",
    "push_negatives",
    "scale_by_max",
    "scale_by_minmax",
    "scale_by_stdscore",
    "scale_by_sum",
    "scale_by_vector",
    "pearson_correlation",
    "spearman_correlation",
    "std_weights",
]