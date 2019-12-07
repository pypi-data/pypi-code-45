import sys
import os
import numpy as np
import scipy
import argparse
import json
import jsbeautifier

def main():
	parser = argparse.ArgumentParser(description="giotto_setup_viewer.py", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	parser.add_argument("--num-panel", dest="num_panel", choices=["2", "4", "6", "8"], default="2", required=True)
	parser.add_argument("--input-preprocess-json", dest="file_preprocess", type=str, required=True)
	parser.add_argument("--input-annotation-list", dest="annot_list", type=str, required=False)
	parser.add_argument("--output-json", dest="output", type=str, required=True)
	parser.add_argument("--panel-1", dest="panel_1", choices=["PanelPhysical", "PanelTsne", "PanelPhysicalSimple", "PanelPhysical10X"], default="PanelPhysical", required=True)
	parser.add_argument("--panel-2", dest="panel_2", choices=["PanelPhysical", "PanelTsne", "PanelPhysicalSimple", "PanelPhysical10X"], default="PanelTsne", required=True)
	parser.add_argument("--panel-3", dest="panel_3", choices=["PanelPhysical", "PanelTsne", "PanelPhysicalSimple", "PanelPhysical10X"], default="PanelPhysical", required=False)
	parser.add_argument("--panel-4", dest="panel_4", choices=["PanelPhysical", "PanelTsne", "PanelPhysicalSimple", "PanelPhysical10X"], default="PanelTsne", required=False)
	parser.add_argument("otherpanels", nargs="*")

	args = parser.parse_args()

	f = open(args.file_preprocess)
	preprocess_json = json.load(f)
	f.close()

	ac = {}
	for k in preprocess_json:
		if k.startswith("new_task_"):
			ac[preprocess_json[k]["task"]] = k


	config = {}
	config["num_panel"] = int(args.num_panel)
	if config["num_panel"]==2:
		config["orientation"] = "horizontal"

	config.setdefault("annotation_set", {})
	if args.annot_list is not None:
		f = open(args.annot_list)
		annot = []
		for l in f:
			l = l.rstrip("\n")
			ll = l.split(" ")
			annot.append((ll[0], ll[1]))
		f.close()
		config["annotation_set"]["num_annot"] = len(annot)
		for ind,(i,j) in enumerate(annot):
			n_key = "annot_%d" % (ind+1)
			config["annotation_set"].setdefault(n_key, {})
			config["annotation_set"][n_key]["file"] = i
			config["annotation_set"][n_key]["name"] = j
	else:		
		config["annotation_set"]["num_annot"] = 1
		config["annotation_set"]["annot_1"] = {"file": "generic.annot.file.txt", "name": "generic.name"}
		sys.stdout.write("Warning: section \"annotation_set\", using generic annotation file names, because --input-annotation-list not specified.\n")

	is_multi_fov = True
	is_multi_channel = True
	if len(preprocess_json["positions"])==1:
		is_multi_fov = False
	if len(preprocess_json["stain_ids"])==1:
		is_multi_channel = False

	default_annot = config["annotation_set"]["annot_1"]["name"]

	default_height = "500px"
	if config["num_panel"]==2 and config["orientation"]=="vertical":
		default_height = "500px"
	elif config["num_panel"]==2 and config["orientation"]=="horizontal":
		default_height = "1000px"
	elif config["num_panel"]==4:
		default_height = "500px"

	for m in range(1, config["num_panel"] + 1):
		n_key = "map_%d" % m
		config.setdefault(n_key, {})
		if m==1:
			config[n_key]["type"] = args.panel_1
		elif m==2:
			config[n_key]["type"] = args.panel_2
		elif m==3:
			config[n_key]["type"] = args.panel_3
		elif m==4:
			config[n_key]["type"] = args.panel_4

		if config[n_key]["type"]=="PanelPhysical":
			config[n_key]["maxBound"] = preprocess_json["tiff_width"]
			config[n_key]["id"] = m
			#=====================================================
			config[n_key]["annot"] = default_annot
			config[n_key]["gene_list"] = "giotto_gene_ids.txt"
			#=====================================================
			config[n_key]["tile"] = "nissl"
			pp = ["dir_polyA", "dir_nissl", "dir_dapi", "dir_other1", "dir_other2", "dir_other3"]
			stains = preprocess_json[ac["tiling_image"]]["stain_ids"]
			for ind,st in enumerate(stains):
				field = pp[ind]
				name = preprocess_json[ac["tiling_image"]]["output_dir"].replace("[STAINID]", "%d" % st)
				config[n_key][field] = name
			config[n_key]["gene_map"] = preprocess_json[ac["prepare_gene_expression"]]["output_dir"] + "/" + "gene.map"

			if ac["stitch_segmentation_roi"] in preprocess_json or ac["extract_roi_zip"] in preprocess_json:
				if is_multi_fov:
					config[n_key]["segmentation"] = preprocess_json[ac["stitch_segmentation_roi"]]["output"]
				else:
					config[n_key]["segmentation"] = preprocess_json[ac["extract_roi_zip"]]["output"]
			else:
				sys.stdout.write("It appears that it doesn't contain segmentation information. Maybe use PanelPhysical10X instead.\n")
				sys.exit(0)

			config[n_key]["segmentation_map"] = preprocess_json[ac["align_segmentation_and_cell_centroid"]]["output"]
			config[n_key]["dir_gene_expression"] = preprocess_json[ac["prepare_gene_expression"]]["output_dir"]
			config[n_key]["map_height"] = "1000px"

		if config[n_key]["type"]=="PanelTsne":
			config[n_key]["id"] = m
			config[n_key]["maxBound"] = 500
			#=================================================
			config[n_key]["file_tsne"] = "umap_umap_dim_coord.txt"
			config[n_key]["annot"] = default_annot
			#=================================================
			config[n_key]["map_height"] = default_height
	
		if config[n_key]["type"]=="PanelPhysicalSimple":
			config[n_key]["id"] = m
			config[n_key]["maxBound"] = 2000
			#=================================================
			config[n_key]["file_simple"] = "centroid_locations.txt"
			config[n_key]["annot"] = default_annot
			#=================================================
			config[n_key]["map_height"] = default_height
		
		if config[n_key]["type"]=="PanelPhysical10X":
			config[n_key]["id"] = m
			config[n_key]["maxBound"] = preprocess_json["tiff_width"]
			#===================================================
			config[n_key]["file_simple"] = "centroid_locations.txt"
			config[n_key]["gene_list"] = "giotto_gene_ids.txt"
			config[n_key]["annot"] = default_annot
			#=================================================
			config[n_key]["gene_map"] = preprocess_json[ac["prepare_gene_expression"]]["output_dir"] + "/" + "gene.map"
			pp = ["dir_nissl", "dir_dapi", "dir_polyA", "dir_other1", "dir_other2", "dir_other3"]
			stains = preprocess_json[ac["tiling_image"]]["stain_ids"]
			for ind,st in enumerate(stains):
				field = pp[ind]
				name = preprocess_json[ac["tiling_image"]]["output_dir"].replace("[STAINID]", "%d" % st)
				config[n_key][field] = name
			config[n_key]["dir_dapi"] = config[n_key]["dir_nissl"]
			config[n_key]["dir_polyA"] = config[n_key]["dir_nissl"]
			config[n_key]["tile"] = "nissl"
			config[n_key]["dir_gene_expression"] = preprocess_json[ac["prepare_gene_expression"]]["output_dir"]
			config[n_key]["map_height"] = default_height
			
	if config["num_panel"]==2:
		config["interact_1"] = ["map_1", "map_2"]
	elif config["num_panel"]==4:
		config["interact_1"] = ["map_1", "map_2", "map_3", "map_4"]
		config["sync_1"] = ["map_1", "map_3"]
		config["sync_2"] = ["map_3", "map_4"]
	elif config["num_panel"]==6:
		config["interact_1"] = ["map_1", "map_2", "map_3", "map_4", "map_5", "map_6"]
		config["sync_1"] = ["map_1", "map_4"]
		config["sync_2"] = ["map_2", "map_5"]
		config["sync_3"] = ["map_3", "map_6"]

	fw = open(args.output, "w")
	fw.write(jsbeautifier.beautify(json.dumps(config)))
	fw.close()

if __name__=="__main__":
	main()	
