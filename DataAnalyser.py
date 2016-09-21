import math
import Constants
from collections import Counter

from pprint import pprint

class DataAnalyser:

    def analyseFeatures(self, dataSet, filterIndex=[], availableFeatures=[]):
        # for index, data in enumerate(dataSet.getMatrix()):
        #     print '{index}, {list}'.format(index=index, list=data)

        # if no filterIndex, scan full dataSet,
        #   else, create filtered dataSet
        filtered_data = dataSet.getMatrix()
        if filterIndex:
            filtered_data = [dataSet.getMatrix()[i] for i in filterIndex]

        # this data-structure holds vital information
        #   about the features, incl pos,neg counts
        featureDict = {}
        filteredLabels = []

        for feature in availableFeatures:
            featureDict[feature] = {}
            for index, data in enumerate(filtered_data):
                label_index = len(data) - 1

                if data[feature] in featureDict[feature]:
                    featureDict[feature][data[feature]][data[label_index]] += 1
                else:
                    featureDict[feature][data[feature]] = [0,0]
                    featureDict[feature][data[feature]][data[label_index]] += 1

        featureDict = self.calculateInfoGain(featureDict=featureDict)
        pprint(featureDict)

        # find the feature with max
        #   information gain
        max_gain = 0.0
        for key, value in featureDict.iteritems():
            if value['info-gain'] > max_gain:
                max_gain = value['info-gain']
                max_gain_feature = key

        return {max_gain_feature: featureDict[max_gain_feature]}

    def calculateInfoGain(self, featureDict):

        for featureIndex, dict in featureDict.iteritems():
            total_pos_count = 0
            total_neg_count = 0
            for featureValue, featureCounts in dict.iteritems():
                total_pos_count += featureCounts[True.__int__()]
                total_neg_count += featureCounts[False.__int__()]

            # print total_pos_count, total_neg_count
            parent_entropy = self.calculateEntropy(total_pos_count, total_neg_count)
            # print parent_entropy

            sum_feature_entropy = 0.0
            for featureValue, featureCounts in dict.iteritems():
                # norm_prob = |Sv| / |S|
                norm_prob = float(sum(featureCounts)) / (total_pos_count + total_neg_count)

                # we calculate sum of entropies
                #   of all feature values
                sum_feature_entropy += (norm_prob) * \
                                    self.calculateEntropy(featureCounts[True.__int__()],
                                                          featureCounts[False.__int__()])

            # subtract parent entropy from
            #   sum of feature entropies to get info-gain
            dict['info-gain'] = parent_entropy - sum_feature_entropy
            featureDict[featureIndex] = dict

        # pprint(featureDict)
        return featureDict


    def calculateEntropy(self, posCount=0, negCount=0):
        # if either count is 0,
        #   then entropy is 0
        if posCount>0 and negCount>0:
            p_pos = float(posCount) / (posCount + negCount)
            p_neg = float(negCount) / (posCount + negCount)
            entropy = -(p_pos * math.log(p_pos, 2)) - (p_neg * math.log(p_neg, 2))
        else:
            entropy = 0
        return entropy
