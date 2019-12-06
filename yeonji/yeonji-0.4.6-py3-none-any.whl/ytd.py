import yaml
import os
import sys
from doreah.control import mainfunction
from . import DATA_DIR


DATA_DIR = os.path.join(DATA_DIR,"ytd")
settingsfile = os.path.join(DATA_DIR,"presets.yml")

@mainfunction({},shield=True)
def main(preset=None,url=None,new=None,path=None):
	if new is None and path is None:
		with open(settingsfile,"r") as f:
			settings = yaml.safe_load(f)

		selected = settings[preset]
		os.chdir(selected["path"])
		os.system("youtube-dl " + url)
	elif new is not None and path is not None:
		settings = {}
		assert os.path.exists(path)
		with open(settingsfile,"r") as f:
			settings = yaml.safe_load(f)

		settings[new] = {"path":path}

		with open(settingsfile,"w") as f:
			yaml.dump(settings,f)

	else:
		print("You need to specify --new and --path to create a new preset!")


def create_bash_complete():

	bc =
"""#/usr/bin/env bash
_dothis_completions()
{
	compopt +o default
	if [ ${COMP_CWORD} == 1 ]
	then
		COMPREPLY=($(compgen -W "update start restart stop import install" "${COMP_WORDS[1]}"))
	fi
	if [[ ${COMP_CWORD} == 2 && ${COMP_WORDS[1]} == "import" ]]
	then
		#COMPREPLY=($(compgen -o default -A file "${COMP_WORDS[2]}"))
		compopt -o default; COMPREPLY=()
	fi
}

complete -o default -F _dothis_completions maloja
	"""
