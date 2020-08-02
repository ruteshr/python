n=5
for i in range(n):
  for j in range(n-i-1):
    print(end=" ")
  for j in range(2*i+1):
    print("*",end="")
  print()
  '''
  OUTPUT:
    *
   ***   
  *****  
 ******* 
*********
  '''
#-----------------------------------------
n=5
for i in range(n):
  for j in range(n-i-1):
    print(end=" ")
  for j in range(2*i+1):
    print(j+1,end="")
  print()
  '''
  OUTPUT:
    1    
   123   
  12345  
 1234567 
123456789
  '''
#-----------------------------------------
n=5
for i in range(n):
  for j in range(n-i-1):
    print(end=" ")
  for j in range(2*i+1):
    print(i+1,end="")
  print()
'''
  OUTPUT:
    1
   222
  33333
 4444444
555555555
'''
#-----------------------------------------
n=5
for i in range(n):
  for j in range(n-i-1):
    print(end=" ")
  for j in range(2*i+1,0,-1):
    print(j,end="")
  print()
'''
  OUTPUT:
    1
   321
  54321
 7654321
987654321
'''
#-----------------------------------------
n=5
for i in range(n):
  for j in range(n-i-1):
    print(end=" ")
  for j in range(i+1):
    print(j+1,end="")
  for j in range(i,0,-1):
    print(j,end="")
  print()
'''
  OUTPUT:
    1
   321
  54321
 7654321
987654321
'''
#-----------------------------------------
n=5
for i in range(n):
  for j in range(n-i-1):
    print(end=" ")
  for j in range(i+1,0,-1):
    print(j,end="")
  for j in range(2,i+2,1):
    print(j,end="")
  print()
'''
OUTPUT:
    1
   212
  32123
 4321234
543212345
'''
