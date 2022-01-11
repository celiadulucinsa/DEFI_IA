#download forecast data
mkdir data_meteonet
mkdir data_meteonet/train
mkdir data_meteonet/train/X_forecast
mkdir data_meteonet/train/X_forecast/2D_arpege_train
mkdir data_meteonet/train/X_forecast/2D_arome_train
mkdir data_meteonet/train/X_forecast/3D_arpege_train

#pour 2D_arpege_train
wget https://meteonet.umr-cnrm.fr/dataset/data/defi_ia_challenge/train/X_forecast/2016/2D_arpege_2016.tar.gz
wget https://meteonet.umr-cnrm.fr/dataset/data/defi_ia_challenge/train/X_forecast/2017/2D_arpege_2017.tar.gz

tar -xf ./2D_arpege_2016.tar.gz 
tar -xf ./2D_arpege_2017.tar.gz 

mv ./2D_arpege_2016/* ./data_meteonet/train/X_forecast/2D_arpege_train
mv ./2D_arpege_2017/* ./data_meteonet/train/X_forecast/2D_arpege_train

rm -r ./2D_arpege_2016
rm -r ./2D_arpege_2017

#pour 3D_arpege_train
wget https://meteonet.umr-cnrm.fr/dataset/data/defi_ia_challenge/train/X_forecast/2016/3D_arpege_2016.tar.gz
wget https://meteonet.umr-cnrm.fr/dataset/data/defi_ia_challenge/train/X_forecast/2017/3D_arpege_2017.tar.gz

tar -xf ./3D_arpege_2016.tar.gz 
tar -xf ./3D_arpege_2017.tar.gz 

mv ./3D_arpege_2016/* ./data_meteonet/train/X_forecast/3D_arpege_train
mv ./3D_arpege_2017/* ./data_meteonet/train/X_forecast/3D_arpege_train

rm -r ./3D_arpege_2016
rm -r ./3D_arpege_2017


#pour 2D_arome_train
wget https://meteonet.umr-cnrm.fr/dataset/data/defi_ia_challenge/train/X_forecast/2016/2D_arome_2016.tar.gz
wget https://meteonet.umr-cnrm.fr/dataset/data/defi_ia_challenge/train/X_forecast/2017/2D_arome_2017.tar.gz

tar -xf ./2D_arome_2016.tar.gz 
tar -xf ./2D_arome_2017.tar.gz 

mv ./2D_arome_2016/* ./data_meteonet/train/X_forecast/2D_arome_train
mv ./2D_arome_2017/* ./data_meteonet/train/X_forecast/2D_arome_train

rm -r ./2D_arome_2016
rm -r ./2D_arome_2017



# test
mkdir data_meteonet/test
mkdir data_meteonet/test/3D_arpege
mkdir data_meteonet/test/2D_arpege
mkdir data_meteonet/test/2D_arome

# pour 2D_arome_test
wget https://meteonet.umr-cnrm.fr/dataset/data/defi_ia_challenge/test/X_forecast/2D_arome_test.tar.gz

tar -xf ./2D_arome_test.tar.gz

mv ./2D_arome_test/* ./data_meteonet/test/2D_arome

rm -r ./2D_arome_test

# pour 2D_arpege_test
wget https://meteonet.umr-cnrm.fr/dataset/data/defi_ia_challenge/test/X_forecast/2D_arpege_test.tar.gz

tar -xf ./2D_arpege_test.tar.gz

mv ./2D_arpege_test/* ./data_meteonet/test/2D_arpege

rm -r ./2D_arpege_test

# pour 3D_arpege_test
wget https://meteonet.umr-cnrm.fr/dataset/data/defi_ia_challenge/test/X_forecast/3D_arpege_test.tar.gz

tar -xf ./3D_arpege_test.tar.gz

mv ./3D_arpege_test/* ./data_meteonet/test/3D_arpege

rm -r ./3D_arpege_test


#download X_station
mkdir data_station




