import sys
from typing import List

import dirlistproc
from jsonasobj import as_json
from pyshex.shex_evaluator import ShExEvaluator
from rdflib import Namespace


def do_shex(input_fn: str, output_fn: str, _: Namespace) -> bool:
    evaluator: ShExEvaluator = ShExEvaluator(schema=input_fn)
    with open(output_fn, 'w') as f:
        # TODO: Add the context in or create a function in the evaluator that emits the full JSON string
        f.write(as_json(evaluator._schema))
    return True


def main(argv: List[str] = None):
    """
    Turn any ShEx files in indir into ShExJ in outdir
    :param argv: Argument list.  If None, use sys.argv
    :return: 0 if conversion was successful, 1 if errors
    """
    dlp = dirlistproc.DirectoryListProcessor(argv, "ShEx to ShExJ converter", ".shex", ".shexj")
    if not (dlp.opts.infile or dlp.opts.indir):
        dirlistproc.DirectoryListProcessor(["--help"], "ShEx to ShExJ converter", ".shex", ".shexj")
    nfiles, nsuccess = dlp.run(do_shex)
    print(f"Total={nfiles} Successful={nsuccess}")
    return 0 if nfiles == nsuccess else 1


if __name__ == '__main__':
    main(sys.argv[1:])
