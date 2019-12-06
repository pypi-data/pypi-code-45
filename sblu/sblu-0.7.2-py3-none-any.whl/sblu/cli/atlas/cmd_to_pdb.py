import click
from sblu.io.atlas import parse_atlas_stream
import numpy as np
from prody import writePDBStream


@click.command('to_pdb', short_help='Convert ATLAS JSON to a PDB file.')
@click.argument('json_file', type=click.File(mode='r'))
@click.option('--hetatm',
              is_flag=True,
              help='Save all atoms as HETATM')
@click.option('--resn', help='Set residue name to this value (must be 3 character long) for all atoms.')
@click.option('-o', '--outfile',
              type=click.File(mode='w'),
              default=click.open_file('-', 'w'))
def cli(json_file, hetatm, resn, outfile):
    atomgrp = parse_atlas_stream(json_file)
    natoms = len(atomgrp)

    if resn is not None:
        if len(resn) != 3:
            raise click.BadParameter('should be 3 character long. Value "{}" is {} character long'.
                                     format(resn, len(resn)), param_hint='--resn')
        atomgrp.setResnames([resn] * natoms)

    if hetatm:
        atomgrp.setFlags('hetatm', np.ones(natoms, dtype=bool))

    writePDBStream(outfile, atomgrp)
