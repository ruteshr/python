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
#------------------------------------------------
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
#------------------------------------------------
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
#------------------------------------------------
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
#------------------------------------------------
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
 #------------------------------------------------
 n=5
count=0
for i in range(n):
  for j in range(i):
    count+=1
    print(count,end=" ")
  print()
'''
OUTPUT:
1
2 3
4 5 6
7 8 9 10
'''
#===========================================================
n=5
count=0
for i in range(n):
    if(i%2==0):
        for j in range(i+1):
            count+=1
            if(i==j):
                print(count,end="")
            else:
                print(count,end="*")
    if(i%2!=0):
        for j in range(i+1):
            count+=1
        temp=count
        for j in range(i+1):
            if(i==j):
                print(temp,end="")
                temp-=1
            else:
                print(temp,end="*")
                temp-=1
    print()
'''
OUTPUT:
1
3*2
4*5*6
10*9*8*7
11*12*13*14*15
'''
