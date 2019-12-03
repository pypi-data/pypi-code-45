class WriteProxy(object):
	"""
	Keeps track of updates to an underlying data structure.

	The intended use case is that a larger structure
	(e.g. M2MGraph) can hand out some internal sub-structure
	(e.g. M2M) and allow the caller to modify that sub-structure
	while still keeping the main data structure in sync.
	"""
	__slots__ = ('_data', '_listeners')

	def __init__(self, data):
		self._data = data

	def sub(self):
		pass
