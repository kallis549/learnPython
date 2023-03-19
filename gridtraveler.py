# Say that you are a traveller on a 2D grid, You being in the
# top-left corner and your goal is to travel to the bottom-right
# corner. You may only move down or right.
# In how many ways can you travel to the goal on a grid with dimensions m*n?

def gridtraverse(m, n, hashDict):
	key=str(m)+"|"+str(n)
	if m ==0 or n ==0:
		hashDict[key] = 0
	if m ==1 and n == 1:
		hashDict[key] = 1
	if key in hashDict:
		return hashDict[key]
	else:
		hashDict[key] = gridtraverse(m-1, n, hashDict) + gridtraverse(m, n-1, hashDict)
	return hashDict[key]		

hashDict = {}
print (gridtraverse(18,18, hashDict))