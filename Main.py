import os
import Data
import Constants
import InputHandler
import DecisionTree

# import used for creating csv file
import csv


class Main:
    def get_train_file(self, fileIndex=1, own_file=False):
        if own_file:
            return Constants.OWN_FILE_NAME.format(purpose='train')
        else:
            return Constants.INPUT_FILE_NAME.format(index=fileIndex,
                                                    purpose='train')

    def get_test_file(self, fileIndex=1, own_file=False):
        if own_file:
            return Constants.OWN_FILE_NAME.format(purpose='test')
        else:
            return Constants.INPUT_FILE_NAME.format(index=fileIndex,
                                                    purpose='test')

    def run_monk(self):
        print ("--- DECISION TREE ALGORITHM (MONKS DATA-SET) --- ")

        # list to hold accuracies
        self.__monk_accuracies = []
        self.__avg_accuracies = {}

        # run for all train/test files
        for fileIndex in range(1, 4):
            # create new data & input-handler object
            data_train = Data.Data()
            data_test = Data.Data()
            inputHandler = InputHandler.InputHandler()

            # create dict for accuracy at depth
            accuracy_dict = {}

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
                accuracy_dict[tree_depth] = dt_accuracy

                # plot the confusion matrix for depth 1,2
                if tree_depth in [1, 2]:
                    decisionTree.plotConfusionMatrix(data_test.getMatrix(),
                                                     predicted_classes)

            # append to accuracy list
            self.__monk_accuracies.append(accuracy_dict)

        # pprint(self.__monk_accuracies)

        # average all accuracies
        for tree_depth in range(1, Constants.TREE_DEPTH):
            self.__avg_accuracies[tree_depth] = sum(d[tree_depth] for d in self.__monk_accuracies) / len(self.__monk_accuracies)

        # pprint(self.__avg_accuracies)
        self.plot_accuracy_graph()

    def run_own(self):
        print ("--- DECISION TREE ALGORITHM (OWN DATA-SET) --- ")

        # create new data & input-handler object
        data_train = Data.Data()
        data_test = Data.Data()
        inputHandler = InputHandler.InputHandler()

        # create data matrix from training file
        matrix_train = inputHandler.readFile(self.get_train_file(own_file=True),
                                             Constants.OWN_LABEL_INDEX,
                                             Constants.OWN_FEATURE_INDICES)

        # create data matrix from testing file
        matrix_test = inputHandler.readFile(self.get_test_file(own_file=True),
                                            Constants.OWN_LABEL_INDEX,
                                            Constants.OWN_FEATURE_INDICES)

        # set the data matrices in the object
        data_train.setMatrix(matrix_train)
        data_test.setMatrix(matrix_test)

        # create decision-tree object
        decisionTree = DecisionTree.DecisionTree()
        print ('{0:{fill}{align}{width}} '.format('=',
                                                  fill='=',
                                                  width=65,
                                                  align='^'))
        print ("-- Learning decision tree from file = {} ".format(os.path.basename(self.get_train_file(own_file=True))))
        print ('{0:{fill}{align}{width}} '.format('=',
                                                  fill='=',
                                                  width=65,
                                                  align='^'))

        # run for depth 1,2
        for tree_depth in range(1, 8):
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
            if tree_depth in [1, 2]:
                decisionTree.plotConfusionMatrix(data_test.getMatrix(),
                                                 predicted_classes)

        pass

    def plot_accuracy_graph(self):
        # csv library is used only for writing the csv file
        #   csv file is used for plotting graph
        with open('dt_accuracies.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Depth of Tree', 'Monk-1 Accuracy', 'Monk-2 Accuracy', 'Monk-3 Accuracy', 'Avg. Accuracy'])
            for depth, accuracy in self.__avg_accuracies.items():
                writer.writerow([depth,
                                 self.__monk_accuracies[0][depth],
                                 self.__monk_accuracies[1][depth],
                                 self.__monk_accuracies[2][depth], accuracy])
        pass

# run main function
if __name__ == '__main__':
    main_obj = Main()

    # run DT algorithm on Monks data-set
    main_obj.run_monk()

    # run DT algorithm on own data-set
    # main_obj.run_own()

