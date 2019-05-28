def getMoneySpent(keyboards,drives,b):
	pairs = [sum([i,j]) for i in keyboards for j in drives]
	pairs = sorted(list(set(pairs)))[::-1]
	flag = 1
	for i in pairs:
		if i<=b:
			flag = 0
			return i
			break
	if flag == 1:
		return -1

getMoneySpent([4],[5],5)


# result : Brute Force Worked Well All submissions accepted
