def chargemap():
	file_name = "input.txt"
	file = open(file_name)
	lines = [l.strip() for l in file.readlines()]
	file.close()
	return lines

	
def isTree(lines,x,y):
	patern_lignes = len(lines[0])
	return "#" == lines[x][(y%(patern_lignes))] 


def total_tree_Met(lines,co_ini,traj):
	acc = 0
	x_traj, y_traj, x, y = traj[0], traj[1], co_ini[0], co_ini[1]
	end_slide = (len(lines) - 1) / traj[0]

	for i in xrange(0,end_slide):
		x = x + x_traj
		y = y + y_traj
		if isTree(lines,x , y):
			acc = acc +1
	return acc

lines = chargemap()

def totalTrees(trajectories):
	results=[]
	co_ini = [0,0]
	for traj in trajectories:
		NumTreeMet = total_tree_Met(lines,co_ini,traj)
		results.append(NumTreeMet)
		print(results)
	total = reduce(lambda a,b : a*b, results)
	print total

trajectories=[[1,1],[1,3],[1,5],[1,7],[2,1]]
totalTrees(trajectories)