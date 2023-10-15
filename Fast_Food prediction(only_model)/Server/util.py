import joblib
import pandas as pd
import numpy as np

model=joblib.load('model_joblib')
compare_df=pd.read_csv('compare.csv')


def predict_item(calories, fat, sugar, protein):
    l = np.zeros(4)
    l[0] = calories
    l[1] = fat
    l[2] = sugar
    l[3] = protein
    result_n = model.predict([l])
    result = compare_df[compare_df.n_item == result_n[0]].Item[:1]
    return result.values[0]


if __name__=="__main__":
    print(predict_item(1,2,3,4))