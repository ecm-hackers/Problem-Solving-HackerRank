 # My approach ....
 # Count consecutive zeroes .. note their indexes 
 # see if value after first index is positive or negative 




# if value is negative , valley_count ++
def countingValleys(n, s):
    value = []
    for i in s:
        if i == "D":
            value.append(-1)
        else:
            value.append(1)

    # sum approach
    add = 0
    zero_indexes = [0]
    i = 0
    while i!=len(value):
        add+=value[i]
        if add == 0:
    #        print(value[i])
            zero_indexes.append(i)
        i+=1
    #if (len(value)-1) in zero_indexes:zero_indexes.remove(len(value)-1)
    print(zero_indexes)
    print(value)
    valley_count = 0
    for i in range(len(zero_indexes)-1):
    	print([zero_indexes[i],zero_indexes[i+1]])
    	new = [zero_indexes[i],zero_indexes[i+1]]
    	if new[1] == new[0]+1:
    		if value[new[0]] == -1:
    			valley_count+=1
    	else:
    		if value[new[0]+1] == -1:
    			valley_count+=1
    	# print([])
    	# if (sum(value[zero_indexes[i]:zero_indexes[i+1]-1]))<0:
    	# 	valley_count+=1
    return valley_count


print(countingValleys(12,"DUDDDUUDUU"))
