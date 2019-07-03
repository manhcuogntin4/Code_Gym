class Node:
	def __init__(self,n):
		self.value=n
		self.left=None
		self.right=None
	def add(self,n):
		if self.value==None:
			self.value=n
		else:
			if self.value>n:
				if self.left is None:
					self.left=Node(n)
				else:
					self.left.add(n)
			else:
				if self.right is None:
					self.right=Node(n)
				else:
					self.right.add(n)
	def find(self,n):
		if self.value is None:
			return False
		if self.value:
			if self.value==n:
				return True
			else:
				if self.value<n:
					if self.right is None:
						return False
					else:
						return self.right.find(n)
				else:
					if self.left is None:
						return False
					else:
						return self.left.find(n)
root=Node(5)
root.add(3)
root.add(7)
print(root.find(3))
print(root.find(4))


