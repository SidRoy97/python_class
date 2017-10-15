a = input("Enter some nos. : ").split(" ")
a = list(map(int,a))


def sort_order():
    def ascending(a,b):
        if(a<b):
            return True
        return False

    def descending(a,b):
        if(a>b):
            return True
        return False

    print("1->Ascending\n2->Descending\n : ")

sort_order()
    
    
