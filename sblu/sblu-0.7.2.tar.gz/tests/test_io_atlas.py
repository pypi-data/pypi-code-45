"""
Test reading Atlas JSON files.
"""

from . import DATA_DIR

from sblu.io import atlas
from prody import AtomGroup
import re


def test_parse_atlas():
    atomgroup = atlas.parse_atlas(DATA_DIR / "small_molecule.json")
    assert isinstance(atomgroup, AtomGroup)
    assert len(atomgroup) == 40
    assert atomgroup.numAtoms() == 40
    assert atomgroup.getCoords().shape == (40, 3)

    for atom_num, atom in enumerate(atomgroup):
        assert atom.getIndex() == atom_num
        assert re.match(r'[CNOH]\d+', atom.getName())
        assert atom.getResname() == ''  # No 'residue_name' field
        assert atom.getResnum() == 1
        assert atom.getChid() == 'X'  # CHain ID
        assert atom.getFlag('hetatm') == False
