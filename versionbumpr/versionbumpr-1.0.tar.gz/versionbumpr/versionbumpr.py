import re

from typing import List


def load_file(filename: str) -> List[str]:
	""" Returns the lines of the provided setup.py. 
	"""

	with open(file_path, "r") as setup_py:
		data = setup_py.readlines()
	
	return data


def update_setup_py(lines: List[str], bump_type: str, custom_version: str) -> List[str]:
	""" Bumps the version. Eyyo. 
	"""
	# for posterity
	# params_re = re.compile("(\w+\s*=\s*[\'\"\[\{]*?[\w\d\_\.\s\'\"\:\/\@\=\[\]\{\}]*[\'\"\]\}]*(,\s*[\{\}\[\]])*\s*[\"\'\]\}]*\s*?,*?(?!\D*\s*setup))+")

	version_re = re.compile("version\s*\=\s*[\'\"]((\d*\.?)+)[\'\"]")

	for i in range(len(lines)):
		version_match = version_re.match(lines[i].strip())
		if version_match:
			ver = version_match.groups(0)[0]
			if custom_version != "":
				bumped_ver = custom_version
			else:
				bumped_ver = bump_version(ver, bump_type)
			lines[i] = lines[i].replace(ver, bumped_ver)
			break
	
	return lines


def bump(num: str) -> str:
	n = int(num) + 1

	return str(n)


def bump_minor(split_version: List[str]) -> List[str]:
	if len(split_version) == 1:
		split_version.append("1")
	else:
		split_version[1] = bump(split_version[1])
	
	return split_version


def bump_hotfix(split_version: List[str]) -> List[str]:
	if len(split_version) == 1:
		split_version += ["0", "1"]
	elif len(split_version) == 2:
		split_version.append("1")
	elif len(split_version) == 3:
		split_version[2] = bump(split_version[2])
	
	return split_version


def bump_version(old_version: str, bump_type: str) -> str:
	split_ver = old_version.split(".")

	if bump_type == "major":
		split_ver[0] = bump(split_ver[0])
	elif bump_type == "minor":
		bump_minor(split_ver)
	elif bump_type == "hotfix":
		bump_hotfix(split_ver)
	
	return ".".join(split_ver)