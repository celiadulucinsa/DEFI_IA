# AIF
├── __report_INSA_MA__: report of our project  
├── __Data__: all the data are stored in this folder   
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;├── __X_precip_train.csv__ Each row contains 24 values corresponding to 24 hours of day D-1   
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;├── __y_train.csv__ Each row contains 1 value corresponding to cumulative rainfall of day D   
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;├── __X_precip_test.csv__ Similar to __X_precip_train.csv__  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;└── __Id_test.csv__ containing the Id's of test set in the order of __X_precip_test.csv__   
├── __structure.py__: defining the architecture of the neural net     
└── __train.py__: training model and predicting for test set. All the results of training and testing are saved to output_folder (= Results by default) 
### Preliminary step: set up virtual environment to work with python
Create a virtual environment:
```
conda create --name AIF python==3.7.12 -c conda-forge
```
Notice that the environment here is named AIF, you can choose a name at your convenience.

To work in this environment, we need to activate it: 
```
conda activate AIF
```
Now this environment is empty. We load packages/libraries necessary for our project:
```
pip install -r requirements.txt
```
### Training and predicting
```
python train.py --data_path=<PATH_TO_YOUR_DATA_FOLDER> --output_folder=<PATH_TO_OUTPUT_FOLDER> --epochs=<NUMBER_OF_EPOCHS> --batch_size=<BATCH_SIZE> --learning_rate=<LEARNING_RATE> --train_val_split=<RATIO>
```
By default, we have:
- data_path=Data
- output_folder=Results
- epochs=5
- batch_size=32
- learning_rate=1e-3
- train_val_split=0.2

So, normally, for executing the file train.py, once you in the virtual environment, you just need to type in the terminal:
```
python train.py
```
After execution of this file, it will create output_folder (=Results by default). In this folder, we have following files created:
- mono_recurrent_model.h5: containing weights after training
- losses.csv: containing losses of training and validation set over epochs.
- plot_losses.pdf: containg the plot of training and validation losses
- Prediction_Kaggle_INSA_MA.csv: the file in good format to be submit on Kaggle

If you do not want to use a parameter as default, for example, epochs:
```
python train.py --epochs=10
```
