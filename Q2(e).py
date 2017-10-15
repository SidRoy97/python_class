a = input("Enter some nos. : ").split(" ")
a = list(map(int,a))

b = input("Enter some nos. : ").split(" ")
b = list(map(int,b))

print("Your Lists : ")
print(a)
print(b)

def sort(a,b):
    ans = []
    a.sort()
    b.sort()
    print("Sorted lists : ")
    print(a)
    print(b)
    i = j = 0
    while((i <(len(a)))and(j<(len(b)))):
        if(a[i]<b[j]):
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            j += 1

    if(i == len(a)):
        while(j < len(b)):
            ans.append(b[j])
            j += 1
    else:
        while(i < len(a)):
            ans.append(a[i])
            i += 1
    return(ans)

print("Merge sorted list  : ",sort(a,b))
