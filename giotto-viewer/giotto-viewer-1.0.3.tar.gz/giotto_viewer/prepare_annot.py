import sys
import os
import numpy as np
import scipy
import argparse

def read_cluster(n):
	f = open(n)
	h = f.readline()
	names = []
	clust = []
	for l in f:
		l = l.rstrip("\n")
		ll = l.split(",")
		cell = ll[0]
		cl = int(ll[1])
		names.append(cell)
		clust.append(cl)
	f.close()
	names = np.array(names)
	clust = np.array(clust)
	return names, clust

def read_tsne(n):
	f = open(n)
	f.readline()
	names = []
	pos = []
	for l in f:
		l = l.rstrip("\n")
		ll = l.split(",")
		cell = ll[0]
		pos.append((float(ll[1]), float(ll[2])))
		names.append(cell)
	f.close()
	names = np.array(names)
	Xcen = np.empty((len(names), 2), dtype="float32")
	for ind,(i,j) in enumerate(pos):
		Xcen[ind,:] = [i,j]
	return names, Xcen

def read_column_order(n):
	f = open(n)
	names = []
	for l in f:
		l = l.rstrip("\n")
		names.append(l)
	f.close()
	return names

def read_physical(n):
	f = open(n)
	names = []
	pos = []
	for l in f:
		l = l.rstrip("\n")
		ll = l.split(",")
		cell = ll[0]
		names.append(cell)
		pos.append((float(ll[-2]), float(ll[-1])))
	f.close()
	names = np.array(names)
	Xcen = np.empty((len(names), 2), dtype="float32")
	for ind,(i,j) in enumerate(pos):
		Xcen[ind,:] = [i,j]
	return names, Xcen	

def get_map(t_array):
	t_map = {}
	for ind,v in enumerate(t_array):
		t_map[v] = ind
	return t_map

def main():
	parser = argparse.ArgumentParser(description="prepare.annot.py", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	parser.add_argument("-p", "--projection", dest="file_projection", type=str, required=False)
	parser.add_argument("-c", "--cluster", dest="file_clusters", type=str, required=False)
	parser.add_argument("-n", "--cluster-name", dest="cluster_name", type=str, required=False)
	parser.add_argument("-b", "--barcode-order", dest="file_barcode_order", type=str, required = True)
	parser.add_argument("-l", "--position", dest="file_position", type=str, required=False)
	parser.add_argument("-o", "--output", dest="output_dir", type=str, required=True)

	args = parser.parse_args()

	#col_order = read_column_order("filtered_feature_bc_matrix/filtered.barcodes.txt")
	col_order = read_column_order(args.file_barcode_order)

	if args.file_projection is not None:
		#t_col_names, tsne_coord = read_tsne("analysis/tsne/2_components/projection.csv")
		t_col_names, tsne_coord = read_tsne(args.file_projection)
		map_tsne = get_map(t_col_names)
		good_ids = []
		for cell in col_order:
			good_ids.append(map_tsne[cell])
		good_ids = np.array(good_ids)
		tsne_coord = tsne_coord[good_ids,:]

		#scale tSNE coordinates
		minX, minY = np.min(tsne_coord[:,0]), np.min(tsne_coord[:,1])
		maxX, maxY = np.max(tsne_coord[:,0]), np.max(tsne_coord[:,1])
		rangeX = maxX - minX
		rangeY = maxY - minY
		unitX = rangeX / 40.0
		unitY = rangeY / 40.0
	
		for i in range(tsne_coord.shape[0]):
			newX = (tsne_coord[i,0] - minX) / unitX + (-20.0)
			newY = (tsne_coord[i,1] - minY) / unitY + (-20.0)
			tsne_coord[i,:] = [newX, newY]

		fw = open("%s/tsne_coord.txt" % args.output_dir, "w")
		for i in range(tsne_coord.shape[0]):
			fw.write("%.2f %.2f\n" % (tsne_coord[i,0], tsne_coord[i,1]))
		fw.close()


	if args.file_clusters is not None:
		if args.cluster_name is None:
			sys.stderr.write("Error: requires --cluster-name\n") 
			sys.exit(0)
		#c_col_names, clust = read_cluster("analysis/clustering/kmeans_10_clusters/clusters.csv")
		c_col_names, clust = read_cluster(args.file_clusters)
		map_clust = get_map(c_col_names)
		good_ids = []
		for cell in col_order:
			good_ids.append(map_clust[cell])
		good_ids = np.array(good_ids)
		clust = clust[good_ids]

		fw = open("%s/%s.txt" % (args.output_dir, args.cluster_name), "w")
		for i in range(clust.shape[0]):
			fw.write("%d\n" % clust[i])
		fw.close()
		t_uniq = np.unique(clust)
		fw = open("%s/%s.annot" % (args.output_dir, args.cluster_name), "w")
		for tu in t_uniq:
			fw.write("%d\tC%d\n" % (tu, tu))
		fw.close()
	
	if args.file_position is not None:
		#p_col_names, physical_coord = read_physical("spatial/tissue_positions_list.csv")	
		p_col_names, physical_coord = read_physical(args.file_position)	
		
		map_physical = get_map(p_col_names)

		good_ids = []
		for cell in col_order:
			good_ids.append(map_physical[cell])
		good_ids = np.array(good_ids)
		physical_coord = physical_coord[good_ids,:]

		fw = open("%s/physical_coord.txt" % args.output_dir, "w")
		for i in range(physical_coord.shape[0]):
			fw.write("%.2f %.2f\n" % (physical_coord[i,0], physical_coord[i,1]))
		fw.close()

if __name__=="__main__":
	main()	
