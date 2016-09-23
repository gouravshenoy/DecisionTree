## This file holds the constants and input parameters to the program

# import for drawing tree (optional)
import pydot

# Input file to train the data
# INPUT_FILE_NAME = "/home/anwar/AML-PA-1/raw_data/monks-{index}.{purpose}"
# OWN_FILE_NAME = "/home/anwar/AML-PA-1/raw_data/mammographic-masses-{purpose}.txt"
RESULT_FILE = "dt_accuracies.csv"

INPUT_FILE_NAME = "/Users/goshenoy/SOIC-Courses/Applied-ML/PA1/monks-{index}.{purpose}.txt"
OWN_FILE_NAME = "/Users/goshenoy/SOIC-Courses/Applied-ML/PA1/mammographic-masses-{purpose}.txt"

LABEL_INDEX = 1
OWN_LABEL_INDEX = 0
FEATURE_INDICES = (2,8)
OWN_FEATURE_INDICES = (1, 7)
TREE_DEPTH = 10

GRAPH = pydot.Dot(graph_type='graph')