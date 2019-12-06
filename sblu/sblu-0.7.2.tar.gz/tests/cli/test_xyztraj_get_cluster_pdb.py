import filecmp
from click.testing import CliRunner

from .. import DATA_DIR
from sblu.cli.xyztraj import cmd_gen_cluster_pdb


def test_gen_cluster_pdb():
    """
    This test uses same cluster center positions as docking gen_cluster_pdb test.
    Appropriate coordinates are artificially inserted into xyztraj_long.xyz based on ft.cluster_models and rot.cluster_models.mol2
    Rotation matrices were converted to quaternions.
    Translation vectors were adjusted by initial ligand centroid to mimic behavior of docking gen_cluster_pdb.
    """
    runner = CliRunner()

    with runner.isolated_filesystem():
        cluster_file = DATA_DIR / 'clusters.test'
        xyztraj_file = DATA_DIR / 'xyztraj_long.xyz'
        lig_file = DATA_DIR / 'pdb' / 'cluster_models' / '1avx_l_u_nmin.pdb'

        result = runner.invoke(cmd_gen_cluster_pdb.cli, [cluster_file, xyztraj_file, '1', lig_file,
                                                         '-o', 'output', '--max-clusters', '2'])

        assert result.exit_code == 0
        # Validate output pdb files
        for i in range(2):
            expected_pdb = DATA_DIR / 'pdb' / 'cluster_models' / "lig.{:02d}.pdb".format(i)
            assert filecmp.cmp("output.{:02d}.pdb".format(i), expected_pdb)
