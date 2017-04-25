masterList = []
list1 = []
inputList = []
outputList = []
outputVar = []
inputVar = []
inputVar1 = []
outputCount = []
ctrList = []
finalList = []
list1 = []
inputVar1 = []
inputNum = 0
outputNum = 0
searchString = 0
primaryInput = 0
cktOutput = 0
ctr = 0

inputFile= open('s27.bench')

for x in inputFile:
	line= x.split(' ')
	masterList.append(line)
	
print('The contents of the file are: ')
for y in (masterList):
	print(y)

inputFile.close()

for i in range(len(masterList)):
    for j in range(len(masterList[i])):
        if masterList[i][j] == 'inputs\n':
            inputNum = int(masterList[i][j-1])
            print('Number of inputs =', inputNum)
        if masterList[i][j] == 'outputs\n':
            outputNum = int(masterList[i][j-1])
            print('Number of outputs = ', outputNum)
        list1.append(masterList[i][j])
		
print('\n')
for m in range(len(list1)):
	if list1[m] == 'INPUT(G0)\n':
		for n in range(m, m+inputNum):
			inputList.append(list1[n])
			#print(list1[n])

print('The checkpoints of the circuit are :')
for d in range(len(inputList)):
	inputVar1.append(inputList[d][6:8])
     

for o in range(len(inputVar1)):
    print(inputVar1[o])	

for pp in range(len(masterList)):
    if masterList[pp][0][0:1] == 'G':
        outputVar.append(masterList[pp][0])

for ptr1 in range(len(outputVar)):
	for ptr2 in range(len(masterList)):
		for ptr3 in range(len(masterList[ptr2])):
			if masterList[ptr2][ptr3].find(outputVar[ptr1]) !=-1:
				outputCount.append(outputVar[ptr1])
			#print(outputCount)
				
for k in range(len(outputVar)):
    count = 0
    for l in range(len(outputCount)):
        if outputCount[l].find(outputVar[k]) != -1:
            count = count + 1
    ctrList.append(count)

for v in range(len(outputVar)):
    if ctrList[v] > 2:
        print(outputVar[v])



        

