option = int(input("Enter 1 for sum of the digits and 2 for factorial"))

n = int(input("Enter a no. : "))

if(option == 1):
    sum = 0
    while(n):
        sum += n%10
        n = n//10
    print(sum)

elif(option == 2):
    fact = 1
    if(n == 0 or n == 1):
        fact = 1
    else:
        while(n != 1):
            fact = fact * n
            n -= 1
    print(fact)
