import os
import pdb
# from readline import replace_history_item
from bardapi import Bard
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
from keras.models import load_model
from pyparsing import replace_with
from xgboost import XGBRegressor
from pandas import DataFrame

app = Flask(__name__)
CORS(app)

os.environ['_BARD_API_KEY'] = 'XQioAemGhqCVyyCpevEoko2VYuzou8Xg5W2b_STl-gHHbQDmw1_11LhQwF2eCyHw9u9QdA.'

def preprocess(input_data):
    # Load your trained OneHotEncoder
    encoder = joblib.load(r'C:\Users\Hursh Shah\Documents\GitHub\HackerBytes-2\flask-server\encoder.joblib')

    # Replace the values based on the replace_dict
    replace_dict = {
        'None': 0,
        'Yes': 1,
        'No': 0,
        'Partial': 0.5,
        'Very Low': 0,
        'Low': 1,
        'Medium-Low': 2,
        'Medium': 3,
        'Medium-High': 4,
        'High': 5,
        'Very High': 6
    }

    # if isinstance(input_data, dict):
    #     # Convert dictionary to DataFrame
    #     input_data = pdb.DataFrame([input_data])

    for column in input_data.columns:
        if input_data[column].dtype == 'object' and column != 'materials':
            input_data[column] = input_data[column].replace(replace_dict)

    # Encode the materials
    input_data_encoded = encoder.transform(input_data['materials'].reshape(-1, 1))

    return input_data_encoded

def map_prediction_to_string(prediction):
    reverse_replace_dict = {
        0: 'Very Low',
        1: 'Low',
        2: 'Medium-Low',
        3: 'Medium',
        4: 'Medium-High',
        5: 'High',
        6: 'Very High'
    }
    return reverse_replace_dict[prediction]


@app.route("/product", methods=["POST"])
def product():

    # Load Models
    rf_model = joblib.load(r'C:\Users\Hursh Shah\Documents\GitHub\HackerBytes-2\flask-server\rf_model.joblib')
    model_nn = load_model(r'C:\Users\Hursh Shah\Documents\GitHub\HackerBytes-2\flask-server\keras_model.h5')
    xgb_model = joblib.load(r'C:\Users\Hursh Shah\Documents\GitHub\HackerBytes-2\flask-server\xgboost_model.joblib')

    # Extract data from the request
    data = request.get_json()
    print(data)

    input_data_dict = {
        'Energy Consumption': data['Energy Consumption'],
        'Electricity Usage': data['Electricity Usage'],
        'Gasoline Usage': data['Gasoline Usage'],
        'Water Usage': data['Water Usage'],
        'Emission Levels': data['Emission Levels'],
        'Recyclability': data['Recyclability'],
        '% of Recycled Materials Used': data['% of Recycled Materials Used'],
        'Biodegradability': data['Biodegradability'],
        'Toxicity': data['Toxicity'],
        'Materials': data['Materials']
    }

    # Convert input data to DataFrame
    input_data = DataFrame(input_data_dict, index=[0])

    # Preprocess the input data 
    preprocessed_input = preprocess(input_data)

    # Use your models to make a prediction
    rf_prediction = rf_model.predict(preprocessed_input)
    nn_prediction = model_nn.predict(preprocessed_input)
    xgb_prediction = xgb_model.predict(preprocessed_input)

    # Calculate average prediction
    average_prediction = np.mean([rf_prediction, nn_prediction, xgb_prediction])

    mapped_prediction = map_prediction_to_string(average_prediction)

    # Send the prediction as a response
    response = jsonify({'prediction': mapped_prediction})
    return response, 200


if __name__ == "__main__":
    app.run(debug=True)

    