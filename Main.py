import os
import Data
import Constants
import InputHandler
import DecisionTree


class Main:
    def get_train_file(self, fileIndex):
        return Constants.INPUT_FILE_NAME.format(index=fileIndex,
                                                purpose='train')

    def get_test_file(self, fileIndex):
        return Constants.INPUT_FILE_NAME.format(index=fileIndex,
                                                purpose='test')

    def run(self):
        print ("--- DECISION TREE ALGORITHM --- ")

        # run for all train/test files
        for fileIndex in range(1, 4):
            # create new data & input-handler object
            data_train = Data.Data()
            data_test = Data.Data()
            inputHandler = InputHandler.InputHandler()

            # create data matrix from training file
            matrix_train = inputHandler.readFile(self.get_train_file(fileIndex),
                                                 Constants.LABEL_INDEX,
                                                 Constants.FEATURE_INDICES)

            # create data matrix from testing file
            matrix_test = inputHandler.readFile(self.get_test_file(fileIndex),
                                                 Constants.LABEL_INDEX,
                                                 Constants.FEATURE_INDICES)

            # set the data matrices in the object
            data_train.setMatrix(matrix_train)
            data_test.setMatrix(matrix_test)

            # create decision-tree object
            decisionTree = DecisionTree.DecisionTree()
            print ('{0:{fill}{align}{width}} '.format('=',
                                                      fill='=',
                                                      width=65,
                                                      align='^'))
            print ("-- Learning decision tree from file = {} ".format(os.path.basename(self.get_train_file(fileIndex))))
            print ('{0:{fill}{align}{width}} '.format('=',
                                                      fill='=',
                                                      width=65,
                                                      align='^'))

            # run for max-depth times
            for tree_depth in range(1, Constants.TREE_DEPTH):
                print ("\n- Tree Depth = {}".format(tree_depth))

                ''' ~~ Training Phase ~~ '''
                # run the decision-tree training algorithm
                decisionTree.train(data_train, treeDepth=tree_depth)

                # optional - print the generated tree
                # decisionTree.printTree()

                ''' ~~ Testing Phase ~~ '''
                # get prediction accuracy from trained model
                predicted_classes = decisionTree.test(data_test.getMatrix())

                # calculate accuracy of model
                dt_accuracy = decisionTree.calculateAccuracy(data_test.getMatrix(),
                                                             predicted_classes)
                print('- Accuracy of model = {}'.format(dt_accuracy))

                # plot the confusion matrix for depth 1,2
                if tree_depth in [1,2]:
                    decisionTree.plotConfusionMatrix(data_test.getMatrix(),
                                                     predicted_classes)

# run main function
if __name__ == '__main__':

    main_obj = Main()
    main_obj.run()