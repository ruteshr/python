n=5
for i in range(n):
  for j in range(n-i-1):
    print(end=" ")
  for j in range(2*i+1):
    print("*",end="")
  print()
for i in range(1,n):#for i in range(n)-->for 10 line
  for j in range(i):
    print(end=" ")
  for j in range(2*n-(2*i+1)):
    print("*",end="")
  print()
'''
OUTPUT:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
#============================================
n=5
for i in range(n):
  for j in range(n-i-1):
    print(end=" ")
  for j in range(2*i+1):
    print(j+1,end="")
  print()
for i in range(1,n):
  for j in range(i):
    print(end=" ")
  for j in range(2*n-(2*i+1)):
    print(j+1,end="")
  print()
'''
OUTPUT:
    1
   123
  12345
 1234567
123456789
 1234567
  12345
   123
    1
'''
#============================================
n=5
for i in range(n):
  for j in range(n-i-1):
    print(end=" ")
  for j in range(2*i+1):
    print(i+1,end="")
  print()
for i in range(1,n):
  for j in range(i):
    print(end=" ")
  for j in range(2*n-(2*i+1)):
    print(n-i,end="")
  print()
'''
OUTPUT:
    1
   222
  33333
 4444444
555555555
 4444444
  33333
   222
    1
'''
#================================================
n, m = map(int,input().split())
for i in range(n//2):
    for j in range(1, (n-1),2):
        txt='.|.'*j 
        print(txt.center(m,"-"))
    break
w="WELCOME"
print(w.center(m,"-"))
for i in range(n//2):
    for j in range(n-2,0,-2):
        txt='.|.'*j 
        print(txt.center(m,"-"))
    break
'''
INPUT:
  7 21
OUTPUT:
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
'''
#=============================================
n=5
a=n
if(n==1):
    print('a')
else:
    for i in range(n):
        for j in range(2*n-(2*i)-2):
            print(end="-")
        for j in range(i+1):
            print(chr(96+a-j),end="-")
        for j in range(i):
            if((96+n+1-i+j==96+n) and (j==n-2)):
                print(chr(96+n+1-i+j),end="")
            else:
                print(chr(96+n+1-i+j),end="-")
        for j in range(2*n-(2*i)-2-1):
            print(end="-")
        print()
    for i in range(n-1):
        for j in range(2+2*i):
            print(end="-")
        for j in range(n-i-1):
            print(chr(96+n-j),end="-")
        for j in range(n-2-i):
            print(chr(97+2+j+i),end="-")
        for j in range(2*i+1):
            print(end="-")
        print()
 '''
 OUTPUT:
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

''''
#===========================================
