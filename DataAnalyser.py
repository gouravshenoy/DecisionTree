import math
import Constants

from pprint import pprint

class DataAnalyser:

    def analyseInfoGain(self, dataSet, filterIndex=[], availableFeatures=[]):
        for index, data in enumerate(dataSet.getMatrix()):
            print '{index}, {list}'.format(index=index, list=data)

        # if no filterIndex, scan full dataSet,
        #   else, create filtered dataSet
        filtered_data = dataSet.getMatrix()
        if filterIndex:
            filtered_data = [dataSet.getMatrix()[i] for i in filterIndex]

        # this data-structure holds vital information
        #   about the features, incl pos,neg counts
        featureDict = {}
        for feature in availableFeatures:
            featureDict[feature] = {}
            for index, data in enumerate(filtered_data):
                label_index = len(data) - 1
                if data[feature] in featureDict[feature]:
                    featureDict[feature][data[feature]][data[label_index]] += 1
                else:
                    featureDict[feature][data[feature]] = [0,0]

        pprint(featureDict)
        return


    def calculateEntropy(self, posCount=0, negCount=0):
        p_pos = float(posCount) / (posCount + negCount)
        p_neg = float(negCount) / (posCount + negCount)
        entropy = -(p_pos * math.log(p_pos, 2)) - (p_neg * math.log(p_neg, 2))
        return entropy
