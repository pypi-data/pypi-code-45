import matplotlib.pyplot as plt
import csv
import gzip
import os
import scipy.io
import numpy as np
from scipy.sparse import csr_matrix, csc_matrix
from scipy.stats import zscore
import sys
from operator import itemgetter
import argparse

def get_map(t_array):
	t_map = {}
	for ind,v in enumerate(t_array):
		t_map[v] = ind
	return t_map

def read_list(n):
	f = open(n)
	ll = []
	for l in f:
		l = l.rstrip("\n")
		ll.append(l)
	f.close()
	return ll

def main():
	parser = argparse.ArgumentParser(description="read.matrix.custom", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	
	parser.add_argument("-i", "--input", dest="input_dir", type=str, required=True)
	parser.add_argument("-g", "--genes", dest="file_genes", type=str, required=True)
	parser.add_argument("-b", "--barcodes", dest="file_barcodes", type=str, required = True)
	parser.add_argument("-o", "--output", dest="output_dir", type=str, required=True)

	args = parser.parse_args()

	mat = scipy.io.mmread("%s/matrix.mtx.gz" % args.input_dir)
	feature_ids = [row[0] for row in csv.reader(gzip.open("%s/features.tsv.gz" % args.input_dir, "rt"), delimiter="\t")]
	gene_names = [row[1] for row in csv.reader(gzip.open("%s/features.tsv.gz" % args.input_dir, "rt"), delimiter="\t")]
	feature_types = [row[2] for row in csv.reader(gzip.open("%s/features.tsv.gz" % args.input_dir, "rt"), delimiter="\t")]
	barcodes = [row[0] for row in csv.reader(gzip.open("%s/barcodes.tsv.gz" % args.input_dir, "rt"), delimiter="\t")]

	mat = mat.todense()
	#print mat.shape
	map_genes = get_map(gene_names)
	map_barcodes = get_map(barcodes)
	gene_names = np.array(gene_names)
	barcodes = np.array(barcodes)
	
	#file_genes = sys.argv[1]
	#file_barcodes = sys.argv[2]
	
	n_genes = read_list(args.file_genes)
	n_barcodes = read_list(args.file_barcodes)

	good_ids = []	
	for gene in n_genes:
		good_ids.append(map_genes[gene])
	good_ids = np.array(good_ids)
	mat = mat[good_ids, :]
	gene_names = gene_names[good_ids]

	good_ids = []	
	for cell in n_barcodes:
		good_ids.append(map_barcodes[cell])
	good_ids = np.array(good_ids)
	mat = mat[:, good_ids]
	barcodes = barcodes[good_ids]

	mat = zscore(mat, axis=0) #per column
	mat = zscore(mat, axis=1) #per row

	fw = open("%s/zscored.matrix.txt" % args.output_dir, "w")
	for i in range(barcodes.shape[0]):
		fw.write(",%d" % i)
	fw.write("\n")
	for i in range(gene_names.shape[0]):
		fw.write(gene_names[i] + ",")
		val = ["%.2f" % mat[i,j] for j in range(mat.shape[1])]
		fw.write(",".join(val) + "\n")
	fw.close()

	fw = open("%s/filtered.genes.txt" % args.output_dir, "w")
	fw.write("\n".join(gene_names) + "\n")
	fw.close()

	fw = open("%s/filtered.barcodes.txt" % args.output_dir, "w")
	fw.write("\n".join(barcodes) + "\n")
	fw.close()
	

if __name__=="__main__":
	main()
