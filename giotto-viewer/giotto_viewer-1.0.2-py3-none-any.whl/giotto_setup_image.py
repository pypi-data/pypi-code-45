import sys
import os
import numpy as np
import scipy
import argparse
import json
import jsbeautifier

def main():
	parser = argparse.ArgumentParser(description="giotto_setup_image.py", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	parser.add_argument("--require-stitch", dest="to_stitch", choices=["y", "n"], default="n", required=True)
	parser.add_argument("--image", dest="has_image", choices=["y", "n"], default="n", required=True)
	parser.add_argument("--image-multi-channel", dest="has_image_multi_channel", choices=["y", "n"], default="n", required=True)
	parser.add_argument("--segmentation", dest="has_segmentation", choices=["y", "n"], default="n", required=True)
	parser.add_argument("--multi-fov", dest="has_multi_fov", choices=["y", "n"], default="n", required=True)
	parser.add_argument("--output-json", dest="output", type=str, required=True)

	args = parser.parse_args()

	config = {}
	config["tiff_width"] = 4028
	config["tiff_height"] = 4028
	config["positions"] = [0]
	if args.has_multi_fov=="y":
		config["positions"] = [0, 1, 2, 3, 4]

	config["stain_ids"] = [0]
	if args.has_image_multi_channel=="y":
		config["stain_ids"] = [0, 1, 2, 3, 4]
	
	actions = []
	if args.has_image=="y":
		actions.append("decouple_tiff")
	
	if args.has_segmentation=="y":
		actions.append("extract_roi_zip")
		
	if args.to_stitch=="y":
		actions.append("stitch_image")
		actions.append("stitch_coord")
		if args.has_segmentation=="y":
			actions.append("stitch_segmentation_roi")
	
	if args.has_segmentation=="y":
		actions.append("align_segmentation_and_cell_centroid")
	
	if args.has_image=="y":
		actions.append("tiling_image")
	
	actions.append("prepare_gene_expression")

	a_map = {}

	sys.stdout.write("=====================\nExtra messages for the output JSON file:\n=====================\n")
	if args.has_image=="y":
		sys.stdout.write("Check that \"tiff_width\" and \"tiff_height\" are correct\n")
	if args.has_multi_fov=="y":
		sys.stdout.write("Check that \"positions\" are correct\n")
	if args.has_image_multi_channel=="y":
		sys.stdout.write("Check that \"stain_ids\" are correct\n")

	for ind,ac in enumerate(actions):
		if ac=="decouple_tiff":
			n_key = "new_task_%d" % (ind+1)
			config.setdefault(n_key, {})
			config[n_key]["task"] = ac
			config[n_key]["priority"] = ind+1
			a_map[ac] = n_key
			if args.has_multi_fov=="y":
				config[n_key]["input"] = "extent_[POSITION]_V1_Adult_Mouse_Brain_image.tif"
				config[n_key]["output_prefix"] = "pos[POSITION]"
			else:
				config[n_key]["input"] = "extent_V1_Adult_Mouse_Brain_image.tif"
				config[n_key]["output_prefix"] = "pos"
			config[n_key]["positions"] = config["positions"]
			sys.stdout.write("Section \"decouple_tiff\", check that \"input\" is correct\n")		
		elif ac=="extract_roi_zip":
			n_key = "new_task_%d" % (ind+1)
			config.setdefault(n_key, {})
			config[n_key]["task"] = ac
			config[n_key]["priority"] = ind+1
			a_map[ac] = n_key
			if args.has_multi_fov=="y":
				config[n_key]["input"] = "RoiSet_Pos[POSITION]_real.zip"
				config[n_key]["output"] = "roi/roi.pos[POSITION].all.txt"
				config[n_key]["tmp"] = "/tmp/pos[POSITION]"
			else:
				config[n_key]["input"] = "RoiSet_real.zip"
				config[n_key]["output"] = "roi/roi.all.txt"
				config[n_key]["tmp"] = "/tmp/pos"
			config[n_key]["positions"] = config["positions"]
			sys.stdout.write("Section \"extract_roi_zip\", check that \"input\" is correct\n")		
	
		elif ac=="stitch_image":
			n_key = "new_task_%d" % (ind+1)
			config.setdefault(n_key, {})
			config[n_key]["task"] = ac
			config[n_key]["priority"] = ind+1
			a_map[ac] = n_key
			#by definition has to be multiple fov
			if args.has_multi_fov=="n":
				sys.stderr.write("Error: has_multi_fov is set to n. Should be y.\n")
				sys.exit(0)
			#if args.has_image_multi_channel=="y":
			if "decouple_tiff" in a_map:
				config[n_key]["input"] = config[a_map["decouple_tiff"]]["output_prefix"] + "." + "[STAINID].tif"
			else:
				config[n_key]["input"] = "generic.Pos[POSITION].[STAINID].tif"
				sys.stdout.write("Warning: section \"stitch_image\", using generic value for \"input\".\n")
			config[n_key]["output"] = "pos[STAINID].joined.tif"
			#else:
			#	config[n_key]["input"] = "Pos[POSITION].tif"
			#	config[n_key]["output"] = "pos.joined.tif"
			config[n_key]["offset"] = "offset.txt"
			config[n_key]["positions"] = config["positions"]
			config[n_key]["stain_ids"] = config["stain_ids"]
			
		elif ac=="stitch_coord":
			n_key = "new_task_%d" % (ind+1)
			config.setdefault(n_key, {})
			config[n_key]["task"] = ac
			config[n_key]["priority"] = ind+1
			a_map[ac] = n_key
			config[n_key]["input"] = "Cell_centroids.csv"
			config[n_key]["output"] = "cell.centroid.stitched.pos.all.cells.txt"
			config[n_key]["offset"] = "offset.txt"
			config[n_key]["positions"] = config["positions"]
			sys.stdout.write("Section \"stitch_coord\", check that \"input\" is correct\n")
			
		elif ac=="stitch_segmentation_roi":
			n_key = "new_task_%d" % (ind+1)
			config.setdefault(n_key, {})
			config[n_key]["task"] = ac
			config[n_key]["priority"] = ind+1
			a_map[ac] = n_key
			if args.has_multi_fov=="n":
				sys.stderr.write("Error: has_multi_fov is set to n. Should be y.\n")
				sys.exit(0)
			if "extract_roi_zip" in a_map:
				config[n_key]["input"] = config[a_map["extract_roi_zip"]]["output"]
			else:
				config[n_key]["input"] = "generic.roi.pos[POSITION].all.txt"
				sys.stdout.write("Warning: section \"stitch_coord\", using generic value for \"input\".\n")

			config[n_key]["output"] = "roi.stitched.pos.all.cells.txt"
			config[n_key]["offset"] = "offset.txt"
			config[n_key]["positions"] = config["positions"]
		
		elif ac=="align_segmentation_and_cell_centroid":
			n_key = "new_task_%d" % (ind+1)
			config.setdefault(n_key, {})
			config[n_key]["task"] = ac
			config[n_key]["priority"] = ind+1
			a_map[ac] = n_key
			if "stitch_coord" in a_map:
				config[n_key]["input_cell_centroid"] = config[a_map["stitch_coord"]]["output"]
			else:
				config[n_key]["input_cell_centroid"] = "generic_cell_centroid_file.txt"
				sys.stdout.write("Warning: section \"align_segmentation_and_cell_centroid\", using generic value for \"input_cell_centroid\".\n")
			if "stitch_segmentation_roi" in a_map:
				config[n_key]["input_segmentation"] = config[a_map["stitch_segmentation_roi"]]["output"]
			elif "extract_roi_zip" in a_map:
				config[n_key]["input_segmentation"] = config[a_map["extract_roi_zip"]]["output"]
			else:
				config[n_key]["input_segmentation"] = "generic_cell_segmentation_roi_file.txt"
				sys.stdout.write("Warning: section \"align_segmentation_and_cell_centroid\", using generic value for \"input_segmentation\".\n")
			config[n_key]["output"] = "segmentation.to.cell.centroid.map.txt"

		elif ac=="tiling_image":
			n_key = "new_task_%d" % (ind+1)
			config.setdefault(n_key, {})
			config[n_key]["task"] = ac
			config[n_key]["priority"] = ind+1
			a_map[ac] = n_key
			if args.has_image_multi_channel=="y":
				config[n_key]["input"] = "Pos.ch[STAINID].joined.tif"
				config[n_key]["output_dir"] = "tiles.[STAINID]"
			else:
				if "stitch_image" in a_map: #multi-fov
					config[n_key]["input"] = config[a_map["stitch_image"]]["output"]
				elif "decouple_tiff" in a_map: #single-fov, but single image
					config[n_key]["input"] = config[a_map["decouple_tiff"]]["output_prefix"] + "." + "[STAINID].tif"
				else:
					config[n_key]["input"] = "generic_Pos.tif"
					sys.stdout.write("Warning: section \"tiling_image\", using generic value for \"input\".\n")
				config[n_key]["output_dir"] = "tiles.[STAINID]"
			config[n_key]["zoom"] = 6
			config[n_key]["stain_ids"] = config["stain_ids"]

		elif ac=="prepare_gene_expression":
			n_key = "new_task_%d" % (ind+1)
			config.setdefault(n_key, {})
			config[n_key]["task"] = ac
			config[n_key]["priority"] = ind+1
			a_map[ac] = n_key
			config[n_key]["input"] = "giotto_expression.csv"
			config[n_key]["output_dir"] = "all.genes"
			config[n_key]["csv_sep"] = ","
			config[n_key]["csv_header"] = 0
			config[n_key]["csv_index_col"] = 0
			config[n_key]["num_genes_per_file"] = 100
			sys.stdout.write("Section \"prepare_gene_expression\", check that \"input\" is correct\n")

	#opts = jsbeautifier.default_options()
	#opts.indent_with_tabs = True	
	fw = open(args.output, "w")
	fw.write(jsbeautifier.beautify(json.dumps(config)))
	fw.close()

if __name__=="__main__":
	main()	
