from flask import Flask, request, jsonify
from flask_cors import CORS
from bardapi import Bard
import os

app = Flask(__name__)
CORS(app)

os.environ['_BARD_API_KEY'] = 'XwhWFK57yz8L6Ai8-e3YH5gQSPQ5LG-kGvxzfBjoZSf_z5xTC-bbMe0CQZpJe7C-rL00mw.'

@app.route("/product", methods=["POST"])
def test():
    data = request.get_json()
    value = data.get('value', '')
    
    result = Bard().get_answer("DONT SAY SURE OR CONFIRM ANYTHING. STOP EXPLAINING STUFF. STOP EXPLAINING ONLY GIVE THE DEFINITION. ONLY output all the raw materials used in a " + value + " in a python dictionary expression format, with the second part being all the raw materials listed together and the first part being called 'Materials'. Next, give one output for recyclability and biodegradability on a scale of no, yes and partial. Keep it all in python dictionary format")['content']
    
    return jsonify({'value': result})

if __name__ == "__main__":
    app.run(debug=True)

    