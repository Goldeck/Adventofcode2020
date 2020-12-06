
def chargelines():
	file = open("input.txt")
	lines= [parseline(l.strip()) for l in file.readlines()]
	file.close()
	return lines

def parseline(line):
	firstSplit = line.split(" ")
	min_max= firstSplit[0]
	letter = firstSplit[1].rstrip(":")
	password= firstSplit[2]

	secondSplit= min_max.split("-")
	mini = int(secondSplit[0])
	maxi= int(secondSplit[1])
	return [mini, maxi, letter, password]



def checkCorrupt_pass(mini, maxi, letter, password):
	let_reccu= password.count(letter)
	return  (mini <= let_reccu <= maxi)

def checkCorrupt_pass2(mini, maxi, letter, password):
	return (letter == password[mini-1]) ^ (letter == password[maxi-1])

def check_corrupt(parsedInputs):
	acc=0
	for mini, maxi, letter, password in parsedInputs:
		isValid = checkCorrupt_pass2(mini, maxi, letter, password)
		if isValid:
			acc=acc+1
	print(acc)
	return acc

parsedInputs = chargelines() 
check_corrupt(parsedInputs)

