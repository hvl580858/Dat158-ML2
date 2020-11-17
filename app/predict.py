import numpy as np
import pandas as pd
import joblib


# model = joblib.load('models/dat158-ml2-model.joblib')


def preprocess(data):
    feature_values = {
        'belongs_to_collection': 0.800591,
        'budget': 2.264929e+07,
        'homepage': 0.677126,
        'original_language': 11.454297,
        'popularity': 8.550230,
        'runtime': 107.622212,
        'tagline': 0.196226,
        'release_year': 1999.675233,
        'release_month': 6.889015,
        'Comedy': 0.358572,
        'director_Martin Scorsese': 0.003667,
        'director_Paul W.S.Anderson': 0.002667,
        'director_Alfred Hitchcock': 0.002667,
        'director_Michael Bay': 0.004333,
        'director_Francis Ford Coppola': 0.00600,
        'director_Brian De Palma': 0.002667,
        'director_Steven Soderbergh': 0.005000,
        'director_Joel Schumacher': 0.002667,
        'director_Peter Hyams': 0.003000,
        'title_length': 15.127873
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
