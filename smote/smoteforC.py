import math
import operator
import random
class1={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'H':6}
classrev={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'H'}
spotsize={'X':0,'R':1,'S':2,'A':3,'H':4,'K':5}
spotsizerev={0:'X',1:'R',2:'S',3:'A',4:'H',5:'K'}
spotdstr={'X':0,'O':1,'I':2,'C':3}
spotdstrrev={0:'X',1:'O',2:'I',3:'C'}
ones =0
twos=0

csample=open("csample.txt" , 'w')
def loadDataset(dataset,filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
		lines = csvfile.readlines()
		'''dataset=csvfile.readlines()'''
		#print(lines,'\n\n')
		#dataset=[]
		for i in lines:
			i=i.split(',')
			i[12]=i[12].split("\n" )
			i[12]=i[12][0]
			for j in range(13):
				if(j==0):
					i[j]=class1[i[j]]
				elif(j==1):
					i[j]=spotsize[i[j]]
				elif(j==2):
					i[j]=spotdstr[i[j]]
				else:
					i[j]=ord(i[j])
			#if(i[10]==50):		
			dataset.append(i)
			'''print(i , '\n')'''
	       
		'''print(dataset)'''
	for x in range(len(dataset)):
		if random.random() < split:
		    trainingSet.append(dataset[x])
		else:
		    testSet.append(dataset[x])
		'''trainingSet.append(dataset[x])
		testSet.append(dataset[x])'''
 
 
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		
		'''print(instance1 , '      ggggggggggg\n' , instance2)'''
		'''distance += pow((instance1[x] - instance2[x]), 2)'''
		distance=0
		for i in range(length):
			distance += pow((instance1[i] - instance2[i]), 2)
			
		
		return math.sqrt(distance)
 
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	print("len fo distances ",len(distances))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors
 

trainingSet=[]
testSet=[]
dataset=[]
Synthetic=[]
newindex=0
neighbors=[]
def Populate(N,i,neighbors,k,testSet):
	global newindex
	global Synthetic,ones,twos
	while (N !=0):
		nn=random.randint(0, k-1)
		a=[]
		for attr in range(13):
			
			'''temp=(neighbors[nn][attr]-testSet[attr])>0?neighbors[nn][attr]−testSet[attr]:-(neighbors[nn][attr]−testSet[attr])'''
			dif=neighbors[nn][attr]-testSet[attr]
			
			gap=random.random()
			val= int(testSet[attr]+ gap*dif)
			#print("val",val,"newindex" , newindex , "attr" , attr )
			
			#Synthetic[newindex][attr]=val
			
			a.append(val)
			#print(Synthetic[newindex][attr])
			
			if(attr==0 and val> 6):
				a[attr]=6
			if(attr==1 and val> 5):
				[attr]=5
			if(attr==2 and val> 3):
				a[attr]=3

		for i in range(13):
			if(i==0):
				a[i]=classrev[a[i]]
				
			elif(i==1 ):
				a[i]=spotsizerev[a[i]]
			elif(i==2 ):
				a[i]=spotdstrrev[a[i]]
			else :
				a[i]=chr(a[i])
			if(i==12):	
				csample.write(a[i] )
			else:
				csample.write(a[i]+',')

		csample.write("\n")
		Synthetic.append(a)
		if(a[10]=='1'):
			ones+=1
		if(a[10]=='2'):
			twos+=1
		newindex+=1
		N-=1
		#print(N)
	#print(Synthetic ,"-------------------" , len(Synthetic))
			
	

	
def smote(T,N,k):
	global ones
	global twos
	if(N<100):
		T =(N/100)*T
		N = 100
	N =(int)(N/100)
	
       
	for i in range(T):
		neighbors = getNeighbors(trainingSet, testSet[i], k)
		#print(testSet[i],"------>>>>>",neighbors)
		for j in range(13):
			if(j==0):
				csample.write(classrev[testSet[i][j]]+",")
				
			elif(j==1 ):
				csample.write(spotsizerev[testSet[i][j]]+",")
			elif(j==2 ):
				csample.write(spotdstrrev[testSet[i][j]]+',')
			elif(j==12) :
				csample.write(chr(testSet[i][j]))
			else:
				csample.write(chr(testSet[i][j])+',')
				
			#csample.write(a[i] + ",")
		csample.write("\n")
		if(testSet[i][10]==49):
			N1=10
			print(N1)
			ones+=1
			Populate(N1, i, neighbors,k,testSet[i])
		elif(testSet[i][10]==50):
			N2=200
			print(N2)
			twos+=1
			Populate(N2, i, neighbors,k,testSet[i])
		
		#Populate(N, i, neighbors,k,testSet[i])
		

	
def main():
	# prepare data
	
	loadDataset(dataset,'c.txt', 0.67,trainingSet, testSet)
	print('Train set: ' + repr(len(trainingSet)))
	print('Test set: ' + repr(len(testSet)))
	
	#neighbors=[]
	k = 5 #nearest neighbo no
	'''for x in range(len(testSet)):
		neighbors = getNeighbors(trainingSet, testSet[x], k)
		print(testSet[x],"------>>>>>",neighbors)'''
	

	smote(len(testSet),300,k)
	print("Sythetic------------------>>>>>>>>>>>")
	print(len(Synthetic))

	#print("63ee56666666666666666666666666666666  " , ones ,"     4444  "  , twos)
	csample.close()

main()


