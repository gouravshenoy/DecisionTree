
# This is a class which holds the data
class Data:

    def __init__(self):
        self.__matrix = []

    def getMatrix(self):
        return self.__matrix

    def setMatrix(self, matrix):
        self.__matrix = matrix

    def getAvailableFeatures(self):
        matrix = self.__matrix
        return list(range(0,len(matrix[0])-1))

    def getFeaturesBreakDown(self):
        features = self.getAvailableFeatures()
        breakDown = []
        for datapoint in self.__matrix:
            label = datapoint[-1]
            for feature in features:
                featureValue = datapoint[feature]
                featureBreakDown = breakDown[feature]
                featureBreakDown[featureValue][label] += 1
        return breakDown

    def getDataIndices(self, featureIndex, featureValue, subsetIndices):
        indices = []

        if len(subsetIndices) == 0:
            subsetIndices = list(range(0, len(self.__matrix)))

        for dataPointIndex in subsetIndices:
            dataPoint = self.__matrix[dataPointIndex]
            if dataPoint[featureIndex] == featureValue:
                indices.append(dataPointIndex)

        return indices

class DataSubset(Data):

    __subsetIndices = []

    def addSubsetIndices(self, index):
        self.__subsetIndices.append(index)