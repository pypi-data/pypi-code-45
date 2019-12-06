class StackError(Exception):
	pass

class Stack:
	def __init__(self,size):
		self.stack = []
		self.index = len(self.stack)
		self.size = size
	def push(self,element):
		if self.index == self.size:
			raise StackError("Stack Overflow!")
		else:
			self.stack.append(element)
			self.index = len(self.stack)
			return "Pushed!"
	def pop(self):
		if self.index == 0:
			raise StackError("Stack Underflow!")
		else:
			val = self.stack.pop()
			self.index = len(self.stack)
			return val

