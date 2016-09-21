import os.path


class InputHandler:
    # Function that reads the file and returns the data object
    def readFile(inputFile):
        if os.path.isfile(inputFile) == False:
            print('Invalid file path')
            return 0
        else:
            file = open(inputFile, 'r')
            lines = file.readlines()
            for line in lines:
                lineData = line.split(' ')
                label = lineData[0]
                features = lineData[1:7]