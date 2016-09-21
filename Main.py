
import InputHandler
import Constants
import Data

data = Data.Data()
inputHandler = InputHandler.InputHandler()

data.matrix = inputHandler.readFile(Constants.INPUT_FILE_TRAIN,
                                    Constants.LABEL_INDEX,
                                    Constants.FEATURE_INDICES)

#TO-TEST:
print('Matrix:')
print(data.matrix)