import sys
import os
import os.path
import terminalmushroom


def cli():
    if len(sys.argv) not in [2, 3]:
        print('Terminal Mushroom Version {}'.format(terminalmushroom.__version__))
        print('Usage: {script} input-file [output-file]'.format(script=terminalmushroom.__name__))
        return

    in_file = sys.argv[1]
    with open(in_file, 'r') as f:
        flat_string = f.read()

    output = terminalmushroom.compile_source(flat_string, False, os.path.basename(in_file))

    if len(sys.argv) == 3:
        out_file = sys.argv[2]
        with open(out_file, 'wb') as f:
            f.write(output)
    else:
        os.write(sys.stdout.fileno(), output)
        sys.stdout.flush()


if __name__ == '__main__':
    cli()
