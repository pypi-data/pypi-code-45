import os
from click.testing import CliRunner
import filecmp

from sblu.cli.atlas import cmd_to_pdb

from .. import DATA_DIR


def test_to_pdb():
    runner = CliRunner()

    with runner.isolated_filesystem():
        json_file = DATA_DIR / 'small_molecule.json'
        expected_pdb = DATA_DIR / 'small_molecule.default.pdb'

        result = runner.invoke(cmd_to_pdb.cli, [json_file, '-o', 'out.pdb'])

        assert result.exit_code == 0
        assert os.path.exists('out.pdb')
        assert filecmp.cmp('out.pdb', expected_pdb)

    with runner.isolated_filesystem():
        json_file = DATA_DIR / 'small_molecule.json'
        expected_pdb = DATA_DIR / 'small_molecule.params.pdb'

        result = runner.invoke(cmd_to_pdb.cli, [json_file, '--hetatm', '--resn', 'LIG', '-o', 'out.pdb'])

        assert result.exit_code == 0
        assert os.path.exists('out.pdb')
        assert filecmp.cmp('out.pdb', expected_pdb)
