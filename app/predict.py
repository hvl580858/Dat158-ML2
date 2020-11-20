import numpy as np
import pandas as pd
import joblib

model = joblib.load('model/model.joblib')
pipeline = joblib.load("model/pipeline.joblib")

"""
Preprocess:
    This is the "cleaning" stage of the prediction. Here we put the values from the form into our preset and calculate
    budget_year_ratio which turned out to be a good predictor. 
    We then convert the dict to a pandas DataFrame and run that through our pipeline.
    Output of our pipeline is a numpy Array.
    We also grab the title from the form and remove if from the data before we start to enter the data into the 
    feature_values dict. 
    
"""


def preprocess(data):
    data.update({'budget_year_ratio': 0})

    title = data.pop('name', None)

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

    df = pd.DataFrame(feature_values, index=[0])
    df = pipeline.transform(df)

    return df, title


"""
Predict:
    This does what the name implies it will predict the revenue of the movie based on the input.
    We take the predicted revenue and increase it exponentially subtracting 1 to get it back up to a value that makes 
    sense to us. The reason for this is that it got a better prediction downscaling the labels before fitting the model,
    but that means the value it predicts will be downscaled as well.
    This last step we probably could have done in postprocess but we mad our life easy with short time remaining.
"""


def predict(data):
    pred = np.expm1(model.predict(data.reshape(1, -1)))
    return pred


"""
Postprocess: 
    Here we make the prediction into a dictionary and return it.
"""


def postprocess(pred):
    pred = str(pred[0])
    return_dict = {'pred': pred}
    return return_dict
