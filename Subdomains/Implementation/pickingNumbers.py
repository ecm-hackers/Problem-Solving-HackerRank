def pickingNumbers(a):
    maxim = 0
    a = sorted(a)
    for i in range(len(a)):
        count = 0
        for j in range(i+1,len(a)):
            if a[j]-a[i]<=1:
                count+=1
        if count > maxim:
            maxim = count

    return maxim+1
