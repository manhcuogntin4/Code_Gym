def sound(s):
	words=s.split()
	sounds=[]
	for word in words:
		s=0
		for i in range(len(word)):
			for j in range(i+1,len(word)):
				if word[j]==word[i]:
					s+=1
				else:
					break
		if s>=2:
			sounds.append(word)
	return sounds
s="Well, sheep says beeeeee and cat says miaaaaaaaaaaaaw - and a cow would shout moooooooooow"
print(sound(s))