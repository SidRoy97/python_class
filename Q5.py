cont = True

d = {}

while(cont):
    a = input("Enter state and city : ")
    a = a.split(" ")
    a = tuple(a)
    #print(a)
    
    print("Enter the places of interest in",a[1],"\n :",end = " ")
    v = input()
    v = v.split(" ")
    #print(v)

    d[a] = v

    print("Your dictionary of places : ",d)
    #Modify list

    if(int(input("Do you wanna modify the list of places (0/1) : ")) == 1):
        m = (input("Enter the state and the city : ")).split(" ")
        m = tuple(m)
        y = 1
        while(y):
            if(m in d):
                for i in d:
                    if(i == m):
                        d[i].extend(input("Enter the places : ").split(" "))
            
                y = int(input("Forgot some ? Wanna add more places? (0/1) : "))
            else:
                print("The state and place not added...Add first")
                y = 0
    print("Your dictionary of places AFTER MODIFICATION : ",d)
    if(int(input("Wanna add more(1/0) : ")) == 1):
        cont = True
    else:
        cont = False
        
