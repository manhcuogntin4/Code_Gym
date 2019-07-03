d={}
d['a']=10
d['b']=5
for x in d.items():
	print(x)


d1={}
for k,v in d.items():
	d1[v]=k
print (d1)


s="Well sheep says beeeeee and cat says miaaaaaaw"

def get_words(s):
	return s.split()
def is_sound(word):
	start,end=0,1
	for i in range(len(word)):
		if word(start)=word(end):
			 