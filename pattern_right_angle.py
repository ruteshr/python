#right angle pattern
a=int(input("enter no. of rows"))
for i in range(a):
    for j in range (i+1):
        print("*",end="")
    print()
'''
OUTPUT:

enter no. of rows 4
*
**
***
****
'''
#--------------------------------------
a=5
for i in range(a):
  for j in range(i+1):
    print(j,end="")
  print()
'''
output:
0
01
012
0123
01234
'''
#--------------------------------------
for i in range(a):
  for j in range(1,i+2):
    print(j,end="")
  print()
'''
OUTPUT:
1
12
123
1234
12345
'''
