def ft(n):
	if n==1:
		return 1
	else:
		return n*ft(n-1)
n=3
print ft(n)


def ft2(n):
	s=1
	for i in range(1,n+1):
		s=s*i
	return s
print ft2(n)