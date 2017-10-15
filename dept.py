cont = 1
l = []
r = ["Department ID","Department Name","Employees"]
while(cont):
    print("1->Add\n2->No.of Employees\n3->Maximum employees\n4->Display\n5->exit\n : ",end = "")
    option = int(input())

    if(option == 1):
        d = {}
        d = d.fromkeys(r)
        print("Department ID : ")
        d["Department ID"] = int(input())
        print("Department Name : ")
        d["Department Name"] = (input())
        print("Name of the Employees : ")
        d["Employees"] = input().split(" ")
        l.append(d)
    elif(option == 2):
        depid = int(input("Enter the Department ID : "))
        v = False
        for i in l:
            if(i["Department ID"] == depid):
                depname = input("Enter the Department Name : ")
                if(i["Department Name"] == depname):
                    print(len(i["Employees"]))
                    v = True
        if(v == False):
            print("Wrong Department info")
    elif(option == 3):
        depid = ""
        depname = ""
        m = 0
        for i in l:
            if(len(i["Employees"]) > m):
                m = len(i["Employees"])
                depid = i["Department ID"]
                depname = i["Department Name"]
        print("Max employees = ",m)
        print("Department ID = ",depid)
        print("Department name = ",depname)
    elif(option == 4):
        print(l)
    elif(option == 5):
        cont = 0
