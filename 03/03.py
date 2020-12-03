
def chargemap():
	file_name = "input.txt"
	file = open(file_name)
	lines = [l.strip() for l in file.readlines()]
	file.close()
	return lines

	
def isTree(lines,x,y):
	patern_lignes = len(lines[0])
	return "#" == lines[x][(y%(patern_lignes))] 

#0-322 lignes



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


co_ini = [0,0]
#down 1 right 3
#tajectory = [1,3]

#NumTreeMet = total_tree_Met(lines,co_ini,tajectory)
#print(NumTreeMet)

def totalTrees(trajectories):
	results=[]
	for traj in trajectories:
		NumTreeMet = total_tree_Met(lines,co_ini,traj)
		results.append(NumTreeMet)
		print(results)
	total = reduce(lambda a,b : a*b, results)
	print total

trajectories=[[1,1],[1,3],[1,5],[1,7],[2,1]]
totalTrees(trajectories)
#Right 1, down 1. 65
#Right 3, down 1. (This is the slope you already checked.) 236
#Right 5, down 1. 59
#Right 7, down 1. 60
#Right 1, down 2. 37
