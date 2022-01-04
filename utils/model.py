import tensorflow
from tensorflow import keras
import keras.backend as K


def MAPELoss(y_true, y_pred): 
  m = 100 * K.mean(K.abs((y_true - y_pred) / (y_true+1)), axis=-1)
  return m 

def get_model(shape,n_layers,n_neurons): 
    
    # shape : nb de variables explicatives 
    # n_layers : nb de couches
    # n_neurons : neurons/ couche
   
    model = keras.models.Sequential()
    model.add(keras.layers.Input(shape))
    
    for i in range(n_layers): 
            model.add(keras.layers.Dense(n_neurons, activation='relu'))
   
    model.add(keras.layers.Dense(1, name='Output'))
    model.compile(optimizer = 'adam', 
                  loss      = MAPELoss,
                  metrics   = ['mae', 'mse', MAPELoss] )
    return model
    
# Init du modèle
def init_model(shape, n_layers = 20, n_neurons = 32): 
    model_reg_nn = get_model(shape, n_layers, n_neurons)
    return model_reg_nn
    

    
