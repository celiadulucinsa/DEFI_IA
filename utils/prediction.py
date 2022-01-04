import pandas as pd
import tensorflow
from tensorflow import keras

def prediction(model, X_test, filename): 

    y_pred = model.predict(X_test.drop(["number_sta", "Id", "date"], axis = 1))
    y_pred  = pd.DataFrame(y_pred)
    
    # Création dataframe submit 
    df_submit = X_test["Id"].to_frame()
    df_submit["Prediction"] = y_pred

    # On met toutes les prédictions négatives à 0 + ajout de 1
    df_submit["Prediction"] = df_submit.Prediction.apply(lambda x : max(0,x) + 1)

    # Export csv 
    df_submit.to_csv(filename, index = False)
    
    return df_submit
    
    
