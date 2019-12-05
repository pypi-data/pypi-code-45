#!/usr/bin/env python3

import argparse
from esa import ESA

def create_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", required = False, action = "store_true")
    parser.add_argument("-c", required = True)
    #parser.add_argument("-s", required = False, default = "cos", \
    #                    choices = ["cos", "max", "avg"], \
    #                    help  = "similarity measure to use")
    parser.add_argument('document', nargs = argparse.REMAINDER)
    return parser


def main():
    parser = create_argparser()
    args = parser.parse_args()

    word_level = vars(args)["w"]
    matrix_path = vars(args)["c"]
    #similarity = vars(args)["s"]

    try:
        input_document = vars(args)["document"][0]

        esa = ESA(matrix_path)
        results = esa.process(input_document, word_level)

        if not word_level: 
            for result in results:
                print(f"{results[result]:30.30f} {result}")
        else:
            for result in results:
                print(f"{result} - {results[result]}")
    except IndexError:
        print("ERROR: no input text specified")
  

if __name__ == "__main__":
    main()