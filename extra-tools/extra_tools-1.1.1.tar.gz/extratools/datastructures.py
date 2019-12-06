class StackError(Exception):
	pass

class Stack:
	def __init__(self,size):
		self.stack = []
		self.index = 0
		self.size = size
	def push(self,element):
		if self.index == size:
			raise StackError("Stack Overflow!")
		else:
			self.stack.append(element)
			self.index += 1
			return "Pushed!"
	def pop(self):
		if self.index == 0:
			raise StackError("Stack Underflow!")
		else:
			self.size -= 1
			return self.stack.pop()

