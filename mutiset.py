class Multiset:
	def __init__(self):
		self.a=[]
	def add(self,value):
		self.a.append(value)
	def remove(self,value):
		for i in self.a:
			if i==value:
				self.a.remove(i)
				break
	def multiplicity(self, elem):
		if elem not in self.a:
			return 0
		else:
			for i in self.a:
				count=0
				if i==elem:
					count+=1
			return count
	def display(self):
		for i in self.a:
			print(i, )

a=Multiset()
a.add(2)
a.add(3)
a.add(2)
a.add(4)
a.display()
a.remove(3)
a.display()
print(a.multiplicity(2))
print(a.multiplicity(3))