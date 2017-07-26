#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016-2017, Cabral, Juan; Luczywo, Nadia
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# * Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.

# * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.

# * Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


"""
https://matplotlib.org/examples/pylab_examples/boxplot_demo2.html

"""

# =============================================================================
# IMPORTS
# =============================================================================

import numpy as np

import matplotlib.pyplot as plt
from matplotlib import patches

from six.moves import zip


# =============================================================================
# FUNCTIONS
# =============================================================================

def box_plot(
        mtx, criteria, weights, anames, cnames, show_legend=False,
        cmap=None, ax=None, subplots_kwargs=None, box_kwargs=None):

    # create ax if necesary
    if ax is None:
        subplots_kwargs = subplots_kwargs or {}
        subplots_kwargs.setdefault("figsize", (9, 6))
        ax = plt.subplots(**subplots_kwargs)[-1]

    # boxplot
    box_kwargs = box_kwargs or {}
    box_kwargs.setdefault("notch", False)
    box_kwargs.setdefault("vert", True)
    box_kwargs.setdefault("patch_artist", True)
    box_kwargs.setdefault("sym", "o")
    box_kwargs.setdefault("flierprops", {'linestyle': 'none',
                                         'marker': 'o',
                                         'markerfacecolor': 'red'})
    bp = ax.boxplot(mtx, **box_kwargs)

    # colors in boxes
    colors = cmap(np.linspace(0, 1, mtx.shape[1]))
    legends_patchs = []
    for box, color, cname in zip(bp['boxes'], colors, cnames):
        box.set_facecolor(color)

        legend_patch = patches.Patch(color=color, label=cname)
        legends_patchs.append(legend_patch)

    if show_legend:
        ax.legend(loc="best", handles=legends_patchs)

    # ticks
    ax.set_xticklabels(cnames, rotation=10, size="small")

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    return ax