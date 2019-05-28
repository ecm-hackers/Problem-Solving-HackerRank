def countingValleys(n, s):
	lvl = 0
	valley_count = 0
	for i in s:
		if i == "D":
			lvl-=1
		else:
			lvl+=1
		if(i=="U") and (lvl == 0):
			valley_count+=1
	return valley_count