ourlist = [2, 4, 3, 1, 5]

def ordered(ourlist):
    count = 0
    for i in range(1, len(ourlist)):
        if ourlist[i] > ourlist[i-1]:
            count += 1
    return(count)
    

while ordered(ourlist) != (len(ourlist) - 1):
    for i in range(1, len(ourlist)):
        if ourlist[i] < ourlist[i - 1]:
            a, b = ourlist.index(ourlist[i]), ourlist.index(ourlist[i - 1])
            ourlist[b], ourlist[a] = ourlist[a], ourlist[b]

print (ourlist)