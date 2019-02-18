'''
Your task is to sort the string

in the following manner:

    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.

'''
def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)
def sort_array(a):
    a_temp=a.copy()
    for i in range(len(a_temp)):
        for j in range(i+1, len(a_temp)):
            if a_temp[i][1]>a_temp[j][1]:
                temp=a_temp[i]
                a_temp[i]=a_temp[j]
                a_temp[j]=temp
    return a_temp
def print_array(a):
    for i in a:
        print(i[0],end="")


s=input()
l=0
d={}
for i in char_range('a','z'):
    d[i]=l
    l+=1
for i in char_range('A','Z'):
    d[i]=l
    l+=1
for i in ('1','3','5','7','9'):
    d[i]=l
    l+=1
for i in ('0','2','4','6','8'):
    d[i]=l
    l+=1
a=[]
for i in s:
    if i in d:
        a.append((i,d[i]))
d=sort_array(a)
print_array(d)


'''
myList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"
print(*sorted(input(), key=lambda x: myList.index(x)), sep ="")
'''