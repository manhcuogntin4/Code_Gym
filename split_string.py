str = "1 23 459"
n=4
s = str.split(" ")
st=""
for si in s:
	st+=si

result = ""
for i in range(int(len(st)/n)):
	result +=st[i*n:(i+1)*n]+"\\n"

if len(st)%n==0:
	result = result[:-2]
else:
	result += st[int(len(st)/n)*n:]

print(result)
