#prime number from the given interval
lower=int(input("Enter lower interval"))
upper=int(input("Enter Upper interval"))
for i in range(lower,upper+1,1):
  if(i>1):
    for j in range(2,i):
      if(i%j==0):
        break
    else:
      print(i,end=" ")
