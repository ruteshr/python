#finding GCD between two numbers
#using recursive method:
def computeGCD(a,b):
  if(b==0):
    return a
  else:
    return computeGCD(b,a%b)

num1,num2=int(input("Enter two number ")),int(input())
print(computeGCD(num1,num2))

#using loop method:
def computegcd(a,b):
  while(b!=0):
    temp=b
    b=a%temp
    a=temp
  return a
n1,n2=int(input("enter two number")),int(input())
print(computegcd(n1,n2))

#=============================================
#gcd of three numbers
def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)
a,b,c=18,27,36
print(gcd(a,gcd(b,c)))
'''
OUTPUT:
9
'''
#=============================================
#gcd for multiple/array of inputs
def find_gcd(a,b):
    if(b==0):
        return a
    return find_gcd(b,a%b)
a=list(map(int,input().split(" ")))#getting i/p from the user and store it in the list
n1=a[0]
n2=a[1]
gcd=find_gcd(n1,n2)
for i in range(2,len(a)):
    gcd=find_gcd(gcd,a[i])
print(gcd)
'''
INPUT:
    16 8 4 20 36 40 84

OUTPUT:
    4
'''
