def split_poem( poem ):
	return poem . split ('\n')
def reverse_line( st ):
	s =""
	for i , c in enumerate( st ):
		s += st [len( st )- i -1]
	return s
def reverse_poem(poem):
# Your code goes here
	lines = split_poem ( poem )
	#print(lines[n-1])
	result=[]
	for line in lines:
		s= reverse_line(line)
		result.append(s)
	return result
s=""" Hoo

Hoo 

Hi

Cuong
"""
s=reverse_poem(s)
for i in s:
	print i