# Imports 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import argparse
import os, sys

def get_args(): 
	parser = argparse.ArgumentParser(description="Script to launch jigsaw training", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_arguement("--data_path", type = str, help = "path to a folder containing all the data files") 
	parser.add_argument("--output_folder", type = str,  help = "path to an input folder where to output your model and predictions") 
	return parser.parse_args()

def main(): 
	args = get_args()

if __name__ == "__main__":
    main()