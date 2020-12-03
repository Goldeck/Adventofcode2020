file = open("input.txt")

#3-5 f: fftfff




def checkCorrupt_pass(l):
	firstSplit = l.split(" ")
	min_max= firstSplit[0]
	letter = firstSplit[1].rstrip(":")
	password= firstSplit[2]

	secondSplit= min_max.split("-")
	mini = int(secondSplit[0])
	maxi= int(secondSplit[1])

	let_reccu= password.count(letter)

	if  mini <= let_reccu <= maxi:
		return 1
	else: 
		return 0

def checkCorrupt_pass2(l):
	firstSplit = l.split(" ")
	pos= firstSplit[0]
	letter = firstSplit[1].rstrip(":")
	password= firstSplit[2]

	secondSplit= pos.split("-")
	pos1 = int(secondSplit[0])
	pos2= int(secondSplit[1])

	let_reccu= password.count(letter)
	if  letter == password[pos1-1] and letter != password[pos2-1]:
		return 1
	if  letter != password[pos1-1] and letter == password[pos2-1]:
		return 1

	if  letter == password[pos1-1] and letter == password[pos2-1]:
		return 0
	else: 
		return 0

def check_corrupt(list):
	acc=0
	for l in list:
		isValid = checkCorrupt_pass2(l)
		if isValid == 1:
			acc=acc+1
	print(acc)
	return 0

check_corrupt(file)


l = "1-5 r: rvmjr"

checkCorrupt_pass(l)

#firstSplit = l.split(" ")
#min_max= firstSplit[0]
#letter = firstSplit[1].rstrip(":")
#password= firstSplit[2]



#secondSplit= min_max.split("-")
#min = secondSplit[0]
#max= secondSplit[1]
#print(min,max,letter, password)