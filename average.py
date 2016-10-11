def average(listz=[]):
    sumList = 0
    for indx in range(len(listz)):
        sumList = sumList + listz[indx]
    avgList = float(sumList) / len(listz)
    return avgList

l = range(20)

average(l)

