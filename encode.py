st = "aaabbaccd"

index = 0
c=st[index]
count = 1
list_character=[]
while index< len(st)-1:
	if st[index+1]==c :
		count += 1
	else:
		list_character.append((count, c))
		c = st[index+1]
		count = 1
	index+=1
list_character.append((count, c))
result=""
for count, c in list_character:
	result+=str(count)+c

print(result)




