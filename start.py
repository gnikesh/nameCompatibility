from toNum import calcPercent, sumWala
def calculate():
	name1 = input("Enter First Name: ")
	name2 = input("Enter Second Name: ")

	inpString = name1.upper().strip() + name2.upper().strip()
	numbers = calcPercent(list(inpString))
	ans = int(sumWala(numbers))
	while ans > 100:
		ans = int(sumWala(str(ans)))
	
	print('Name Compatibility: ' + str(ans) + '%')
	
if __name__ == '__main__':
	calculate()



