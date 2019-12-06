import os
import filecmp
from click.testing import CliRunner
import pytest

from .. import DATA_DIR
from sblu.cli.pdb import cmd_get

with open(DATA_DIR / "pdb_list") as f:
    pdbs = [l.strip().split()[0] for l in f]

pdbs = [pdb for pdb in pdbs if len(pdb) == 4]

def test_get_invalid():
    runner = CliRunner()

    result = runner.invoke(cmd_get.cli, [])
    assert result.exit_code == 2


@pytest.mark.need_network
@pytest.mark.parametrize("pdb", pdbs)
def test_get(pdb):
    runner = CliRunner()

    with runner.isolated_filesystem():
        expected_pdb = DATA_DIR / 'pdb' / (pdb + '.pdb')
        out_pdb = pdb + '.pdb'

        params = [pdb]
        result = runner.invoke(cmd_get.cli, params)

        assert result.exit_code == 0
        #only keep ATOM, HETATOM, and END lines
        with open(out_pdb) as inp, open("atoms.pdb", "w") as out:
            for l in inp:
                if l.startswith("ATOM  ") or l.startswith("HETATM") or \
                   l.startswith("END   ") or l.startswith("TER   "):
                    out.write(l)
        assert filecmp.cmp("atoms.pdb", expected_pdb)
