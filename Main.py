
import InputHandler
import Constants
import Data
import DecisionTree

data = Data.Data()
inputHandler = InputHandler.InputHandler()

matrix = inputHandler.readFile(Constants.INPUT_FILE_TRAIN,
                                    Constants.LABEL_INDEX,
                                    Constants.FEATURE_INDICES)

data.setMatrix(matrix)

decisionTree = DecisionTree.DecisionTree()
decisionTree.train(data, Constants.TREE_DEPTH)
# decisionTree.printTree()

#### TEST PHASE ####
ih = InputHandler.InputHandler()
data_t = Data.Data()
matrix_t = ih.readFile(Constants.INPUT_FILE_TEST,
                                    Constants.LABEL_INDEX,
                                    Constants.FEATURE_INDICES)

data_t.setMatrix(matrix_t)
classes = decisionTree.test(data_t.getMatrix())

accuracy = decisionTree.calculateAccuracy(data_t.getMatrix(), classes)
print('Accuracy = {}'.format(accuracy))
decisionTree.plotConfusionMatrix(data_t.getMatrix(), classes)


#TO-TEST:
#print('Matrix:')
# print(data.getMatrix())
