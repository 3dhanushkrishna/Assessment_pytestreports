def Amstrong(x):
    sum = 0
    temp = x
    while temp>0:
        r=temp % 10
        sum  += r**3
        temp //= 10
        if x == sum:
            return True
        else:
            return False
def Div_8(x):
    if x%8==0:
        return True
    else:
        return False
def Smallest(x,y,z):
    if x<y and x<z:
        return x
    elif y<x and y<z:
        return y
    else:
        return z

def Evenorodd(x):
    if x%2==0:
        return True
    else:
        return False
def Palindrome(x):
    if x == x[::-1]:
        return True
    else:
        return False
if __name__=="__main__":
    a=int(input("enter the a value: "))
    b=int(input("enter the b value: "))
    c=int(input("enter the c value: "))
    amstrong=Amstrong(a)
    print(amstrong)
    div_8=Div_8(a)
    print(div_8)
    smallest=Smallest(a,b,c)
    print(smallest)
    evenorodd=Evenorodd(a)
    print(evenorodd)
    palindrome=Palindrome(a)
    print(palindrome)