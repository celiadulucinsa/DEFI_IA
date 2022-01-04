# Imports 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import argparse
import os, sys

# Imports personal libraries
# import pre_traitement 
# import features_engineering
import training 
import prediction

def get_args(): 
	parser = argparse.ArgumentParser(description="Script to launch defi-ia training", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_arguement("--data_path", type = str, help = "path to a folder containing all the data files") 
	parser.add_argument("--output_folder", type = str,  help = "path to an input folder where to output your model and predictions") 
	parser.add_argument("--preprocessing", type = bool, help = "if false, preprocessed dataset is downloaded") 
	return parser.parse_args()

def main(): 
	args = get_args()
	output_folder = args.output_folder
	data_path  = args.data_path

	# Folder where to save trained model + predictions
	if not os.path.exists(output_folder):
 		os.makedirs(output_folder)
	
	if args.preprocessing: 
		# fonction qui télécharge données X_station 
		# from preprocessing to fill values by missforest
 	else: 
		input_folder = "inputs"
		if not os.path.exists(input_folder):
 			os.makedirs(input_folder)
		# Load data train: load df pré existant 
		X_train = pd.read_csv(input_folder + "/X_train.csv")  
	

 		# Load data test 

	# Preprocessing
	# Normalisation 
	# Split train / test 

 	# Model training
	model_trained = training.main(X_train, y_train) 
	
	# Prediction on test + save 
	filename = output_folder + "/submission.csv"
	submit = prediction(model_trained, X_test, filename)

 	# Save the model 
	model_trained.save(output_folder + '/model.h5')


if __name__ == "__main__":
    main()
