# PRINT THE FIBONACCI SERIES FOR THE NUMBER ENTERED#
#

def fibOf(num, hshDict):
	if num in hshDict:
		return hshDict[num]

	if num <=2:
		hshDict[num] = 1	
	else:
		hshDict[num] = fibOf(num-1, hshDict) + fibOf(num-2, hshDict)


	print(num , hshDict[num])
	return hshDict[num]

hshDict = {}
fibOf(25, hshDict)
