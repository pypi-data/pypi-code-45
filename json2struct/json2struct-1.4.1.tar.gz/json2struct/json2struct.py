import re
import copy

from pprint import pprint

from data2struct import generate_field_name

go_types_map = {
	"str":     "string",
	"bool":    "bool",
	"int":     "int",
	"float":   "float32",
}

typename_re = re.compile("\<class\s\'(.+)\'\>")


def get_items_by_type(json_data, datatype):
	items = []
	
	for k, v in json_data.items():
		if isinstance(v, datatype):
			items.append(k)
	
	return items


def get_type_name(type_):
	return typename_re.search(str(type_)).groups(0)[0]


def check_array_type(array):
	"""
	Checks an array to ensure that all entries are of the same type. 
	Otherwise, shit'll get funky with struct building. 
	"""
	zero_index_type = type(array[0])
	is_uniform_type = True

	for a in array:
		if not isinstance(a, zero_index_type):
			is_uniform_type = False

	zero_index_type = get_type_name(zero_index_type)
	
	return (is_uniform_type, zero_index_type)


def assure_uniform_object_structure(obj_array):
	"""
	Checks if all dicts in a list of dicts have the same structure (keys and types)
	"""
	all_same_keys = True
	all_same_value_types = True

	base_keys = list(obj_array[0].keys())
	base_val_types = { k: type(v) for k, v in obj_array[0].items() }

	if len(obj_array) == 1:
		pass
	else:
		for obj in obj_array[1:]:
			keys = list(obj.keys())
			val_types = { k: type(v) for k, v in obj.items() }
			all_same_keys = keys == base_keys
			all_same_value_types = all([val_types[k] == base_val_types[k] for k in keys])

	return (all_same_keys, all_same_value_types)


def make_key_type_map(json_data):
	key_type_map = {
		k: type(v) for k, v in json_data.items()
	}

	return key_type_map


def generate_struct_info(json_data, struct_name, is_array=False):
	"""
	Not sure how I wrote this sober
	"""
	struct_info = {
		"__struct_name":   struct_name,
		"__is_type_array": is_array
	}

	key_type_map = make_key_type_map(json_data)

	for k, v in key_type_map.items():
		val_type_str = get_type_name(v)

		json_item = json_data[k]

		if val_type_str in go_types_map:
			struct_info[k] = go_types_map[val_type_str]
		elif val_type_str == "dict":
			struct_info[k] = generate_struct_info(json_item, generate_field_name(k))
		elif val_type_str == "list":
			array_type_info = check_array_type(json_item)

			if array_type_info[0]:
				if array_type_info[1] == "dict":
					if all(assure_uniform_object_structure(json_item)):
						array_struct_name = f"{generate_field_name(k)}List"
						struct_info[k] = generate_struct_info(json_item[0], array_struct_name, is_array=True)
					else:
						struct_info[k] = "[]interface{}"
				else:
					zero_index_type = get_type_name(type(json_item[0]))
					zero_index_type = go_types_map[zero_index_type]
					struct_info[k] = f"[]{zero_index_type}"
			else:
				struct_info[k] = "[]interface{}"

	
	return struct_info