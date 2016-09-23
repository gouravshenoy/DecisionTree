import os.path

class InputHandler:
    """
    This is InputHandler class responsible for reading inputs to the program
    """

    def convertToInteger(self, numberString):
        """
        This function checks if input is number and if yes then convert it into integer.
        :param numberString:
            Number string to convert into integer
        :return:
            Converted integer if string is digit else the same string
        """
        try:
            numberString = float(numberString)
            numberString = int(numberString)
        except ValueError:
            pass

        return numberString


    def readFile(self, inputFile, labelIndex, featureIndices):
        """
        This function reads the input file to the program and generate the data matrix for the program.

        :param inputFile: path to input file
        :param labelIndex: index of class label column in the data
        :param featureIndices: indices of the feature columns in the data
        :return: data matrix with in format [[feature1, feature2, .., classlabel],..]
        """
        if os.path.isfile(inputFile) == False:
            print('Invalid file path')
            return 0
        else:
            file = open(inputFile, 'r')
            lines = file.readlines()
            featureMatrix = []
            for line in lines:
                lineData = [ self.convertToInteger(x) for x in line.rstrip('\n').split(' ')]
                label = lineData[labelIndex]
                features = lineData[featureIndices[0]:featureIndices[1]]
                features.append(label)
                featureMatrix.append(features)
            return featureMatrix
