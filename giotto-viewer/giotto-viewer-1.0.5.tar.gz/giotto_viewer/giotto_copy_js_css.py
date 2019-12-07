import sys
import os
import numpy as np
import scipy
import argparse
import json
import jsbeautifier
import shutil
import giotto_viewer

def main():
	parser = argparse.ArgumentParser(description="giotto_copy_js_css", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	parser.add_argument("--output", dest="output_dir", type=str, required=True)

	args = parser.parse_args()

	dirname = os.path.dirname(giotto_viewer.__file__)
	shutil.copytree(dirname+"/css", "%s/css" % args.output_dir)
	shutil.copytree(dirname+"/js", "%s/js" % args.output_dir)
	
if __name__=="__main__":
	main()	
