n=5
for i in range(n):
  for j in range(i):
    print(end=" ")
  for j in range(n-i):
    print("*",end="")
  print()
  '''
  OUTPUT:
*****
 ****
  ***
   **
    *
  '''
n=5
for i in range(n):
  for j in range(i):
    print(end=" ")
  for j in range(n-i):
    print(j+1,end="")
  print()
  '''
  OUTPUT:
12345
 1234
  123
   12
    1
  '''
n=5
for i in range(n):
  for j in range(i):
    print(end=" ")
  for j in range(n-i):
    print(n-j,end="")
  print()
  '''
  OUTPUT:
54321
 5432
  543
   54
    5
  '''
n=5
for i in range(n):
  for j in range(i):
    print(end=" ")
  for j in range(n-i):
    print(n-i,end="")
  print()
  '''
  OUTPUT:
55555
 4444
  333
   22
    1
  '''
  n=5
for i in range(n):
  for j in range(i):
    print(end=" ")
  for j in range(n-i):
    print(i+1,end="")
  print()
  '''
  OUTPUT:
11111
 2222
  333
   44
    5
  '''
