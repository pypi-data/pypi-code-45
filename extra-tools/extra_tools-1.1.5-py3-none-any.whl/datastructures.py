class StackError(Exception):
	pass

class Stack:
	def __init__(self,size):
		self.stack = []
		self._index = len(self.stack)
		self.size = size
	def push(self,element):
		if self._index == self.size:
			raise StackError("Stack Overflow!")
		else:
			self.stack.append(element)
			self._index = len(self.stack)
			return None
	def pop(self):
		if self._index == 0:
			raise StackError("Stack Underflow!")
		else:
			val = self.stack.pop()
			self._index = len(self.stack)
			return val

