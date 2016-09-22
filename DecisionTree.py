import  DataAnalyser
from pprint import pprint


class DecisionTree:

    __rootNode = -1
    __treeDepth = -1

    def train(self, data, treeDepth):
        indices = []
        availableFeatures = data.getAvailableFeatures()

        self.__treeDepth = treeDepth
        self.__rootNode = self.createNode(data, indices, availableFeatures, 1)


    def createNode(self, data, subsetIndices, availableFeatures, nodeDepth, positiveCount =-1, negativeCount=-1):

        dataAnalyser = DataAnalyser.DataAnalyser()
        print("\nNode Data--")
        print("Subset Indices: ", subsetIndices)
        print("Available Features: ", availableFeatures)

        # Check if the node has pure class
        if (positiveCount == 0 or negativeCount == 0):
            # Creating a pure class leaf node and return
            positiveRatio = positiveCount / (positiveCount + negativeCount)
            negativeRatio = negativeCount / (negativeCount + positiveCount)
            node = Node(-1, positiveRatio, negativeRatio, nodeDepth)
            return node

        # If node is not pure get the feature breakdown from analyzer
        featureBreakDown = dataAnalyser.analyseFeatures(data, subsetIndices, availableFeatures)
        print("Feature Breakdown from Analyzer: ")
        pprint(featureBreakDown)
        feature = list(featureBreakDown.keys())[0]
        featureValues = list(featureBreakDown.get(feature).keys())
        featureValues.remove('info-gain')

        #print("FeatureValue: " , featureValues)

        # calculate positive and negative class ratio at the node
        if(positiveCount == -1 or negativeCount == -1):
            negativeCount = 0
            positiveCount = 0
            for featureValue in featureValues:
                negativeCount += featureBreakDown.get(feature).get(featureValue)[0]
                positiveCount += featureBreakDown.get(feature).get(featureValue)[1]

        positiveRatio = float(positiveCount)/(positiveCount+negativeCount)
        negativeRatio = float(negativeCount)/(negativeCount+positiveCount)

        print (positiveRatio)
        print (negativeRatio)
        # Create a new node
        node = Node(feature, positiveRatio, negativeRatio, nodeDepth)


        # Create branches and child nodes for each possible value feature can take
        childrenAvailableFeatures = list(availableFeatures)
        childrenAvailableFeatures.remove(feature)
        childrenNodeDepth = nodeDepth + 1
        if self.isTerminationCondition(childrenNodeDepth, positiveRatio, childrenAvailableFeatures) == False:
            for featureValue in featureValues:
                childSubsetIndices = data.getDataIndices(feature, featureValue, subsetIndices)
                childNode = self.createNode(data, childSubsetIndices,
                                            childrenAvailableFeatures, childrenNodeDepth,
                                            featureBreakDown.get(feature).get(featureValue)[1],
                                            featureBreakDown.get(feature).get(featureValue)[0])
                node.addChildren(featureValue, childNode)

        return node

    def isTerminationCondition(self, childNodeDepth, positiveRatio, childrenAvailableFeatures):
        isTerminationCondition = False
        if(positiveRatio == 1
            or positiveRatio == 0
            or childNodeDepth > self.__treeDepth
            or not childrenAvailableFeatures):
            isTerminationCondition = True

        #print('Is Terminated: ', isTerminationCondition)
        return isTerminationCondition

    def test(self, data):
        rootNode = self.__rootNode
        predictedLabel = []

        for dataPoint in data:
            currentNode = rootNode
            while(currentNode.getChildren() != -1):
                featureToTest = currentNode.getFeatureIndex()
                dataPointValue = dataPoint[featureToTest]
                children = currentNode.getChildren()
                currentNode = children[dataPointValue]

            predictedLabel.append(currentNode.getClassLabel())
        return predictedLabel

    def printTree(self):
        print('\n****Printing decision Tree-***')
        self.__rootNode.printNode()

class Node:
    __featureIndex = -1
    __children =  {}
    __positiveRatio = 0
    __negativeRatio = 0
    __nodeDepth = -1

    def __init__(self, feature, positiveRatio, negativeRatio, nodeDepth):
        self.__featureIndex = feature
        self.__positiveRatio = positiveRatio
        self.__negativeRatio = negativeRatio
        self.__nodeDepth = nodeDepth
        self.__children = -1

    def addChildren(self, featureValue, childNode):
        if self.__children == -1:
            self.__children = {}

        self.__children[featureValue] = childNode

    def getPositiveRatio(self):
        return self.__positiveRatio

    def negativeRatio(self):
        return self.__negativeRatio

    def getNodeDepth(self):
        return self.__nodeDepth

    def getChildren(self):
        return self.__children

    def getFeatureIndex(self):
        return self.__featureIndex

    def getClassLabel(self):
        if self.__positiveRatio > self.__negativeRatio:
            return 1
        else:
            return 0

    def printNode(self):
        print("\n\nNode Feature:", self.getFeatureIndex(), "| ClassLabel:", self.getClassLabel())
        if self.getChildren() != -1:
            print("Node Children: ")
            for branchValue in self.getChildren():
                #print("Node-",node)
                print("Child:: Branch-value:", branchValue,
                      " | Feature:", self.getChildren()[branchValue].getFeatureIndex())

            for node in self.getChildren().values():
                node.printNode()
        else:
            print("NO CHILD")