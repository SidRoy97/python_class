print("1->GCD\n2->Validate date and give the next date\n3->Generate prime nos\n :", end =" ")
option = int(input())

if(option == 1):
    (a,b) = input("Enter two nos. : ").split(" ")
    a = int(a)
    b = int(b)
    gcd = 1
    def isprime(n):
        p = True
        for i in range(2,(n//2 + 1)):
            if(n%i == 0):
                p = False
                break
        return p
    
    if(isprime(a) or isprime(b)):
        gcd = 1
    else:
        big = max([a,b])
        small = min([a,b])
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
    print("GCD of",a,b,"=",gcd,sep = " ")
        
    

elif(option == 2):
    date = input("Enter the date dd/mm/yyyy: ")
    (d,m,y) = date.split("/")
    d = int(d)
    m = int(m)
    y = int(y)

    valid = True

    if(m in [4,6,9,11] and d not in range(1,31) ):
        valid = False

    elif(m in [1,3,5,7,8,10,12] and d not in range(1,32)):
        valid = False

    elif(m == 2):
        if(y%4 == 0):
            if(d not in range(1,30)):
                valid = False
        else:
            if(d not in range(1,29)):
                valid = False

    if(valid):
        print("VALID")
        d = d + 1
        if(m in [4,6,9,11] and d == 31):
            d = 1
            m += 1
        elif(m in [1,3,5,7,8,10,12] and d == 32):
            d = 1
            m += 1
            if(m > 12):
                m = 1
                y += 1
        elif(m == 2):
            d += 1
            if(y%4 == 0):
                if(d > 29):
                    d = 1
                    m += 1
            else:
                if(d > 28):
                    d = 1
                    m += 1
        print("NEXT DATE IS : ")
        print(d,m,y,sep = " /")
    else:
        print("INVALID")

if(option == 3):
    def isprime(n):
        p = True
        for i in range(2,(n//2 + 1)):
            if(n%i == 0):
                p = False
                break
        return p
    upper_limit = int(input("Enter the upper limit : "))

    for i in range(2,upper_limit):
        if(isprime(i)):
            print(i)
        
            
