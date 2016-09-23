## This file holds the constants and input parameters to the program

# import for drawing tree (Optional: Needed only if you wish to visualize the tree)
#import pydot

# Path format of monk input data files to the program
INPUT_FILE_NAME = "/home/anwar/AML-PA-1/raw_data/monks-{index}.{purpose}"
#INPUT_FILE_NAME = "/Users/goshenoy/SOIC-Courses/Applied-ML/PA1/monks-{index}.{purpose}.txt"

# Path format of own input data files to the program
OWN_FILE_NAME = "/home/anwar/AML-PA-1/raw_data/mammographic-masses-{purpose}.txt"
#OWN_FILE_NAME = "/Users/goshenoy/SOIC-Courses/Applied-ML/PA1/mammographic-masses-{purpose}.txt"

# Output result file from the program
RESULT_FILE = "dt_accuracies.csv"




# Index of the class label in monk data
LABEL_INDEX = 1

# Index of the class label in own data
OWN_LABEL_INDEX = 0

# Indices of features in the monk data
FEATURE_INDICES = (2,8)

# Indices of features in the own data
OWN_FEATURE_INDICES = (1, 7)

# Desired max depth of the tree
TREE_DEPTH = 10

# Optional (Needed only if you wish to visualize the tree)
#GRAPH = pydot.Dot(graph_type='graph')