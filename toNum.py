def calcPercent(name):
	percent = ''
	while name != []:
		char = name[0]
		no = name.count(char)
		percent += str(no)
		for m in range(no):
			position = name.index(char)
			name.pop(position)

	return percent

def sumWala(number):
	length = len(number)
	numList = list(number)
	perStr = ''
	for i in range(length//2):
		first = numList.pop(0)
		last = numList.pop(-1)
		added = str(int(first) + int(last))
		perStr += added
	if numList:
		perStr += numList.pop()
		
	return perStr

