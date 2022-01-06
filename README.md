# Defi-IA-2022
Défi IA 2022 (Kaggle)

<p align="center" href="https://www.kaggle.com/c/defi-ia-2022">
  <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Kaggle_logo.png" width="120" alt="Kaggle">
</p>


Team: STEC

Members: Célia Duluc, Thomas Nivelet, Elisa Escanez, Sébastien Castets

INSA Toulouse - 5th year (Applied Mathematics)

Objective: Predict the accumulated daily rainfall on the D day on the observation ground stations.


## Download data

- Option 1 : download all the data on your computer. Warning : data size of 80Gb and time consuming!
- Option 2 : download the final dataset with all the preprocessing already done. 

### Option 1
- Run the download_data.sh 

```
sh download_data.sh
```
- Go on Kaggle website -> profile -> Account -> Create New API Token
- Move the kaggle.json into the data_station folder
- Run the command:

```
kaggle competitions download -c defi-ia-2022
```
- Unzip the kaggle data running :
```
sh unzip_data.sh
```
### Option 2

- Download the csv files following these links in the current folder
```
https://drive.google.com/file/d/1UFRhVIOeXBG0N-5KFDnzRbrnmJhPbCKY/view?usp=sharing
lien2
```
## Train the model and get the predictions

- Run the train.py, with the following arguments: 
  - data_path = './data_station/', 
  - output_folder: an output folder, where you will get the predictions,
  - preprocessing:
    - *Option 1 (if you have downloaded all the data on your computer):* preprocessing = TRUE
      ```
      python train.py --data_path = './data_station' --output_folder = <OUTPUT_FOLDER> --preprocessing = TRUE
      ```
    - *Option 2 (if you have downloaded the final dataset with the preprocessing already done):* preprocessing = FALSE
      ```
      python train.py --data_path = './data_station' --output_folder = <OUTPUT_FOLDER> --preprocessing = FALSE
      ```

