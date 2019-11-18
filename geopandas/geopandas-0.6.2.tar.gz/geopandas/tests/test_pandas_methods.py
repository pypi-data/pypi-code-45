from __future__ import absolute_import

import os

import numpy as np
from numpy.testing import assert_array_equal
import pandas as pd
from six import PY2, PY3

import shapely
from shapely.geometry import Point, GeometryCollection

import geopandas
from geopandas import GeoDataFrame, GeoSeries
from geopandas._compat import PANDAS_GE_024, PANDAS_GE_025
from geopandas.array import from_shapely

from geopandas.testing import assert_geodataframe_equal, assert_geoseries_equal
from pandas.util.testing import assert_frame_equal, assert_series_equal
import pytest


@pytest.fixture
def s():
    return GeoSeries([Point(x, y) for x, y in zip(range(3), range(3))])


@pytest.fixture
def df():
    return GeoDataFrame(
        {
            "geometry": [Point(x, x) for x in range(3)],
            "value1": np.arange(3, dtype="int64"),
            "value2": np.array([1, 2, 1], dtype="int64"),
        }
    )


def test_repr(s, df):
    assert "POINT" in repr(s)
    assert "POINT" in repr(df)
    assert "POINT" in df._repr_html_()


@pytest.mark.skipif(
    not PANDAS_GE_024, reason="formatting for EA only implemented in 0.24.0"
)
def test_repr_boxed_display_precision():
    # geographic coordinates
    p1 = Point(10.123456789, 50.123456789)
    p2 = Point(4.123456789, 20.123456789)
    s1 = GeoSeries([p1, p2, None])
    assert "POINT (10.12346 50.12346)" in repr(s1)

    # projected coordinates
    p1 = Point(3000.123456789, 3000.123456789)
    p2 = Point(4000.123456789, 4000.123456789)
    s2 = GeoSeries([p1, p2, None])
    assert "POINT (3000.123 3000.123)" in repr(s2)

    geopandas.options.display_precision = 1
    assert "POINT (10.1 50.1)" in repr(s1)

    geopandas.options.display_precision = 9
    assert "POINT (10.123456789 50.123456789)" in repr(s1)


def test_repr_all_missing():
    # https://github.com/geopandas/geopandas/issues/1195
    s = GeoSeries([None, None, None])
    assert "None" in repr(s)
    df = GeoDataFrame({"a": [1, 2, 3], "geometry": s})
    assert "None" in repr(df)
    assert "geometry" in df._repr_html_()


def test_repr_empty():
    # https://github.com/geopandas/geopandas/issues/1195
    s = GeoSeries([])
    if PANDAS_GE_025:
        # repr with correct name fixed in pandas 0.25
        assert repr(s) == "GeoSeries([], dtype: geometry)"
    else:
        assert repr(s) == "Series([], dtype: geometry)"
    df = GeoDataFrame({"a": [], "geometry": s})
    assert "Empty GeoDataFrame" in repr(df)
    # https://github.com/geopandas/geopandas/issues/1184
    assert "geometry" in df._repr_html_()


def test_indexing(s, df):

    # accessing scalar from the geometry (colunm)
    exp = Point(1, 1)
    assert s[1] == exp
    assert s.loc[1] == exp
    assert s.iloc[1] == exp
    assert df.loc[1, "geometry"] == exp
    assert df.iloc[1, 0] == exp

    # multiple values
    exp = GeoSeries([Point(2, 2), Point(0, 0)], index=[2, 0])
    assert_geoseries_equal(s.loc[[2, 0]], exp)
    assert_geoseries_equal(s.iloc[[2, 0]], exp)
    assert_geoseries_equal(s.reindex([2, 0]), exp)
    assert_geoseries_equal(df.loc[[2, 0], "geometry"], exp)
    # TODO here iloc does not return a GeoSeries
    assert_series_equal(
        df.iloc[[2, 0], 0], exp, check_series_type=False, check_names=False
    )

    # boolean indexing
    exp = GeoSeries([Point(0, 0), Point(2, 2)], index=[0, 2])
    mask = np.array([True, False, True])
    assert_geoseries_equal(s[mask], exp)
    assert_geoseries_equal(s.loc[mask], exp)
    assert_geoseries_equal(df[mask]["geometry"], exp)
    assert_geoseries_equal(df.loc[mask, "geometry"], exp)

    # slices
    s.index = [1, 2, 3]
    exp = GeoSeries([Point(1, 1), Point(2, 2)], index=[2, 3])
    assert_series_equal(s[1:], exp)
    assert_series_equal(s.iloc[1:], exp)
    assert_series_equal(s.loc[2:], exp)


def test_reindex(s, df):
    # GeoSeries reindex
    res = s.reindex([1, 2, 3])
    exp = GeoSeries([Point(1, 1), Point(2, 2), None], index=[1, 2, 3])
    assert_geoseries_equal(res, exp)

    # GeoDataFrame reindex index
    res = df.reindex(index=[1, 2, 3])
    assert_geoseries_equal(res.geometry, exp)

    # GeoDataFrame reindex columns
    res = df.reindex(columns=["value1", "geometry"])
    assert isinstance(res, GeoDataFrame)
    assert isinstance(res.geometry, GeoSeries)
    assert_frame_equal(res, df[["value1", "geometry"]])

    # TODO df.reindex(columns=['value1', 'value2']) still returns GeoDataFrame,
    # should it return DataFrame instead ?


def test_take(s, df):
    inds = np.array([0, 2])

    # GeoSeries take
    result = s.take(inds)
    expected = s.iloc[[0, 2]]
    assert isinstance(result, GeoSeries)
    assert_geoseries_equal(result, expected)

    # GeoDataFrame take axis 0
    result = df.take(inds, axis=0)
    expected = df.iloc[[0, 2], :]
    assert isinstance(result, GeoDataFrame)
    assert_geodataframe_equal(result, expected)

    # GeoDataFrame take axis 1
    df = df.reindex(columns=["value1", "value2", "geometry"])  # ensure consistent order
    result = df.take(inds, axis=1)
    expected = df[["value1", "geometry"]]
    assert isinstance(result, GeoDataFrame)
    assert_geodataframe_equal(result, expected)

    result = df.take(np.array([0, 1]), axis=1)
    expected = df[["value1", "value2"]]
    assert isinstance(result, pd.DataFrame)
    assert_frame_equal(result, expected)


def test_take_empty(s, df):
    # ensure that index type is preserved in an empty take
    # https://github.com/geopandas/geopandas/issues/1190
    inds = np.array([], dtype="int64")

    # use non-default index
    df.index = pd.date_range("2012-01-01", periods=len(df))

    result = df.take(inds, axis=0)
    assert isinstance(result, GeoDataFrame)
    assert result.shape == (0, 3)
    assert isinstance(result.index, pd.DatetimeIndex)

    # the original bug report was an empty boolean mask
    for result in [df.loc[df["value1"] > 100], df[df["value1"] > 100]]:
        assert isinstance(result, GeoDataFrame)
        assert result.shape == (0, 3)
        assert isinstance(result.index, pd.DatetimeIndex)


def test_assignment(s, df):
    exp = GeoSeries([Point(10, 10), Point(1, 1), Point(2, 2)])

    s2 = s.copy()
    s2[0] = Point(10, 10)
    assert_geoseries_equal(s2, exp)

    s2 = s.copy()
    s2.loc[0] = Point(10, 10)
    assert_geoseries_equal(s2, exp)

    s2 = s.copy()
    s2.iloc[0] = Point(10, 10)
    assert_geoseries_equal(s2, exp)

    df2 = df.copy()
    df2.loc[0, "geometry"] = Point(10, 10)
    assert_geoseries_equal(df2["geometry"], exp)

    df2 = df.copy()
    df2.iloc[0, 0] = Point(10, 10)
    assert_geoseries_equal(df2["geometry"], exp)


def test_assign(df):
    res = df.assign(new=1)
    exp = df.copy()
    exp["new"] = 1
    assert isinstance(res, GeoDataFrame)
    assert_frame_equal(res, exp)


def test_astype(s, df):

    # check geoseries functionality
    with pytest.raises(TypeError):
        s.astype(int)

    assert s.astype(str)[0] == "POINT (0 0)"

    res = s.astype(object)
    assert isinstance(res, pd.Series) and not isinstance(res, GeoSeries)
    assert res.dtype == object

    df = df.rename_geometry("geom_list")

    # check whether returned object is a geodataframe
    res = df.astype({"value1": float})
    assert isinstance(res, GeoDataFrame)

    # check whether returned object is a datafrane
    res = df.astype(str)
    assert isinstance(res, pd.DataFrame) and not isinstance(res, GeoDataFrame)

    res = df.astype({"geom_list": str})
    assert isinstance(res, pd.DataFrame) and not isinstance(res, GeoDataFrame)

    res = df.astype(object)
    assert isinstance(res, pd.DataFrame) and not isinstance(res, GeoDataFrame)
    assert res["geom_list"].dtype == object


def test_astype_invalid_geodataframe():
    # https://github.com/geopandas/geopandas/issues/1144
    # a GeoDataFrame without geometry column should not error in astype
    df = GeoDataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    res = df.astype(object)
    assert isinstance(res, pd.DataFrame) and not isinstance(res, GeoDataFrame)
    assert res["a"].dtype == object


def test_to_csv(df):

    exp = (
        "geometry,value1,value2\nPOINT (0 0),0,1\nPOINT (1 1),1,2\nPOINT (2 2),2,1\n"
    ).replace("\n", os.linesep)
    assert df.to_csv(index=False) == exp


def test_numerical_operations(s, df):

    # df methods ignore the geometry column
    exp = pd.Series([3, 4], index=["value1", "value2"])
    assert_series_equal(df.sum(), exp)

    # series methods raise error
    with pytest.raises(TypeError):
        s.sum()

    if PY3:
        # in python 2, objects are still orderable
        with pytest.raises(TypeError):
            s.max()

    with pytest.raises(TypeError):
        s.idxmax()

    # numerical ops raise an error
    with pytest.raises(TypeError):
        df + 1

    with pytest.raises((TypeError, AssertionError)):
        # TODO(pandas 0.23) remove AssertionError -> raised in 0.23
        s + 1

    # boolean comparisons work
    res = df == 100
    exp = pd.DataFrame(False, index=df.index, columns=df.columns)
    assert_frame_equal(res, exp)


@pytest.mark.skipif(
    not PANDAS_GE_024, reason="where for EA only implemented in 0.24.0 (GH24114)"
)
def test_where(s):
    res = s.where(np.array([True, False, True]))
    exp = GeoSeries([Point(0, 0), None, Point(2, 2)])
    assert_series_equal(res, exp)


def test_select_dtypes(df):
    res = df.select_dtypes(include=[np.number])
    exp = df[["value1", "value2"]]
    assert_frame_equal(res, exp)


# Missing values


def test_fillna(s):
    s2 = GeoSeries([Point(0, 0), None, Point(2, 2)])
    res = s2.fillna(Point(1, 1))
    assert_geoseries_equal(res, s)

    # allow np.nan although this does not change anything
    # https://github.com/geopandas/geopandas/issues/1149
    res = s2.fillna(np.nan)
    assert_geoseries_equal(res, s2)


def test_dropna():
    s2 = GeoSeries([Point(0, 0), None, Point(2, 2)])
    res = s2.dropna()
    exp = s2.loc[[0, 2]]
    assert_geoseries_equal(res, exp)


@pytest.mark.parametrize("NA", [None, np.nan])
def test_isna(NA):
    s2 = GeoSeries([Point(0, 0), NA, Point(2, 2)], index=[2, 4, 5], name="tt")
    exp = pd.Series([False, True, False], index=[2, 4, 5], name="tt")
    res = s2.isnull()
    assert type(res) == pd.Series
    assert_series_equal(res, exp)
    res = s2.isna()
    assert_series_equal(res, exp)
    res = s2.notnull()
    assert_series_equal(res, ~exp)
    res = s2.notna()
    assert_series_equal(res, ~exp)


# Any / all


def test_any_all():
    empty = GeometryCollection([])
    s = GeoSeries([empty, Point(1, 1)])
    assert not s.all()
    assert s.any()

    s = GeoSeries([Point(1, 1), Point(1, 1)])
    assert s.all()
    assert s.any()

    s = GeoSeries([empty, empty])
    assert not s.all()
    assert not s.any()


# Groupby / algos


@pytest.mark.skipif(PY2, reason="pd.unique buggy with WKB values on py2")
def test_unique():
    s = GeoSeries([Point(0, 0), Point(0, 0), Point(2, 2)])
    exp = from_shapely([Point(0, 0), Point(2, 2)])
    # TODO should have specialized GeometryArray assert method
    assert_array_equal(s.unique(), exp)


@pytest.mark.xfail
def test_value_counts():
    # each object is considered unique
    s = GeoSeries([Point(0, 0), Point(1, 1), Point(0, 0)])
    res = s.value_counts()
    exp = pd.Series([2, 1], index=[Point(0, 0), Point(1, 1)])
    assert_series_equal(res, exp)


@pytest.mark.xfail(strict=False)
def test_drop_duplicates_series():
    # duplicated does not yet use EA machinery
    # (https://github.com/pandas-dev/pandas/issues/27264)
    # but relies on unstable hashing of unhashable objects in numpy array
    # giving flaky test (https://github.com/pandas-dev/pandas/issues/27035)
    dups = GeoSeries([Point(0, 0), Point(0, 0)])
    dropped = dups.drop_duplicates()
    assert len(dropped) == 1


@pytest.mark.xfail(strict=False)
def test_drop_duplicates_frame():
    # duplicated does not yet use EA machinery, see above
    gdf_len = 3
    dup_gdf = GeoDataFrame(
        {"geometry": [Point(0, 0) for _ in range(gdf_len)], "value1": range(gdf_len)}
    )
    dropped_geometry = dup_gdf.drop_duplicates(subset="geometry")
    assert len(dropped_geometry) == 1
    dropped_all = dup_gdf.drop_duplicates()
    assert len(dropped_all) == gdf_len


def test_groupby(df):

    # counts work fine
    res = df.groupby("value2").count()
    exp = pd.DataFrame(
        {"geometry": [2, 1], "value1": [2, 1], "value2": [1, 2]}
    ).set_index("value2")
    assert_frame_equal(res, exp)

    # reductions ignore geometry column
    res = df.groupby("value2").sum()
    exp = pd.DataFrame({"value1": [2, 1], "value2": [1, 2]}, dtype="int64").set_index(
        "value2"
    )
    assert_frame_equal(res, exp)

    # applying on the geometry column
    res = df.groupby("value2")["geometry"].apply(lambda x: x.cascaded_union)
    exp = pd.Series(
        [shapely.geometry.MultiPoint([(0, 0), (2, 2)]), Point(1, 1)],
        index=pd.Index([1, 2], name="value2"),
        name="geometry",
    )
    assert_series_equal(res, exp)


def test_groupby_groups(df):
    g = df.groupby("value2")
    res = g.get_group(1)
    assert isinstance(res, GeoDataFrame)
    exp = df.loc[[0, 2]]
    assert_frame_equal(res, exp)


def test_apply_loc_len1(df):
    # subset of len 1 with loc -> bug in pandas with inconsistent Block ndim
    # resulting in bug in apply
    # https://github.com/geopandas/geopandas/issues/1078
    subset = df.loc[[0], "geometry"]
    result = subset.apply(lambda geom: geom.is_empty)
    expected = subset.is_empty
    np.testing.assert_allclose(result, expected)
