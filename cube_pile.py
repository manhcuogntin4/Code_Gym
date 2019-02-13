'''There is a horizontal row of cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if is on top of then

.

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.

Input Format

The first line contains a single integer
, the number of test cases.
For each test case, there are lines.
The first line of each test case contains , the number of cubes.
The second line contains

space separated integers, denoting the sideLengths of each cube in that order.

Constraints


Output Format

For each test case, output a single line containing either "Yes" or "No" without the quotes.

Sample Input

2
6
4 3 2 1 3 4
3
1 3 2

Sample Output

Yes
No

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
def stack_able(l):
    i=0
    j=len(l)-1
    max_temp=max(l[i],l[j])
    while i<=j and i<len(l) and j>0:
        if i==j:
            if l[i]<=max_temp:
                return True
        if l[i]>=l[j]:
            if l[i]<=max_temp:
                max_temp=l[i]
                i+=1
            else:
                return False
        else:
            if l[j]<=max_temp:
                max_temp=l[j]
                j-=1
            else:
                return False

    return True


import sys
data = sys.stdin.readlines()
m=int(data[0].strip())
for i in range(0,m):
    l=list(map(int,data[(i+1)*2].strip().split(" ")))
    #print(l) 
    if stack_able(l):
        print("Yes")
    else:
        print("No")