def bonAppetit(bill, k, b):
	if b == (sum(bill)-bill[k])//2:
		print("Bon Appetit")
	else:
		print(abs((sum(bill) - bill[k])/2 - b)) 

