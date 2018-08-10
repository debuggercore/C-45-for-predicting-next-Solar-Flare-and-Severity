import math
import operator
import random 
 
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
        with open(filename, 'r') as csvfile:
                lines = csvfile.readlines()
                '''dataset=csvfile.readlines()'''
                print(lines,'\n\n')
                dataset=[]
                for i in lines:
                        i=i.split(',')
                        i[12]=i[12].split("\n" )
                        i[12]=i[12][0]
                        for j in range(13):
                                i[j]=ord(i[j])
                                   
                        dataset.append(i)
                        '''print(i , '\n')'''
               
                '''print(dataset)'''
        for x in range(len(dataset)-1):
                for y in range(4):
                   ''' dataset[x][y] = ord(dataset[x][y])'''
                if random.random() < split:
                    trainingSet.append(dataset[x])
                else:
                    testSet.append(dataset[x])
 
 
def euclideanDistance(instance1, instance2, length):
        distance = 0
        for x in range(length):
                
                print(instance1 , '      ggggggggggg\n' , instance2)
                '''distance += pow((instance1[x] - instance2[x]), 2)'''
                distance=0
                for i in range(13):
                        distance += pow((instance1[x][i] - instance2[x][i]), 2)
                        
                
                return math.sqrt(distance)
 
def getNeighbors(trainingSet, testInstance, k):
        distances = []
        length = len(testInstance)-1
        for x in range(len(trainingSet)):
                dist = euclideanDistance(testInstance, trainingSet[x], length)
                distances.append((trainingSet[x], dist))
        distances.sort(key=operator.itemgetter(1))
        neighbors = []
        for x in range(k):
                neighbors.append(distances[x][0])
        return neighbors
 
def getResponse(neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
                response = neighbors[x][-1]
                if response in classVotes:
                        classVotes[response] += 1
                else:
                        classVotes[response] = 1
        print(classVotes)
        sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]
 
def getAccuracy(testSet, predictions):
        correct = 0
        for x in range(len(testSet)):
                if testSet[x][-1] == predictions[x]:
                        correct += 1
        return (correct/float(len(testSet))) * 100.0
        
def main():
        # prepare data
        trainingSet=[]
        testSet=[]
        split = 0.67
        loadDataset('c.txt', split, trainingSet, testSet)
        print('Train set: ' + repr(len(trainingSet)))
        print('Test set: ' + repr(len(testSet)))
        # generate predictions
        predictions=[]
        k = 3
        for x in range(len(testSet)):
                neighbors = getNeighbors(trainingSet, testSet[x], k)
                result = getResponse(neighbors)
                predictions.append(result)
                print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
        accuracy = getAccuracy(testSet, predictions)
        print('Accuracy: ' + repr(accuracy) + '%')


main()
