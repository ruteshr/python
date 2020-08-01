#String is Palindrome 
string=list(str(input("enter a String :")))
a=""
for i in string:
    a=i+a
if("".join(string)==a):
    print('{} is palindrome'.format("".join(string)) )
else:
    print('{} is not palindrome'.format("".join(string)) )
