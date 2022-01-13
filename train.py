"""
Created on Mon Jan 10 15:42:23 2022

@author: NGUYEN Hai Vy
"""
import tensorflow as tf
import pandas as pd
import tensorflow.keras.models as km
import tensorflow.keras.layers as kl
import numpy as np
from numpy import loadtxt,savetxt 
import matplotlib.pyplot as plt
import logging
import argparse
from structure import RNNmodel
import os
def read_args():
    parser = argparse.ArgumentParser()
                        
    parser.add_argument("--epochs",
                        default=5,
                        type=int,
                        help="number of epochs")
    
    parser.add_argument("--batch_size",
                        default=32,
                        type=int,
                        help="batch size")
    parser.add_argument("--learning_rate",
                        default=1e-3,
                        type=float,
                        help="learning rate")
    parser.add_argument("--train_val_split",
                        default=0.2,
                        type=float,
                        help="train/ validation split")
    parser.add_argument("--data_path",
                        default="Data",
                        help="Data set directory")
    parser.add_argument("--output_folder",
                        default="Results",
                        help="Results directory")
    args = parser.parse_args()
    return args
def train_model(args):
    model=RNNmodel()
    opt = tf.keras.optimizers.Adam(learning_rate=args.learning_rate)
    model.compile(loss="mse", optimizer=opt)
    model.summary()
    epochs=args.epochs
    batch_size=args.batch_size
    lr=args.learning_rate
    logging.info(f"Number of epochs is set to be: {epochs}")
    logging.info(f"Batch-size is set to be: {batch_size}")
    logging.info(f"Learning rate is set to be: {lr}")
    logging.info(f"Loading data for training...")
    X_precip=loadtxt('./'+str(args.data_path)+'/X_precip_train.csv', delimiter=',')
    y=loadtxt('./'+str(args.data_path)+'/y_train.csv', delimiter=',')
    logging.info(f"Starting to train model...")
    history=model.fit(X_precip,y, epochs=epochs, batch_size=batch_size, validation_split = args.train_val_split, verbose=1)
    if not os.path.isdir('./'+str(args.output_folder)):
        os.mkdir('./'+str(args.output_folder))
    logging.info(f"Saving weights to the file mono_recurrent_model.h5...")
    model.save_weights('./'+str(args.output_folder)+'/mono_recurrent_model.h5')
    train_loss = history.history['loss']
    val_loss = history.history['val_loss']
    logging.info(f"Saving training and validation losses to the file loss_train_val.csv...")
    df_loss = pd.DataFrame(list(zip(range(1,len(train_loss)+1),train_loss, val_loss)), columns =['Epoch','Training_losses', 'Validation_losses'])
    #df_loss=df_loss.set_index('Epoch')
    df_loss.to_csv('./'+str(args.output_folder)+'/losses.csv',index=False)
    logging.info(f"Plotting training and validation losses to the file plot_losses.pdf...")
    plt.plot(df_loss['Epoch'],df_loss['Training_losses'],label='Training losses')
    plt.plot(df_loss['Epoch'],df_loss['Validation_losses'],label='Validation losses')
    plt.xlabel("Epoch")
    plt.ylabel("MSE")
    plt.legend()
    plt.savefig('./'+str(args.output_folder)+'/plot_losses.pdf')
    logging.info(f"Loading test data for predicting...")
    X_precip_test=loadtxt('./'+str(args.data_path)+'/X_precip_test.csv', delimiter=',')
    ### Load Id test
    id_test=pd.read_csv('./'+str(args.data_path)+'/Id_test.csv')
    logging.info(f"Predicting test set...")
    ypred=model.predict(X_precip_test)
    logging.info(f"Saving prediction to the file Prediction_Kaggle_INSA_MA.csv...")
    predframe=pd.DataFrame({'Id': id_test['Id'],'Prediction':ypred[:,0]})
    predframe.to_csv('./'+str(args.output_folder)+'/Prediction_Kaggle_INSA_MA.csv',index=False)
    
def main(args):
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    train_model(args)
    return

if __name__ == '__main__':
  args = read_args()
  main(args)
