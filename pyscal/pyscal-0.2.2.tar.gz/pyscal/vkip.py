"""Utility function for pyscal
"""
from __future__ import print_function

import pandas as pd
import numpy as np

from pyscal.constants import SWINTEGERS
from pyscal import WaterOil

ECL_EPSILON = 1.0e-6


def interpolator(
    tableobject, curve1, curve2, parameter, sat="sw", kr1="krw", kr2="krow", pc="pc"
):
    """Interpolates between two curves.

    The interpolation parameter is 0 through 1,
    irrespective of phases or low-base/base-high/low-high.

    Args:
        tabjeobject (WaterOil or GasOil): A partially setup object where
            relperm and pc columns are to be filled with numbers.
        curve1 (WaterOil or GasOil): "Low" case of interpolation (relates
            to interpolation parameter 0). Must be copies, as they
            will be modified.
        curve2: Ditto, relates to interpolation parameter 1
        parameter (float): Between 0 and 1, what you want to interpolate to.
        sat (str): Name of the saturation column, typically 'sw' or 'sg'
        kr1 (str): Name of the first relperm column ('krw' or 'krg')
        kr2 (str): Name of the second relperm column ('krow' or 'krog')
        pc (str): Name of the capillary pressure column ('pc')

    Returns:
        None, but modifies the first argument.
    """

    curve1.table.rename(columns={kr1: kr1 + "_1"}, inplace=True)
    curve2.table.rename(columns={kr1: kr1 + "_2"}, inplace=True)
    curve1.table.rename(columns={kr2: kr2 + "_1"}, inplace=True)
    curve2.table.rename(columns={kr2: kr2 + "_2"}, inplace=True)
    curve1.table.rename(columns={pc: pc + "_1"}, inplace=True)
    curve2.table.rename(columns={pc: pc + "_2"}, inplace=True)

    # Result data container:
    satresult = pd.DataFrame(data=tableobject.table[sat], columns=[sat])

    # Merge swresult with curve1 and curve2, and interpolate all
    # columns in sw:
    intdf = (
        pd.concat([curve1.table, curve2.table, satresult], sort=True)
        .set_index(sat)
        .sort_index()
        .interpolate(method="slinear")
        .fillna(method="bfill")
        .fillna(method="ffill")
    )

    # Normalized saturations does not make sense for the
    # interpolant, remove:
    for col in ["swn", "son", "swnpc", "H", "J"]:
        if col in intdf.columns:
            del intdf[col]

    intdf[kr1] = intdf[kr1 + "_1"] * (1 - parameter) + intdf[kr1 + "_2"] * parameter
    intdf[kr2] = intdf[kr2 + "_1"] * (1 - parameter) + intdf[kr2 + "_2"] * parameter
    if pc + "_1" in curve1.table.columns and pc + "_2" in curve2.table.columns:
        intdf[pc] = intdf[pc + "_1"] * (1 - parameter) + intdf[pc + "_2"] * parameter
    else:
        intdf[pc] = 0

    # Slice out the resulting sw values and columns. Slicing on
    # floating point indices is not robust so we need to slice on an
    # integer version of the sw column
    tableobject.table["swint"] = list(
        map(int, list(map(round, tableobject.table[sat] * SWINTEGERS)))
    )
    intdf["swint"] = list(map(int, list(map(round, intdf.index.values * SWINTEGERS))))
    intdf = intdf.reset_index()
    intdf.drop_duplicates("swint", inplace=True)
    intdf.set_index("swint", inplace=True)
    intdf = intdf.loc[tableobject.table["swint"].values]
    intdf = intdf[[sat, kr1, kr2, pc]].reset_index()

    # intdf['swint'] = (intdf['sw'] * SWINTEGERS).astype(int)
    # intdf.drop_duplicates('swint', inplace=True)

    # Populate the WaterOil object
    tableobject.table[kr1] = intdf[kr1]
    tableobject.table[kr2] = intdf[kr2]
    tableobject.table[pc] = intdf[pc]
    tableobject.table.fillna(method="ffill", inplace=True)
    return


def interpolate_oilwater(curve1, curve2, parameter):

    """Interpolates between two oil-water curves.

    NBNB! Currently pc interpolation is not implemented (procedure is the same, on intervals [swirr, 1]..)

    Returns:
        A new oil-water curve

    """

    from scipy.interpolate import interp1d

    def make_normalized_funcs(curve):
        krw_interp = interp1d(
            curve.table["sw"],
            curve.table["krw"],
            kind="linear",
            bounds_error=False,
            fill_value=(0.0, 1.0),
        )
        sw = lambda swn: curve.swcr + swn * (1.0 - curve.swcr - curve.sorw)
        krw = lambda swn: krw_interp(sw(swn))

        kro_interp = interp1d(
            1.0 - curve.table["sw"],
            curve.table["krow"],
            kind="linear",
            bounds_error=False,
            fill_value=(1.0, 0.0),
        )
        so = lambda son: curve.sorw + son * (1.0 - curve.sorw - curve.swl)
        kro = lambda son: kro_interp(so(son))

        return (krw, kro)

    krw1, kro1 = make_normalized_funcs(curve1)
    krw2, kro2 = make_normalized_funcs(curve2)

    weighted_value = lambda a, b: a * parameter + b * (1.0 - parameter)

    swl_new = weighted_value(curve1.swl, curve2.swl)
    swcr_new = weighted_value(curve1.swcr, curve2.swcr)
    sorw_new = weighted_value(curve1.sorw, curve2.sorw)

    h_tmp = min(curve1.h, curve2.h) * 0.5

    sw_new = [swl_new]
    if (swcr_new - swl_new) > ECL_EPSILON:
        if (swcr_new - swl_new) > h_tmp:
            sw_new.extend(list(np.arange(swl_new + h_tmp, swcr_new, step=h_tmp)))
        sw_new.append(swcr_new)
    sw_new.extend(list(np.arange(swcr_new + h_tmp, 1.0 - sorw_new, step=h_tmp)))
    if sorw_new > ECL_EPSILON:
        sw_new.extend([1.0 - sorw_new, 1.0])
    else:
        sw_new.append(1.0)

    sw_new = np.array(sw_new)

    son = (1.0 - sw_new - sorw_new) / (1.0 - sorw_new - swl_new)
    swn = (sw_new - swcr_new) / (1.0 - swcr_new - sorw_new)

    krw_new = weighted_value(krw1(swn), krw2(swn))
    krw_new[-1] = 1.0
    kro_new = weighted_value(kro1(son), kro2(son))
    kro_new[-1] = 0.0
    pc_new = np.zeros_like(krw_new)

    df = pd.DataFrame({"Sw": sw_new, "krw": krw_new, "krow": kro_new, "pcow": pc_new})

    new_curve = WaterOil(swl=swl_new, swcr=swcr_new, sorw=sorw_new)
    new_curve.add_fromtable(df)
    return new_curve
