def check(n):
    if(n<10):
        return n
    if(n==10):
        return 'A'
    if(n==11):
        return 'B'
    if(n==12):
        return 'C'
    if(n==13):
        return 'D'
    if(n==14):
        return 'E'
    if(n==15):
        return 'F'
def octa(number):
    octal=""
    while(number!=0):
        octal=str(number%8) +octal
        number=int(number/8)
    return octal
def he(number):
    hexa=""
    while(number!=0):
        temp=check(number%16)
        hexa=str(temp)+hexa
        number=int(number/16)
    return hexa
def binary(number):
    bina=""
    while(number!=0):
        bina=str(number%2)+bina
        number=int(number/2)
    return bina

def lenbinary(number):#formatting the output with the length of binary value
    bina=""
    while(number!=0):
        bina=str(number%2)+bina
        number=int(number/2)
    return bina
def print_formatted(number):
    # your code goes here
    #to format the value upto binary length
    leng=len(lenbinary(number))
    for number in range(1,number+1):
        octalvalue=octa(number)
        hexavalue=he(number)
        binaryvalue=binary(number)
        print("{:>{width}} {:>{width}} {:>{width}} {:>{width}}".format(number,octalvalue,hexavalue,binaryvalue,width=leng))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
INPUT:
    5
OUTPUT:
  1   1   1   1                                                                                                               
  2   2   2  10                                                                                                               
  3   3   3  11                                                                                                               
  4   4   4 100                                                                                                               
  5   5   5 101
