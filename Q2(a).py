(a,b) = input("Enter two nos. : ").split(" ")
a = int(a)
b = int(b)

def GCD(a,b):
    gcd = 1
    big = max([a,b])
    small = min([a,b])
    print(big)
    print(small)
    if(big%small == 0):
        gcd = gcd * small
    else:
        divide = 1
        while(divide):
            for i in range(2,(min([a,b])//2)+1):
                if(small%i == 0 and big%i == 0):
                    gcd = gcd * i
                    small = small/i
                    big = big/i
                else:
                    if(i == (small//2)):
                        divide = 0
    return(gcd)


print("GCD of",a,b,"=",GCD(a,b),sep = " ")
