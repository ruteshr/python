#pascal's triangle
num,a=int(input("enter no of rows")),[]
for i in range(num):
  row=[]
  for j in range(i+1):
    if(j==0 or j==i):
      row.append(1)
    else:
      row.append(a[i-1][j-1]+a[i-1][j])
  a.append(row)
for i in range(num):
  for j in range(num-i-1):
    print(end=" ")
  for j in range(i+1):
    print(a[i][j],end=" ")
  print()
