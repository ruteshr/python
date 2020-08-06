n=5
a=3
for i in range(n):
    for j in range(i+1):
        print(a,end="")
    a=a+1
    print()
a-=2
for i in range(1,n):
    for j in range(n-i):
        print(a,end="")
    a-=1
    print()
'''
OUTPUT:
3
44
555
6666
77777
6666
555
44
3
'''
#=========================================
n=5
a=3
for i in range(n):
    for j in range(i+1):
        print(j+1,end="")
    print()
for i in range(1,n):
    for j in range(n-i):
        print(j+1,end="")
    print()
'''
OUTPUT:
1
12
123
1234
12345
1234
123
12
1
'''
#=========================================
n=5
a=3
for i in range(n):
    for j in range(i+1):
        p=j+1
    for j in range(i+1):
        print(p,end="")
        p-=1
    print()
for i in range(1,n):
    for j in range(n-i):
        p=j+1
    for j in range(n-i):
        print(p,end="")
        p-=1
    print()
'''
OUTPUT:
1
21
321
4321
54321
4321
321
21
1
'''
#=========================================
