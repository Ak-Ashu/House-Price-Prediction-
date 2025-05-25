from flask import Flask, jsonify, request

import util

app = Flask(__name__)

print("Starting Python Flask Server For Home Price Prediction..")
util.load_saved_artifacts()

@app.route('/get_location_names')
def get_location_names():
    locations = util.get_location_names()
    print("DEBUG: Locations from util.py ->", locations)
    response = jsonify({'locations': locations})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True)