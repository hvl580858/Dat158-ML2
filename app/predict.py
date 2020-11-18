import numpy as np
import pandas as pd
import joblib


# model = joblib.load('models/dat158-ml2-model.joblib')


def preprocess(data):
    feature_values = {
        'belongs_to_collection': NaN,
        'budget': 2.266000e+07,
        'popularity': 8.47,
        'runtime': 107.9,
        'tagline': "likely having a tagline",

        'release_year': 1999.675233,
        'release_month': 6.889015,
        'budget_year_ratio': 0.358572,

        'homepage': 0.677126,
        'original_language': 11.454297,
    }
    # Replace median values with values from form via 'for'
    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]

    return feature_values


def predict(data):
    column_order = []
    #data = np.array([data[feature] for feature in column_order], dtype=object)
    # pred = model.predict(data.reshape(1, -1))
    # uncertainty = model.predict_proba(data.reshape(1, -1))
    return data


def postprocess(prediction):
    pred, uncertainty = prediction
    try:
        int(pred[0]) > 0
    except ValueError:
        pass

    pred = str(pred[0])
    uncertainty = str(uncertainty[0])

    return_dict = {'pred': pred, 'uncertainty': uncertainty}
    return return_dict
