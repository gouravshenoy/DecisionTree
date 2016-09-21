
import InputHandler
import Constants
import Data

data = Data.Data()
inputHandler = InputHandler.InputHandler()

matrix = inputHandler.readFile(Constants.INPUT_FILE_TRAIN,
                                    Constants.LABEL_INDEX,
                                    Constants.FEATURE_INDICES)

data.setMatrix(matrix)
#TO-TEST:
print('Matrix:')
print(data.matrix)