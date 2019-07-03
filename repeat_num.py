def repeat_num(s,pat):
	i=s.find(pat)
	cnt=0
	while i>=0:
		s=s[i+len(pat):]
		print s
		cnt+=1
		i=s.find(pat)
	return cnt

s="hhhhhh"
pat="hh"
print repeat_num(s,pat)
print s.find(pat)