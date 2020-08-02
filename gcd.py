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
