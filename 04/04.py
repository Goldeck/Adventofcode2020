
def Open_file():
	file = open("input.txt")
	lines = file.readlines()
	# print(lines)
	return lines



def Generate_Passports(lines):
	passports = []
	passport = {}
	for line in lines:
		donnees = line.split( )
		if donnees:
			for donnee in donnees:
				key_val= donnee.split(":")
				passport[key_val[0]] = key_val[1]
		else:
			passports.append(passport)
			passport = {}
	passports.append(passport)
	return passports

def pid_is_valid(pid):
	try :
		if len(pid) == 9 and  int(pid) :
			return True
		else:
			return False
	except:
		return False

def hcl_is_valid(hcl):
	hexa = {"0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"}
	try:
		if hcl[0] == "#" and all( l in hexa for l in hcl[1:]) and len(hcl) == 7:
			return True
	except:
		return False


	
def hgt_is_valid(hgt):
	try:
		if (hgt[-2:] == "cm" and 150 <= int(hgt[0:len(hgt)-2]) <= 193):
			return True
		if (hgt[-2:] == "in" and 59 <= int(hgt[0:len(hgt)-2]) <= 76):
			return True
	except:
		return False

def passport_is_valid(passport):
	condition_on_keys = ("ecl"  in passport) and ("pid"  in passport) and ("eyr"  in passport) and ("hcl"  in passport) and ("byr"  in passport) and ("iyr"  in passport) and ("hgt"  in passport)
	eye_clors =("amb","blu","brn","gry","grn","hzl","oth")

	if condition_on_keys:
		ecl_cond = passport["ecl"] in eye_clors

		byr_cond = (len(passport["byr"]) == 4) and (1920 <= int(passport["byr"]) <= 2002)
		iyr_cond = (len(passport["iyr"]) == 4) and (2010 <= int(passport["iyr"]) <= 2020)
		eyr_cond = (len(passport["eyr"]) == 4) and (2020 <= int(passport["eyr"]) <= 2030)
		
		pid_cond = pid_is_valid(passport["pid"])
		hcl_cond = hcl_is_valid(passport["hcl"])
		hgt_cond = hgt_is_valid(passport["hgt"])

		if ( ecl_cond and pid_cond and eyr_cond and hcl_cond and byr_cond and iyr_cond and hgt_cond ):
			return True



def total_passports_valid(passports):
	acc = 0
	for passport in passports:
		if(passport_is_valid(passport)):
			acc = acc + 1
	return acc


lines = Open_file()

passports = Generate_Passports(lines)
result = total_passports_valid(passports)
print(result)

# un passport valid qui manque