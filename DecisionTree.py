import  DataAnalyser

class DecisionTree:

    __rootNode = -1
    __treeDepth = -1

    def train(self, data, treeDepth):
        indices = []
        availableFeatures = data.getAvailableFeatures()

        self.__treeDepth = treeDepth
        self.__rootNode = self.createNode(data, indices, availableFeatures, 1)


    def createNode(self, data, subsetIndices, availableFeatures, nodeDepth):

        dataAnalyser = DataAnalyser.DataAnalyser()
        featureBreakDown = dataAnalyser.analyze(data, subsetIndices, availableFeatures)
        featureBreakDown = {1:{1:(5,3), 2:(5,4)}}
        feature = list(featureBreakDown.keys())[0]
        featureValues = list(featureBreakDown.get(feature).keys())

        # calculate positive and negative class ratio
        negativeCount = 0
        positiveCount = 0
        for featureValue in featureValues:
            negativeCount += featureBreakDown.get(feature).get(featureValue)[0]
            positiveCount += featureBreakDown.get(feature).get(featureValue)[1]

        positiveRatio = positiveCount/(positiveCount+negativeCount)
        negativeRatio = negativeCount/(negativeCount+positiveCount)
        node = Node(feature, positiveRatio, negativeRatio)

        childrenAvailableFeatures = availableFeatures.remove(feature)
        childrenNodeDepth = nodeDepth + 1
        if self.isTerminationCondition(childrenNodeDepth, positiveRatio, childrenAvailableFeatures) == False:
            for featureValue in featureValues:
                childSubsetIndices = data.getDataIndices(feature, featureValue, subsetIndices)
                childNode = self.createNode(data, childSubsetIndices, childrenAvailableFeatures, childrenNodeDepth)
                node.addChildren(featureValue, childNode)

        return node

    def isTerminationCondition(self, childNodeDepth, positiveRaio, childrenAvailableFeatures):
        isTerminationCondition = False

        if(positiveRaio == 1
            | positiveRaio == 0
            | childNodeDepth > self.__treeDepth
            | len(childrenAvailableFeatures) == 0):
            isTerminationCondition = True

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
        print("\n\nNode Feature: ", self.getFeatureIndex)
        if self.getChildren() != -1:
            print("\nNode Children: ")
            for node in self.getChildren():
                print(" | ", node.getFeatureIndex())

            for node in self.getChildren():
                node.printNode()