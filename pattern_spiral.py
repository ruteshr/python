n=5
list=[[0 for x in range(n)] for y in range(n)]
a=1
high=n-1
low=0
count=int((n+1)/2)

for i in range(count):
    for j in range(low,high+1):
        list[low][j]=a
        a+=1
    for j in range(low+1,high+1):
        list[j][high]=a
        a+=1
    for j in range(high-1,low-1,-1):
        list[high][j]=a
        a+=1
    for j in range(high-1,low,-1):
        list[j][low]=a
        a+=1
    low+=1
    high-=1
for i in range(n):
    for j in range(n):
        print(list[i][j],end="\t")
    print()
'''
OUTPUT:
1       2       3       4       5
16      17      18      19      6
15      24      25      20      7
14      23      22      21      8
13      12      11      10      9
'''
#=======================================================

n=5
low=0
a=1
high=n-1
count=int((n+1)/2)
list=[[0 for x in range(n)]for y in range(n)]
for i in range(count):
    for j in range(low,high+1):
        list[j][low]=a
        a+=1
    for j in range(low+1,high+1):
        list[high][j]=a
        a+=1
    for j in range(high-1,low-1,-1):
        list[j][high]=a
        a+=1
    for j in range(high-1,low,-1):
        list[low][j]=a
        a+=1
    low+=1
    high-=1
for i in range(n):
    for j in range(n):
        print(list[i][j],end="\t")
    print()
'''
OUTPUT:
1       16      15      14      13
2       17      24      23      12
3       18      25      22      11
4       19      20      21      10
5       6       7       8       9
'''
#=======================================================
n=5
list=[[0 for x in range(2*n-1)]for y in range(2*n-1)]
a=n
low=0
high=2*n-2
for i in range(2*n-1):
    for j in range(low,high+1):
        list[low][j]=a
    for j in range(low+1,high+1):
        list[j][high]=a
    for j in range(high-1,low-1,-1):
        list[high][j]=a
    for j in range(high-1,low,-1):
        list[j][low]=a
    low+=1
    high-=1
    a-=1
for i in range(2*n-1):
    for j in range(2*n-1):
        print(list[i][j],end=" ")
    print()
'''
OUTPUT:
5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
'''
#=======================================================

n=5
list=[[0 for x in range(2*n-1)]for y in range(2*n-1)]
a=1
low=0
high=2*n-2
for i in range(2*n-1):
    for j in range(low,high+1):
        list[low][j]=a
    for j in range(low+1,high+1):
        list[j][high]=a
    for j in range(high-1,low-1,-1):
        list[high][j]=a
    for j in range(high-1,low,-1):
        list[j][low]=a
    low+=1
    high-=1
    if(a<n):
        a+=1
for i in range(2*n-1):
    for j in range(2*n-1):
        print(list[i][j],end=" ")
    print()
'''
OUTPUT:
1 1 1 1 1 1 1 1 1
1 2 2 2 2 2 2 2 1
1 2 3 3 3 3 3 2 1
1 2 3 4 4 4 3 2 1
1 2 3 4 5 4 3 2 1
1 2 3 4 4 4 3 2 1
1 2 3 3 3 3 3 2 1
1 2 2 2 2 2 2 2 1
1 1 1 1 1 1 1 1 1
'''
