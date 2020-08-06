n=5
for i in range(n):
  for j in range(n-i-1):
    print(end=" ")
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
#-------------------------------
n=5
for i in range(n):
  for j in range(n-i-1):
    print(end=" ")
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
#-------------------------------
n=5
for i in range(n):
  for j in range(n-i-1):
    print(end=" ")
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
#-------------------------------
n=5
for i in range(n):
  for j in range(n-i-1):
    print(end=" ")
  for j in range(i+1):
    print(i+1,end="")
  print()
'''
  OUTPUT:
    1
   22
  333
 4444
55555
  '''
#-------------------------------
n=5
for i in range(n):
  for j in range(n-i-1):
    print(end=" ")
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
#-------------------------------
n=5
for i in range(n):
  for j in range(n-i-1):
    print(end=" ")
  for j in range(i+1,0,-1):
    print(j,end="")
  print()
  '''
  OUTPUT:
    1
   21
  321
 4321
54321
  '''
#=======================================
n=5
count=0
for i in range(n):
    for j in range(n-i-1):
        print(end="\t")
    for j in range(i+1):
        count=count+1
    temp=count
    for j in range(i+1):
        print(temp,end="\t")
        temp-=1
    print()
'''
OUTPUT:
                                1
                        3       2
                6       5       4
        10      9       8       7
15      14      13      12      11

'''
#===========================================================
n=5
count=0
for i in range(n):
    for j in range(n-i-1):
        print(end="\t")
    for j in range(i+1):
        count=count+1
        print(count,end="\t")
    print()
'''
OUTPUT:
                                1
                        2       3
                4       5       6
        7       8       9       10
11      12      13      14      15

'''
#===========================================================
