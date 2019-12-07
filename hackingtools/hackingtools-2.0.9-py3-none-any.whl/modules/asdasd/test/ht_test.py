from hackingtools.core import Logger, Utils, Config
if Utils.amIdjango(__name__):
	from hackingtools.core import hackingtools as ht
else:
	import hackingtools as ht
import os

config = Config.getConfig(parentKey='modules', key='ht_test')
output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'output'))

class StartModule():

	def __init__(self):
		pass

	def help(self):
		Logger.printMessage(message=ht.getFunctionsNamesFromModule('ht_test'), debug_module=True)

	def hola(self, aa, name, fileName=None, edad=10):
		return name

	def liwiskas(self, asddas, sadasd, fileNaeeme=None, edasdad=10):
		return edasdad

	def mimimi(self, a, asdasd='', edasdad=10):
		return edasdad