
import DataAnalyser
import InputHandler
import Constants
import Data

data = Data.Data()
inputHandler = InputHandler.InputHandler()
analyser = DataAnalyser.DataAnalyser()

matrix = inputHandler.readFile(Constants.INPUT_FILE_TRAIN,
                                    Constants.LABEL_INDEX,
                                    Constants.FEATURE_INDICES)

data.setMatrix(matrix)
#TO-TEST:
print('Matrix:')
# print(data.getMatrix())
analyser.analyseInfoGain(dataSet=data, filterIndex=[0,2,5,7])