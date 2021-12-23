# Imports 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import argparse
import os, sys

# Imports personal libraries
# import pre_traitement 
# import features_engineering
# import modele

def get_args(): 
	parser = argparse.ArgumentParser(description="Script to launch jigsaw training", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_arguement("--data_path", type = str, help = "path to a folder containing all the data files") 
	parser.add_argument("--output_folder", type = str,  help = "path to an input folder where to output your model and predictions") 
	return parser.parse_args()

def main(): 
	args = get_args()
	output_folder = args.output_folder
	data_path  = args.data_path

	# Folder where to save trained model + predictions
	if not os.path.exists(output_folder):
 		os.makedirs(output_folder)

 	# Load data train: load df pré existant 

 	# Load data test 

 	# Preprocessing
 		# Normalisation 
 		# Split train / test 

 	# Model training


 	# Prediction on test 


 	# Save the model 

 	# Save the predictions

if __name__ == "__main__":
    main()