n=5
for i in range(n):
  for j in range(i+1):
    print("*",end="")
  print()
'''
OUTPUT:
*
**
***
****
*****
'''
n=5
for i in range(n):
  for j in range(i+1):
    print(j,end="")
  print()
'''
OUTPUT:
0
01
012
0123
01234
'''
n=5
for i in range(n):
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
n=5
for i in range(1,n+1):
  for j in range(i):
    print(i,end="")
  print()
'''
OUTPUT:
1
22
333
4444
55555
'''
n=5
for i in range(n):
  for j in range(i+1):
    print(n-i,end="")
  print()
  '''
OUTPUT:
5
44
333
2222
11111
'''
