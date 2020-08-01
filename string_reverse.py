#Reverse the String 
string=list(str(input("enter a String :")))
a=""
for i in string:
    a=i+a
print(a)
