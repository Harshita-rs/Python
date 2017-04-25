#ATPG

import pickle;

linelist = []         #List used for splitting line wise from the file
in_num = 0
out_num = 0
linelistall = []
inp_list = []
inp_var = []
out_temp =[]
op = []
testGen = []
finalTestGen = []
count = 0
ct_list = []
f = open('s27.bench')
testGen1 = 'testGen.txt'  #open the file 

for line in f:            #for each line in the file
    linelist.append(line.split(' '))      #add each line to the LineList after spliiting by the delimiter space

for i in linelist:
    print("%s" % i)      #Print the contents after splitting

f.close()      #close the file

for i in range(len(linelist)):    #repeat this till the end of input from the linelist 
    for j in range(len(linelist[i])):    #step over
        if linelist[i][j] == 'inputs\n':     #look for matching string for Inputs (First line of the program)
            in_num = int(linelist[i][j-1])   #store the number of intputs to a variable
            print('Number of Inputs : ', in_num)  #print the input
			
xx = 0
while( xx < in_num * in_num ):
    xx = xx + 1
    testGen.append(xx)
	
testGen.insert(0,0)
testGen.pop()

for zz in testGen:
    binary = lambda n: n>0 and [n&1]+binary(n>>1) or []
    binary1 = '{0:04b}'.format(zz)      #generalize this to accept any number of inputs
    finalTestGen.append(binary1)

for yy in finalTestGen:
	print(yy)

with open(testGen1,'wb') as f:
    pickle.dump(finalTestGen,f)