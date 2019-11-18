# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Regression tests for the units package
"""
import pickle
from fractions import Fraction

import pytest
import numpy as np
from numpy.testing import assert_allclose

from astropy.tests.helper import raises, catch_warnings

from astropy import units as u
from astropy import constants as c
from astropy.units import utils


def test_getting_started():
    """
    Corresponds to "Getting Started" section in the docs.
    """
    from astropy.units import imperial
    with imperial.enable():
        speed_unit = u.cm / u.s
        x = speed_unit.to(imperial.mile / u.hour, 1)
        assert_allclose(x, 0.02236936292054402)
        speed_converter = speed_unit._get_converter("mile hour^-1")
        x = speed_converter([1., 1000., 5000.])
        assert_allclose(x, [2.23693629e-02, 2.23693629e+01, 1.11846815e+02])


def test_initialisation():
    assert u.Unit(u.m) is u.m

    ten_meter = u.Unit(10.*u.m)
    assert ten_meter == u.CompositeUnit(10., [u.m], [1])
    assert u.Unit(ten_meter) is ten_meter

    assert u.Unit(10.*ten_meter) == u.CompositeUnit(100., [u.m], [1])

    foo = u.Unit('foo', (10. * ten_meter)**2, namespace=locals())
    assert foo == u.CompositeUnit(10000., [u.m], [2])

    assert u.Unit('m') == u.m
    assert u.Unit('') == u.dimensionless_unscaled
    assert u.one == u.dimensionless_unscaled
    assert u.Unit('10 m') == ten_meter
    assert u.Unit(10.) == u.CompositeUnit(10., [], [])


def test_invalid_power():
    x = u.m ** Fraction(1, 3)
    assert isinstance(x.powers[0], Fraction)

    x = u.m ** Fraction(1, 2)
    assert isinstance(x.powers[0], float)

    # Test the automatic conversion to a fraction
    x = u.m ** (1. / 3.)
    assert isinstance(x.powers[0], Fraction)


def test_invalid_compare():
    assert not (u.m == u.s)


def test_convert():
    assert u.h._get_converter(u.s)(1) == 3600


def test_convert_fail():
    with pytest.raises(u.UnitsError):
        u.cm.to(u.s, 1)
    with pytest.raises(u.UnitsError):
        (u.cm / u.s).to(u.m, 1)


def test_composite():
    assert (u.cm / u.s * u.h)._get_converter(u.m)(1) == 36
    assert u.cm * u.cm == u.cm ** 2

    assert u.cm * u.cm * u.cm == u.cm ** 3

    assert u.Hz.to(1000 * u.Hz, 1) == 0.001


def test_str():
    assert str(u.cm) == "cm"


def test_repr():
    assert repr(u.cm) == 'Unit("cm")'


def test_represents():
    assert u.m.represents is u.m
    assert u.km.represents.scale == 1000.
    assert u.km.represents.bases == [u.m]
    assert u.Ry.scale == 1.0 and u.Ry.bases == [u.Ry]
    assert_allclose(u.Ry.represents.scale, 13.605692518464949)
    assert u.Ry.represents.bases == [u.eV]
    bla = u.def_unit('bla', namespace=locals())
    assert bla.represents is bla
    blabla = u.def_unit('blabla', 10 * u.hr, namespace=locals())
    assert blabla.represents.scale == 10.
    assert blabla.represents.bases == [u.hr]
    assert blabla.decompose().scale == 10 * 3600
    assert blabla.decompose().bases == [u.s]


def test_units_conversion():
    assert_allclose(u.kpc.to(u.Mpc), 0.001)
    assert_allclose(u.Mpc.to(u.kpc), 1000)
    assert_allclose(u.yr.to(u.Myr), 1.e-6)
    assert_allclose(u.AU.to(u.pc), 4.84813681e-6)
    assert_allclose(u.cycle.to(u.rad), 6.283185307179586)


def test_units_manipulation():
    # Just do some manipulation and check it's happy
    (u.kpc * u.yr) ** Fraction(1, 3) / u.Myr
    (u.AA * u.erg) ** 9


def test_decompose():
    assert u.Ry == u.Ry.decompose()


def test_dimensionless_to_si():
    """
    Issue #1150: Test for conversion of dimensionless quantities
                 to the SI system
    """

    testunit = ((1.0 * u.kpc) / (1.0 * u.Mpc))

    assert testunit.unit.physical_type == 'dimensionless'
    assert_allclose(testunit.si, 0.001)


def test_dimensionless_to_cgs():
    """
    Issue #1150: Test for conversion of dimensionless quantities
                 to the CGS system
    """

    testunit = ((1.0 * u.m) / (1.0 * u.km))

    assert testunit.unit.physical_type == 'dimensionless'
    assert_allclose(testunit.cgs, 0.001)


def test_unknown_unit():
    with catch_warnings(u.UnitsWarning) as warning_lines:
        u.Unit("FOO", parse_strict='warn')

    assert 'FOO' in str(warning_lines[0].message)


def test_multiple_solidus():
    assert u.Unit("m/s/kg").to_string() == u.m / u.s / u.kg

    with catch_warnings(u.UnitsWarning) as warning_lines:
        assert u.Unit("m/s/kg").to_string() == 'm / (kg s)'

    assert 'm/s/kg' in str(warning_lines[0].message)
    assert 'discouraged' in str(warning_lines[0].message)

    with pytest.raises(ValueError):
        u.Unit("m/s/kg", format="vounit")

    # Regression test for #9000: solidi in exponents do not count towards this.
    x = u.Unit("kg(3/10) * m(5/2) / s", format="vounit")
    assert x.to_string() == 'kg(3/10) m(5/2) / s'


def test_unknown_unit3():
    unit = u.Unit("FOO", parse_strict='silent')
    assert isinstance(unit, u.UnrecognizedUnit)
    assert unit.name == "FOO"

    unit2 = u.Unit("FOO", parse_strict='silent')
    assert unit == unit2
    assert unit.is_equivalent(unit2)

    unit3 = u.Unit("BAR", parse_strict='silent')
    assert unit != unit3
    assert not unit.is_equivalent(unit3)

    # Also test basic (in)equalities.
    assert unit == "FOO"
    assert unit != u.m
    # next two from gh-7603.
    assert unit != None  # noqa
    assert unit not in (None, u.m)

    with pytest.raises(ValueError):
        unit._get_converter(unit3)

    x = unit.to_string('latex')
    y = unit2.to_string('cgs')

    with pytest.raises(ValueError):
        unit4 = u.Unit("BAR", parse_strict='strict')

    with pytest.raises(TypeError):
        unit5 = u.Unit(None)


@raises(TypeError)
def test_invalid_scale():
    x = ['a', 'b', 'c'] * u.m


def test_cds_power():
    unit = u.Unit("10+22/cm2", format="cds", parse_strict='silent')
    assert unit.scale == 1e22


def test_register():
    foo = u.def_unit("foo", u.m ** 3, namespace=locals())
    assert 'foo' in locals()
    with u.add_enabled_units(foo):
        assert 'foo' in u.get_current_unit_registry().registry
    assert 'foo' not in u.get_current_unit_registry().registry


def test_in_units():
    speed_unit = u.cm / u.s
    x = speed_unit.in_units(u.pc / u.hour, 1)


def test_null_unit():
    assert (u.m / u.m) == u.Unit(1)


def test_unrecognized_equivalency():
    assert u.m.is_equivalent('foo') is False
    assert u.m.is_equivalent('pc') is True


@raises(TypeError)
def test_unit_noarg():
    u.Unit()


def test_convertible_exception():
    try:
        u.AA.to(u.h * u.s ** 2)
    except u.UnitsError as e:
        assert "length" in str(e)


def test_convertible_exception2():
    try:
        u.m.to(u.s)
    except u.UnitsError as e:
        assert "length" in str(e)


@raises(TypeError)
def test_invalid_type():
    class A:
        pass

    u.Unit(A())


def test_steradian():
    """
    Issue #599
    """
    assert u.sr.is_equivalent(u.rad * u.rad)

    results = u.sr.compose(units=u.cgs.bases)
    assert results[0].bases[0] is u.rad

    results = u.sr.compose(units=u.cgs.__dict__)
    assert results[0].bases[0] is u.sr


def test_decompose_bases():
    """
    From issue #576
    """

    from astropy.units import cgs
    from astropy.constants import e

    d = e.esu.unit.decompose(bases=cgs.bases)
    assert d._bases == [u.cm, u.g, u.s]
    assert d._powers == [Fraction(3, 2), 0.5, -1]
    assert d._scale == 1.0


def test_complex_compose():
    complex = u.cd * u.sr * u.Wb
    composed = complex.compose()

    assert set(composed[0]._bases) == set([u.lm, u.Wb])


def test_equiv_compose():
    composed = u.m.compose(equivalencies=u.spectral())
    assert any([u.Hz] == x.bases for x in composed)


def test_empty_compose():
    with pytest.raises(u.UnitsError):
        composed = u.m.compose(units=[])


def _unit_as_str(unit):
    # This function serves two purposes - it is used to sort the units to
    # test alphabetically, and it is also use to allow pytest to show the unit
    # in the [] when running the parametrized tests.
    return str(unit)


# We use a set to make sure we don't have any duplicates.
COMPOSE_ROUNDTRIP = set()
for val in u.__dict__.values():
    if (isinstance(val, u.UnitBase) and
            not isinstance(val, u.PrefixUnit)):
        COMPOSE_ROUNDTRIP.add(val)


@pytest.mark.parametrize('unit', sorted(COMPOSE_ROUNDTRIP, key=_unit_as_str), ids=_unit_as_str)
def test_compose_roundtrip(unit):
    composed_list = unit.decompose().compose()
    found = False
    for composed in composed_list:
        if len(composed.bases):
            if composed.bases[0] is unit:
                found = True
                break
        elif len(unit.bases) == 0:
            found = True
            break
    assert found


# We use a set to make sure we don't have any duplicates.
COMPOSE_CGS_TO_SI = set()
for val in u.cgs.__dict__.values():
    # Can't decompose Celsius
    if (isinstance(val, u.UnitBase) and
            not isinstance(val, u.PrefixUnit) and
            val != u.cgs.deg_C):
        COMPOSE_CGS_TO_SI.add(val)


@pytest.mark.parametrize('unit', sorted(COMPOSE_CGS_TO_SI, key=_unit_as_str),
                         ids=_unit_as_str)
def test_compose_cgs_to_si(unit):
    si = unit.to_system(u.si)
    assert [x.is_equivalent(unit) for x in si]
    assert si[0] == unit.si


# We use a set to make sure we don't have any duplicates.
COMPOSE_SI_TO_CGS = set()
for val in u.si.__dict__.values():
    # Can't decompose Celsius
    if (isinstance(val, u.UnitBase) and
            not isinstance(val, u.PrefixUnit) and
            val != u.si.deg_C):
        COMPOSE_SI_TO_CGS.add(val)


@pytest.mark.parametrize('unit', sorted(COMPOSE_SI_TO_CGS, key=_unit_as_str), ids=_unit_as_str)
def test_compose_si_to_cgs(unit):

    # Can't convert things with Ampere to CGS without more context
    try:
        cgs = unit.to_system(u.cgs)
    except u.UnitsError:
        if u.A in unit.decompose().bases:
            pass
        else:
            raise
    else:
        assert [x.is_equivalent(unit) for x in cgs]
        assert cgs[0] == unit.cgs


def test_to_cgs():
    assert u.Pa.to_system(u.cgs)[1]._bases[0] is u.Ba
    assert u.Pa.to_system(u.cgs)[1]._scale == 10.0


def test_decompose_to_cgs():
    from astropy.units import cgs
    assert u.m.decompose(bases=cgs.bases)._bases[0] is cgs.cm


def test_compose_issue_579():
    unit = u.kg * u.s ** 2 / u.m

    result = unit.compose(units=[u.N, u.s, u.m])

    assert len(result) == 1
    assert result[0]._bases == [u.s, u.N, u.m]
    assert result[0]._powers == [4, 1, -2]


def test_compose_prefix_unit():
    x =  u.m.compose(units=(u.m,))
    assert x[0].bases[0] is u.m
    assert x[0].scale == 1.0
    x = u.m.compose(units=[u.km], include_prefix_units=True)
    assert x[0].bases[0] is u.km
    assert x[0].scale == 0.001
    x = u.m.compose(units=[u.km])
    assert x[0].bases[0] is u.km
    assert x[0].scale == 0.001

    x = (u.km/u.s).compose(units=(u.pc, u.Myr))
    assert x[0].bases == [u.pc, u.Myr]
    assert_allclose(x[0].scale, 1.0227121650537077)

    with raises(u.UnitsError):
        (u.km/u.s).compose(units=(u.pc, u.Myr), include_prefix_units=False)


def test_self_compose():
    unit = u.kg * u.s

    assert len(unit.compose(units=[u.g, u.s])) == 1


@raises(u.UnitsError)
def test_compose_failed():
    unit = u.kg

    result = unit.compose(units=[u.N])


def test_compose_fractional_powers():
    # Warning: with a complicated unit, this test becomes very slow;
    # e.g., x = (u.kg / u.s ** 3 * u.au ** 2.5 / u.yr ** 0.5 / u.sr ** 2)
    # takes 3 s
    x = u.m ** 0.5 / u.yr ** 1.5

    factored = x.compose()

    for unit in factored:
        assert x.decompose() == unit.decompose()

    factored = x.compose(units=u.cgs)

    for unit in factored:
        assert x.decompose() == unit.decompose()

    factored = x.compose(units=u.si)

    for unit in factored:
        assert x.decompose() == unit.decompose()


def test_compose_best_unit_first():
    results = u.l.compose()
    assert len(results[0].bases) == 1
    assert results[0].bases[0] is u.l

    results = (u.s ** -1).compose()
    assert results[0].bases[0] in (u.Hz, u.Bq)

    results = (u.Ry.decompose()).compose()
    assert results[0].bases[0] is u.Ry


def test_compose_no_duplicates():
    new = u.kg / u.s ** 3 * u.au ** 2.5 / u.yr ** 0.5 / u.sr ** 2
    composed = new.compose(units=u.cgs.bases)
    assert len(composed) == 1


def test_long_int():
    """
    Issue #672
    """
    sigma = 10 ** 21 * u.M_p / u.cm ** 2
    sigma.to(u.M_sun / u.pc ** 2)


def test_endian_independence():
    """
    Regression test for #744

    A logic issue in the units code meant that big endian arrays could not be
    converted because the dtype is '>f4', not 'float32', and the code was
    looking for the strings 'float' or 'int'.
    """
    for endian in ['<', '>']:
        for ntype in ['i', 'f']:
            for byte in ['4', '8']:
                x = np.array([1, 2, 3], dtype=(endian + ntype + byte))
                u.m.to(u.cm, x)


def test_radian_base():
    """
    Issue #863
    """
    assert (1 * u.degree).si.unit == u.rad


def test_no_as():
    # We don't define 'as', since it is a keyword, but we
    # do want to define the long form (`attosecond`).
    assert not hasattr(u, 'as')
    assert hasattr(u, 'attosecond')


def test_no_duplicates_in_names():
    # Regression test for #5036
    assert u.ct.names == ['ct', 'count']
    assert u.ct.short_names == ['ct', 'count']
    assert u.ct.long_names == ['count']
    assert set(u.ph.names) == set(u.ph.short_names) | set(u.ph.long_names)


def test_pickling():
    p = pickle.dumps(u.m)
    other = pickle.loads(p)

    assert other is u.m

    new_unit = u.IrreducibleUnit(['foo'], format={'baz': 'bar'})
    # This is local, so the unit should not be registered.
    assert 'foo' not in u.get_current_unit_registry().registry

    # Test pickling of this unregistered unit.
    p = pickle.dumps(new_unit)
    new_unit_copy = pickle.loads(p)
    assert new_unit_copy.names == ['foo']
    assert new_unit_copy.get_format_name('baz') == 'bar'
    # It should still not be registered.
    assert 'foo' not in u.get_current_unit_registry().registry

    # Now try the same with a registered unit.
    with u.add_enabled_units([new_unit]):
        p = pickle.dumps(new_unit)
        assert 'foo' in u.get_current_unit_registry().registry

    # Check that a registered unit can be loaded and that it gets re-enabled.
    with u.add_enabled_units([]):
        assert 'foo' not in u.get_current_unit_registry().registry
        new_unit_copy = pickle.loads(p)
        assert new_unit_copy.names == ['foo']
        assert new_unit_copy.get_format_name('baz') == 'bar'
        assert 'foo' in u.get_current_unit_registry().registry

    # And just to be sure, that it gets removed outside of the context.
    assert 'foo' not in u.get_current_unit_registry().registry


def test_pickle_unrecognized_unit():
    """
    Issue #2047
    """
    a = u.Unit('asdf', parse_strict='silent')
    pickle.loads(pickle.dumps(a))


@raises(ValueError)
def test_duplicate_define():
    u.def_unit('m', namespace=u.__dict__)


def test_all_units():
    from astropy.units.core import get_current_unit_registry
    registry = get_current_unit_registry()
    assert len(registry.all_units) > len(registry.non_prefix_units)


def test_repr_latex():
    assert u.m._repr_latex_() == u.m.to_string('latex')


def test_operations_with_strings():
    assert u.m / '5s' == (u.m / (5.0 * u.s))

    assert u.m * '5s' == (5.0 * u.m * u.s)


def test_comparison():
    assert u.m > u.cm
    assert u.m >= u.cm
    assert u.cm < u.m
    assert u.cm <= u.m

    with pytest.raises(u.UnitsError):
        u.m > u.kg


def test_compose_into_arbitrary_units():
    # Issue #1438
    from astropy.constants import G
    G.decompose([u.kg, u.km, u.Unit("15 s")])


def test_unit_multiplication_with_string():
    """Check that multiplication with strings produces the correct unit."""
    u1 = u.cm
    us = 'kg'
    assert us * u1 == u.Unit(us) * u1
    assert u1 * us == u1 * u.Unit(us)


def test_unit_division_by_string():
    """Check that multiplication with strings produces the correct unit."""
    u1 = u.cm
    us = 'kg'
    assert us / u1 == u.Unit(us) / u1
    assert u1 / us == u1 / u.Unit(us)


def test_sorted_bases():
    """See #1616."""
    assert (u.m * u.Jy).bases == (u.Jy * u.m).bases


def test_megabit():
    """See #1543"""
    assert u.Mbit is u.Mb
    assert u.megabit is u.Mb

    assert u.Mbyte is u.MB
    assert u.megabyte is u.MB


def test_composite_unit_get_format_name():
    """See #1576"""
    unit1 = u.Unit('nrad/s')
    unit2 = u.Unit('Hz(1/2)')
    assert (str(u.CompositeUnit(1, [unit1, unit2], [1, -1])) ==
            'nrad / (Hz(1/2) s)')


def test_unicode_policy():
    from astropy.tests.helper import assert_follows_unicode_guidelines

    assert_follows_unicode_guidelines(
        u.degree, roundtrip=u.__dict__)


def test_suggestions():
    for search, matches in [
            ('microns', 'micron'),
            ('s/microns', 'micron'),
            ('M', 'm'),
            ('metre', 'meter'),
            ('angstroms', 'Angstrom or angstrom'),
            ('milimeter', 'millimeter'),
            ('ångström', 'Angstrom or angstrom'),
            ('kev', 'EV, eV, kV or keV')]:
        try:
            u.Unit(search)
        except ValueError as e:
            assert 'Did you mean {0}?'.format(matches) in str(e)
        else:
            assert False, 'Expected ValueError'


def test_fits_hst_unit():
    """See #1911."""
    x = u.Unit("erg /s /cm**2 /angstrom")
    assert x == u.erg * u.s ** -1 * u.cm ** -2 * u.angstrom ** -1


def test_barn_prefixes():
    """Regression test for https://github.com/astropy/astropy/issues/3753"""

    assert u.fbarn is u.femtobarn
    assert u.pbarn is u.picobarn


def test_fractional_powers():
    """See #2069"""
    m = 1e9 * u.Msun
    tH = 1. / (70. * u.km / u.s / u.Mpc)
    vc = 200 * u.km/u.s

    x = (c.G ** 2 * m ** 2 * tH.cgs) ** Fraction(1, 3) / vc
    v1 = x.to('pc')

    x = (c.G ** 2 * m ** 2 * tH) ** Fraction(1, 3) / vc
    v2 = x.to('pc')

    x = (c.G ** 2 * m ** 2 * tH.cgs) ** (1.0 / 3.0) / vc
    v3 = x.to('pc')

    x = (c.G ** 2 * m ** 2 * tH) ** (1.0 / 3.0) / vc
    v4 = x.to('pc')

    assert_allclose(v1, v2)
    assert_allclose(v2, v3)
    assert_allclose(v3, v4)

    x = u.m ** (1.0 / 101.0)
    assert isinstance(x.powers[0], float)

    x = u.m ** (3.0 / 7.0)
    assert isinstance(x.powers[0], Fraction)
    assert x.powers[0].numerator == 3
    assert x.powers[0].denominator == 7

    x = u.cm ** Fraction(1, 2) * u.cm ** Fraction(2, 3)
    assert isinstance(x.powers[0], Fraction)
    assert x.powers[0] == Fraction(7, 6)

    # Regression test for #9258.
    x = (u.TeV ** (-2.2)) ** (1/-2.2)
    assert isinstance(x.powers[0], Fraction)
    assert x.powers[0] == Fraction(1, 1)


def test_inherit_docstrings():
    assert u.UnrecognizedUnit.is_unity.__doc__ == u.UnitBase.is_unity.__doc__


def test_sqrt_mag():
    sqrt_mag = u.mag ** 0.5
    assert hasattr(sqrt_mag.decompose().scale, 'imag')
    assert (sqrt_mag.decompose())**2 == u.mag


def test_composite_compose():
    # Issue #2382
    composite_unit = u.s.compose(units=[u.Unit("s")])[0]
    u.s.compose(units=[composite_unit])


def test_data_quantities():
    assert u.byte.is_equivalent(u.bit)


def test_compare_with_none():
    # Ensure that equality comparisons with `None` work, and don't
    # raise exceptions.  We are deliberately not using `is None` here
    # because that doesn't trigger the bug.  See #3108.
    assert not (u.m == None)  # nopep8
    assert u.m != None  # nopep8


def test_validate_power_detect_fraction():
    frac = utils.validate_power(1.1666666666666665)
    assert isinstance(frac, Fraction)
    assert frac.numerator == 7
    assert frac.denominator == 6


def test_complex_fractional_rounding_errors():
    # See #3788

    kappa = 0.34 * u.cm**2 / u.g
    r_0 = 886221439924.7849 * u.cm
    q = 1.75
    rho_0 = 5e-10 * u.solMass / u.solRad**3
    y = 0.5
    beta = 0.19047619047619049
    a = 0.47619047619047628
    m_h = 1e6*u.solMass

    t1 = 2 * c.c / (kappa * np.sqrt(np.pi))
    t2 = (r_0**-q) / (rho_0 * y * beta * (a * c.G * m_h)**0.5)

    result = ((t1 * t2)**-0.8)

    assert result.unit.physical_type == 'length'
    result.to(u.solRad)


def test_fractional_rounding_errors_simple():
    x = (u.m ** 1.5) ** Fraction(4, 5)
    assert isinstance(x.powers[0], Fraction)
    assert x.powers[0].numerator == 6
    assert x.powers[0].denominator == 5


def test_enable_unit_groupings():
    from astropy.units import cds

    with cds.enable():
        assert cds.geoMass in u.kg.find_equivalent_units()

    from astropy.units import imperial
    with imperial.enable():
        assert imperial.inch in u.m.find_equivalent_units()


def test_unit_summary_prefixes():
    """
    Test for a few units that the unit summary table correctly reports
    whether or not that unit supports prefixes.

    Regression test for https://github.com/astropy/astropy/issues/3835
    """

    from astropy.units import astrophys

    for summary in utils._iter_unit_summary(astrophys.__dict__):
        unit, _, _, _, prefixes = summary

        if unit.name == 'lyr':
            assert prefixes
        elif unit.name == 'pc':
            assert prefixes
        elif unit.name == 'barn':
            assert prefixes
        elif unit.name == 'cycle':
            assert prefixes == 'No'
        elif unit.name == 'vox':
            assert prefixes == 'Yes'


def test_raise_to_negative_power():
    """Test that order of bases is changed when raising to negative power.

    Regression test for https://github.com/astropy/astropy/issues/8260
    """
    m2s2 = u.m ** 2 / u.s **2
    spm = m2s2 ** (-1 / 2)
    assert spm.bases == [u.s, u.m]
    assert spm.powers == [1, -1]
    assert spm == u.s / u.m
