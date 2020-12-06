def Charge_file():
	file = open("input.txt")
	lines = [l.strip() for l in file.readlines()]
	file.close()
	return lines

def cal_row(code):

	# between 0 and 127 --- 0, 0-63 64-127 0 31 32 64 [0,64[ [64,128[
	mini = 0
	maxi = 128
	Numrow = 0
	for i in code:
		if i == "F":
			maxi = (mini+ maxi) /2 
		if i == "B":
			mini = (mini+ maxi) /2
	return mini

def cal_col(code):
	mini = 0
	maxi = 8
	for i in code:
		if i == "L":
			maxi = (mini+ maxi) /2 
		if i == "R":
			mini = (mini+ maxi) /2
	return mini

# LLL LLR LRL LRR RLL RLR RRL RRR
#  0   1   2   3   4   5   6   7

def gene_id(line):
	row = cal_row(line[:7])
	col = cal_col(line[7:])
	result = (row * 8) + col
	return result


def Find_max_id(lines):
	max_id = 0
	for line in lines:
		id = gene_id(line)
		if (id > max_id):
			max_id = id
	return max_id 

def ids_set(lines):
	max_id = 0
	ensemble_id = set()
	for line in lines:
		id = gene_id(line)
		ensemble_id.add(id)
	print(ensemble_id)
	return ensemble_id

def Find_missing_ids(ids_set):
	missing_ids = set()
	for id in range(0,906):
		if id not in ids_set:
			missing_ids.add(id)
	print(missing_ids)		
	return missing_ids
	

def Find_my_id(ids_set):
	my_id=-1
	missing_ids = Find_missing_ids(ids_set)
	for id in missing_ids:
		if((id-1) in ids_set and id+1 in ids_set):
			my_id = id
	return id


	

lines = Charge_file()
max_id = Find_max_id(lines)
print(max_id)

ids_set = ids_set(lines)
my_id = Find_my_id(ids_set)
print(my_id)
# missing_ids = Find_missing_ids(ids_set)

# print(cal_row("BFFFBBFRRR"))
# print(cal_col("BFFFBBFRRR"))



# print(gene_id("BBFFBBFRLL"))
# print(gene_id("BBFFBBFRLL"))