from flask import Flask, request,jsonify
from flask_cors import CORS

import numpy as np


# from flask import current_app
# current_app.config['SERVER_NAME'] = 'localhost'   
# with current_app.test_request_context():
#      url = url_for('index', _external=True)

app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/': {'origins': ''}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'

# cred_obj = firebase_admin.credentials.Certificate('../../fyp2022-stockpriceprediction-firebase-adminsdk-ku62m-f9ed330292.json')
# fyp_app = firebase_admin.initialize_app(cred_obj, {
# 	'databaseURL':"https://fyp2022-stockpriceprediction-default-rtdb.asia-southeast1.firebasedatabase.app/",
# 	'storageBucket': 'fyp2022-stockpriceprediction.appspot.com'
# 	})

@app.route("/predict", methods=["POST","GET"])
def submitData():
    return 'hi'


if __name__ =='__main__':
    app.run(debug=True)