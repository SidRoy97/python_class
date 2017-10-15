#Cannibal-Missionary

# 0 -> missionary
# 1 -> cannibal

start = [1,1,1,0,0,0]
end = []

valid = True

while(start):
    while(valid):
        end.append(start[0])
        del start[0]
        if(start.count(1)>start.count(0)):
            valid = False
        elif(end.count(1)>end.count(0)):
            valid = False
    if(not valid):
        if(start.count(1)>start.count(0)):
            pass
        elif(end.count(1)>end.count(0)):
            while(end.count(1)<=end.count(0)):
                start.append(1)
                end.remove(1)
            valid = True
    print("Start :  ",start)
    print("End :   ",end)
            
        
