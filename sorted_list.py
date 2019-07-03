class SortedList:
	def __init__(self,l):
		self.l=sorted(l) if l else []
	def add(self,item):
		self.l.append(item)
		self.l=sorted(self.l)
	def concat(self,s2):
		self.l.extend(s2.l)
		self.l=sorted(self.l)
	def print_list(self):
		print(self.l)

s=SortedList([3,2,5])
s.print_list()
s.add(4)
s.print_list()
s2=SortedList([1,3])
s.concat(s2)
s.print_list()