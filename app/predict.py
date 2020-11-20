import numpy as np
import pandas as pd
import joblib

model = joblib.load('../model/model.joblib')
pipeline = joblib.load("../model/pipeline.joblib")


def preprocess(data):
    data.update({'budget_year_ratio': 0})

    name = data.pop('name', None)

    feature_values = {
        'belongs_to_collection': 1,
        'budget': 2.266000e+07,
        'original_language': 7,
        'popularity': 8.47,
        'production_countries': 275,
        'runtime': 107.9,
        'tagline': 0,
        'release_year': 2000,
        'release_month': 7,
        'budget_year_ratio': 3.448084773627077,
        'all_genres': 435,

    }

    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]

    # Budget year ratio
    budget = 1
    year = 1
    for key in feature_values.keys():
        if key == 'budget':
            budget = data[key]
        if key == 'release_year':
            if feature_values[key] <= 1930:
                feature_values[key] = 1930
            year = data[key]
        if key == 'budget_year_ratio':
            if budget > 0:
                feature_values[key] = budget / (year * year)
            print(feature_values[key])

    df = pd.DataFrame(feature_values, index=[0])
    df = pipeline.transform(df)

    return df, name


def predict(data):
    pred = np.expm1(model.predict(data.reshape(1, -1)))

    return pred


def postprocess(pred):
    try:
        int(pred[0]) > 0
    except ValueError:
        pass

    pred = str(pred[0])
    return_dict = {'pred': pred}
    return return_dict
