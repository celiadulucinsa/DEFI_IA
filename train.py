# Imports 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import argparse
import os, sys

# Imports personal libraries
# import pre_traitement 
# import features_engineering
from utils import training 
from utils import prediction
from utils import preprocessing

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
	
	if args.preprocessing: #option1
		df_train, df_X_test = preprocessing.preprocessing()

 	else: #option2
		df_train = pd.read_csv("df_train.csv")  ##### quand ces excels ok -> mettre les bons noms sur le drive + mettre bons liens dans readme
		df_X_test = pd.read_csv("df_X_test.csv") 


	X_train = df_train.drop(["Ground_truth", "Id", "number_sta", "date"], axis = 1)
	X_test =  df_X_test.drop(["number_sta", "date"], axis = 1)
	y_train = df_train["Ground_truth"]
	
	# Normalisation 

 	# Model training
	model_trained = training.main(X_train, y_train) 
	
	# Prediction on test + save 
	filename = output_folder + "/submission.csv"
	submit = prediction.prediction(model_trained, X_test, filename)

 	# Save the model 
	model_trained.save(output_folder + '/model.h5')


if __name__ == "__main__":
    main()
