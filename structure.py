###  Created by NGUYEN Hai Vy
import tensorflow as tf
import tensorflow.keras.models as km
import tensorflow.keras.layers as kl
def RNNmodel():    
    model3 = km.Sequential()
    model3.add(kl.Dense(units=48 ,activation="relu", input_shape=(24,)))
    model3.add(kl.Dense(units=24 ,activation="relu"))
    model3.add(kl.Reshape((24,1),input_shape=(24,)))
    model3.add(kl.GRU(units=20, activation="relu", input_shape=(24, 1),return_sequences=True))
    model3.add(kl.Bidirectional(kl.GRU(units=20 ,activation="relu")))
    model3.add(kl.Dense(units=20 ,activation="relu"))
    model3.add(kl.Dense(1))
    return model3

