n=5
for i in range(n):
  for j in range(i):
    print(end=" ")
  for j in range(2*n-(2*i+1)):
    print("*",end="")
  print()
'''
OUTPUT:
*********
 *******
  *****
   ***
    *
'''
#=======================================
n=5
for i in range(n):
  for j in range(i):
    print(end=" ")
  for j in range(2*n-(2*i+1)):
    print(j+1,end="")
  print()
'''
OUTPUT:
123456789
 1234567
  12345
   123
    1
'''
#=======================================
n=5
for i in range(n):
  for j in range(i):
    print(end=" ")
  for j in range(2*n-(2*i+1)):
    print(i+1,end="")
  print()
'''
OUTPUT
111111111
 2222222
  33333
   444
    5
'''
#=======================================
n=5
for i in range(n):
  for j in range(i):
    print(end=" ")
  for j in range(2*n-(2*i+1)):
    print(n-i,end="")
  print()
'''
OUTPUT:
555555555
 4444444
  33333
   222
    1
'''
#=======================================
n=5
for i in range(n):
  for j in range(i):
    print(end=" ")
  for j in range(n-i):
    print(j+1,end="")
  for j in range(n-i-1,0,-1):
    print(j,end="")
  print()
'''
OUTPUT:
123454321
 1234321
  12321
   121
    1
'''
#=======================================
n=5
for i in range(n):
  for j in range(i):
    print(end=" ")
  for j in range(n-i,0,-1):
    print(j,end="")
  for j in range(2,n-i+1):
    print(j,end="")
  print()
'''
OUTPUT:
543212345
 4321234
  32123
   212
    1
'''
