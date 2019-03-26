def toDecimal(bin):
    decimalNumber, i=0,0
    while bin!=0:
        remainder=bin%10
        bin//=10
        decimalNumber+=remainder*(2**i)
        i+=1
    return decimalNumber

def toBinary(num):
    binaryNumber=0
    remainder, i=1,1
    while num!=0:
        remainder=num%2
        num//=2
        binaryNumber+=remainder*i
        i*=10
    return binaryNumber

bin=10111
num=50
print(toDecimal(bin))
print(toBinary(num))

