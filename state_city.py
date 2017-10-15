cont = 1
d = {}

while(cont):
    print("1->Add state\n2->Add more cities\n3->Remove city\n4->City Count\n5->Display\n6->exit\n : ",end = "")
    option = int(input())

    if(option == 1):
        state = input("Enter state name : ")
        cities = input("Enter cities : ").split(" ")
        cities = ", ".join(cities)
        d[state] = cities
    elif(option == 2):
        state = input("Enter state name : ")
        if(state in d):
            cities = input("Enter cities : ").split(" ")
            cities = ", ".join(cities)
            d[state] = d[state] + ", " + cities 
        else:
            print("First add that state")
    elif(option == 3):
        state = input("Enter state name : ")
        if(state in d):
            city = input("Enter the city : ")
            r = list(d[state].split(", "))
            if(city in r):
                r.remove(city)
                r = ", ".join(r)
                d[state] = r
            else:
                print("That city isn't added")
        else:
            print("First add the state")
    elif(option == 4):
        state = input("Enter state name : ")
        if(state in d):
            print("No. of cities in",state," :",(d[state].count(", "))+1,end = " ")
        else:
            print("First add the state")
    elif(option == 5):
        print(d)
    elif(option == 6):
        cont = 0

