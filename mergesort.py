ourlist = [1, 100, 4, 10, 7, 6]

def mergesort(ourlist):
    lst = []
    middle = len(ourlist)//2

    lst.append(ourlist[0 : (len(ourlist)//2)])
    lst.append(ourlist[len(ourlist)//2 : len(ourlist)])

    for i in range(2):
        temp = lst[i]
        lst.append(temp[0 : (len(temp)//2)])
        lst.append(temp[len(temp)//2 : len(temp)])
    
    lst.remove(lst[0])
    lst.remove(lst[0])

    for i in range(len(lst)):
        if (len(lst[i])) > 1:
            temp = lst[i]
            if temp[0] > temp[1]:
                a, b = temp.index(temp[0]), temp.index(temp[1])
                temp[b], temp[a] = temp[a], temp[b]

    monster1 = []
    monster2 = []

    for i in range(0, (middle - 1)):
        temp = lst[i]
        monster1 += temp
    
    for i in range(middle - 1, len(lst)):
        temp = lst[i]
        monster2 += temp

    monster = []
    monster.append(monster1)
    monster.append(monster2)

    for i in range(len(monster)):
        temp = monster[i]
        
        for i in range(1, len(temp)):
            while temp[i] < temp[i - 1]:
                a, b = temp.index(temp[i]), temp.index(temp[i - 1])
                temp[b], temp[a] = temp[a],  temp[b]
    

    var1 = monster[0]
    var2 = monster[1]
    behemoth = []

    for i in range(0, len(lst) - 1):
        if var1[i] < var2[i]:
            behemoth.append(var1[i])
            behemoth.append(var2[i])
        else:
            behemoth.append(var2[i])
            behemoth.append(var1[i])
            

    
    return behemoth 


print (mergesort(ourlist))
