# edit_distance.py: Reads strings x and y from standard input and computes
# the edit-distance matrix opt. The program outputs x, y, the dimensions
# (number of rows and columns) of opt, and opt itself.

import stdarray
import stdio
import timeit



def recursiveSolution(i,j):
	if i==opt_m_recursive-1:
		opt_recursive[i][j]=(opt_n_recursive-j-1)*2
		return opt_recursive[i][j]
	if j==opt_n_recursive-1:
		opt_recursive[i][j]=(opt_m_recursive-i-1)*2
		return opt_recursive[i][j]
		
	if x[i]==y[j]:
		opt_recursive[i][j]=min(recursiveSolution(i+1,j+1),recursiveSolution(i+1,j)+2,recursiveSolution(i,j+1)+2)
		return opt_recursive[i][j]
	else:
		opt_recursive[i][j]=min(recursiveSolution(i+1,j+1)+1,recursiveSolution(i+1,j)+2,recursiveSolution(i,j+1)+2)
		return opt_recursive[i][j]

def dynamicSolution():
	# Fill the penalty of string x[i] with empty string 
	for i in range(opt_n):
		opt[opt_m-1][i]=(opt_n-i-1)*2
	
	# Fill the penalty of string y[i] with empty string 
	for i in range(opt_m):
		opt[i][opt_n-1]=(opt_m-i-1)*2
		
	# Filling rest of the matrix with dynamic programming formula: 
	# opt[i][j] = min{opt[i+1][j+1] + 0/1, opt[i+1][j] + 2, opt[i][j+1] + 2} where 0 and 1 value depends on whether x[i] and y[j] are match or mismatch and 2 is penalty for gap
	for j in range (opt_n-2,-1,-1):
		for i in range (opt_m-2,-1,-1):
			if x[i]==y[j]:
				opt[i][j]=min(opt[i+1][j+1],opt[i+1][j]+2,opt[i][j+1]+2)
			else:
				opt[i][j]=min(opt[i+1][j+1]+1,opt[i+1][j]+2,opt[i][j+1]+2)
	return opt[0][0]
		
def printMat(sol,m,n):
	for i in range (m):
		for j in range(n):
			stdio.writef('%3d ', sol[i][j])
		stdio.writeln()  



def recursiveTime():
	SETUP_CODE= '''
import stdarray
import stdio
from __main__ import x,y,recursiveSolution
m=len(x)
n=len(y)
opt_recursive = stdarray.create2D(m+1, n+1, 0)
opt_m_recursive = len(opt_recursive)
opt_n_recursive = len(opt_recursive[0])'''
	TEST_CODE='''
recursiveSolution(0,0)
'''
	
	times= timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE,number= 3)
	return times/3
	
def dynamicTime():
	SETUP_CODE= '''
import stdarray
import stdio
from __main__ import x,y,dynamicSolution
m=len(x)
n=len(y)
opt = stdarray.create2D(m+1, n+1, 0)
opt_m = len(opt)
opt_n = len(opt[0])'''
	TEST_CODE='''
dynamicSolution()
'''
	
	times= timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE,number= 3)
	return times/3
	
		
def alignement(x,y,opt,opt_m,opt_n):
	 
	i=0
	j=0
	while (i!=opt_m-1 and j!=opt_n-1):
		
		if opt[i][j]==opt[i][j+1]+2:
				print "  -",y[j],"2"
				j=j+1
		elif opt[i][j]==opt[i+1][j]+2:
				print x[i],"  -","2"
				i=i+1
		if(x[i]==y[j]):
			if opt[i][j]==opt[i+1][j+1]:
				print x[i]," ",y[j],"0"
				i=i+1
				j=j+1
		else:
			if opt[i][j]==opt[i+1][j+1]+1:
				print x[i]," ",y[j],"1"
				i=i+1
				j=j+1
	
	if i<opt_m:
		for k in range (i,opt_m-1):
			print x[k],"  -","2"
	if j<opt_n:
		for k in range (j,opt_n-1):
			print "-  ",y[k],"2"
	
	
# Read x and y.
x = stdio.readString()
y = stdio.readString()


# Create (M + 1) x (N + 1) matrix opt with elements initialized to 0, where
# M and N are lengths of x and y respectively.
m = len(x)
n = len(y)

opt = stdarray.create2D(m+1, n+1, 0)
opt_m = len(opt)
opt_n = len(opt[0])

opt_recursive = stdarray.create2D(m+1, n+1, 0)
opt_m_recursive = len(opt_recursive)
opt_n_recursive = len(opt_recursive[0])

# Write x, y, dimensions of opt, and opt.
stdio.writeln(x)
stdio.writeln(y)
stdio.write(opt_m)
stdio.write(' ')
stdio.writeln(opt_n)		

print "Executing dynamic Solution:"    
print "Edit distance: ",dynamicSolution() 
print "Following is best alignement "
alignement(x,y,opt,opt_m,opt_n)


#
#Execute Recursive solution and performance check only for small strings
if opt_m <14 or opt_n<14:	
	print  "Executing recursive Solution:"
	print "Edit ditance:",recursiveSolution(0,0)	
	print "Checking Performance of both approach:"
	recTime=recursiveTime()
	print "Recursive time taken: ",recTime

	dynTime= dynamicTime()
	print "Dynamic time taken", dynTime

	if dynTime < recTime:
		print "Dynamic is faster by ", recTime/dynTime,"x faster"

			




