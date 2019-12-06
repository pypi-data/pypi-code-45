import click
import numpy as np
import logging

from prody import parsePDB, writePDB, AtomGroup

from sblu.cluster import read_clusters
from sblu.xyztraj import xyz_stream

logger = logging.getLogger(__name__)


def _reset_atom_group_center(atom_group: AtomGroup) -> None:
    """Move `atom_group` so it's centroid is at the origin. Inplace."""
    coords = atom_group.getCoords()  # This returns a copy so we can mutate it
    center = np.mean(coords, axis=0)
    coords -= center
    atom_group.setCoords(coords)


def _apply_transform_atom_group(atom_group: AtomGroup, rot_matrix: np.ndarray, translation_vector: np.ndarray) -> AtomGroup:
    """Apply rotation and then translation to atom group coordinates. Return new AtomGroup with changed coordinates."""
    assert rot_matrix.shape == (3, 3)
    assert translation_vector.shape == (3, )

    out = atom_group.copy()

    orig_coords = atom_group.getCoords()
    new_coords = np.dot(rot_matrix,
                        orig_coords.T)
    new_coords = (new_coords.T + translation_vector)
    out.setCoords(new_coords)

    return out


@click.command('gen_cluster_pdb',
               short_help="Generate pdb models for cluster centers.")
@click.argument("clusterfile", type=click.Path(exists='true'))
@click.argument("xyzfile", type=click.File(mode='r'))
@click.argument("particle_id", type=click.INT)
@click.argument("lig_file", type=click.Path(exists=True))
@click.option('-o', "--output-prefix", type=click.STRING,
              default="lig",
              help="Common prefix for output pdb files (default: lig)")
@click.option('-l', "--max-clusters", type=click.INT,
              default=None,
              help="Number of top clusters to build models for (default: all)")
def cli(clusterfile, xyzfile, particle_id, lig_file,
        output_prefix, max_clusters):
    cluster_data = read_clusters(clusterfile)

    cluster_centers = [cluster["center"]
                       for cluster in cluster_data["clusters"][:max_clusters]]

    lig = parsePDB(lig_file)
    _reset_atom_group_center(lig)

    clusters_written = 0

    for frame_id, frame in enumerate(xyz_stream(xyzfile)):
        if frame_id in cluster_centers:
            particle = frame.particles[particle_id]
            cluster_id = cluster_centers.index(frame_id)
            transformed = _apply_transform_atom_group(lig, particle.r, particle.t)
            model_fname = output_prefix + "." + "{:02d}".format(cluster_id)
            writePDB(model_fname, transformed, csets=[0])
            clusters_written += 1

    if clusters_written != len(cluster_centers):
        logger.error("Found frames corresponding to only {} out of {} clusters".format(clusters_written, len(cluster_centers)))
