#it will capitilize the first letter if it is alphabet
def solve(s):
    a=s.split()
    for x in a:
        s = s.replace(x, x.capitalize())
    return s
n=input()
print(solve(n))
'''
INPUT:
1ragul's ragavendra B

OUTPUT:
1ragul's Ragavendra B

