class Stack:
	def __init__(self):
		# Initialise the stack's data attributes
		self.items=[]
	
	def push(self, item):
		# Push an item to the stack
		self.items.append(item)

	def peek(self):
		# Return the element at the top of the stack
		# Return a string "Error" if stack is empty
		if(len(self.items)!=0):
			return self.items[-1]
		return "Error"

	def pop(self):
		# Pop an item from the stack if non-empty
		if(len(self.items)!=0):
			item=self.items[-1]
			del self.items[-1]
			return item
		return None

	def is_empty(self):
		# Return True if stack is empty, False otherwise
		return len(self.items) == 0

	def __str__(self):
		# Return a string containing elements of current stack in top-to-bottom order, separated by spaces
		# Example, if we push "2" and then "3" to the stack (and don't pop any elements), 
		# then the string returned should be "3 2"
		return " ".join(map(str, reversed(self.items)))

	def __len__(self):
		# Return current number of elements in the stack
		return len(self.items)

