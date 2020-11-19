import numpy as np
import pandas as pd
import joblib

model = joblib.load('model/model.joblib')
pipeline = joblib.load("model/pipeline.joblib")


def preprocess(data):
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
    # Replace median values with values from form via 'for'
    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]
    df = pd.DataFrame(feature_values, index=[0])

    # Budget year ratio

    df = pipeline.transform(df)
    print(df)
    # feature_values = dict(enumerate(df.flatten(), 0))
    return df


def predict(data):
    column_order = ['belongs_to_collection', 'budget', 'original_language', 'popularity', 'production_countries',
                    'runtime', 'tagline', 'release_year', 'release_month', 'budget_year_ratio', 'all_genres']
    # data = np.array([data[feature] for feature in column_order], dtype=object)
    pred = model.predict(data.reshape(1, -1))
    print(pred)
    # uncertainty = model.predict_proba(data.reshape(1, -1))
    return pred  # , uncertainty


def postprocess(prediction):
    # pred, uncertainty = prediction
    pred = prediction
    try:
        int(pred[0]) > 0
    except ValueError:
        pass

    pred = str(pred[0])
    # uncertainty = str(uncertainty[0])
    print(prediction)
    return_dict = {'pred': pred}  # , 'uncertainty': uncertainty}
    return return_dict
