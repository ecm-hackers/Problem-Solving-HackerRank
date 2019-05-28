def sockMerchant(n, ar):
	# to return number of pairs
	# using non-logic python trick
	count = 0
	for i in list(set(ar)):
		count+=ar.count(i)//2
		print(i,"",ar.count(i))

	return count


sockMerchant(9,[10 ,20 ,20 ,10 ,10 ,30 ,50 ,10 ,20])