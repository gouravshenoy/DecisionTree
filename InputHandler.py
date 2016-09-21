import os.path

class InputHandler:

    def convertToInteger(self, numberString):
        """
        This function checks if input is number and if yes then convert it into integer.
        :param numberString:
            Number string to convert into integer
        :return:
            Converted integer if string is digit else the same string
        """
        if numberString.isdigit():
            numberString = int(numberString)

        return numberString

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
                lineData = [ self.convertToInteger(x) for x in line.split(' ')]
                label = lineData[labelIndex]
                features = lineData[featureIndices[0]:featureIndices[1]]
                features.append(label)
                featureMatrix.append(features)
            return featureMatrix
