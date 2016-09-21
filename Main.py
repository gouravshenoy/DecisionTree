
import DataAnalyser
import InputHandler
import Constants
import Data
import DecisionTree

data = Data.Data()
inputHandler = InputHandler.InputHandler()
analyser = DataAnalyser.DataAnalyser()

matrix = inputHandler.readFile(Constants.INPUT_FILE_TRAIN,
                                    Constants.LABEL_INDEX,
                                    Constants.FEATURE_INDICES)

data.setMatrix(matrix)

decisionTree = DecisionTree.DecisionTree()
decisionTree.train(data, Constants.TREE_DEPTH)
decisionTree.printTree()



#TO-TEST:
#print('Matrix:')
# print(data.getMatrix())
