
# This is a class which holds the data
class Data:

    def __init__(self):
        self.__matrix = []

    def getMatrix(self):
        return self.__matrix

    def setMatrix(self, matrix):
        self.__matrix = matrix



class DataSubset(Data):

    __subsetIndices = []

    def addSubsetIndices(self, index):
        self.__subsetIndices.append(index)