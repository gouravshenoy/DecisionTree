import os.path

class InputHandler:

    # Function that reads the file and returns the data matrix
    def readFile(self, inputFile, labelIndex, featureIndices):
        if os.path.isfile(inputFile) == False:
            print('Invalid file path')
            return 0
        else:
            file = open(inputFile, 'r')
            lines = file.readlines()
            featureMatrix = []
            for line in lines:
                lineData = line.split(' ')
                label = lineData[labelIndex]
                features = lineData[featureIndices[0]:featureIndices[1]]
                features.append(label)
                featureMatrix.append(features)
            return featureMatrix
