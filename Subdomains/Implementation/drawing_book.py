
# to reach end we require n//2 i.e. 5 pages
# plr = 4//2 (i.e. p//2) since first side we are sure we reach from the start
# blr = tlr - plr 

def pageCount(n, p):
	return min(p//2 ,(n//2) - (p//2))
