from flask import Flask, request
from flask_cors import CORS
from bardapi import Bard
import os

app = Flask(__name__)
CORS(app)

os.environ['_BARD_API_KEY'] = 'XQioAemGhqCVyyCpevEoko2VYuzou8Xg5W2b_STl-gHHbQDmw1_11LhQwF2eCyHw9u9QdA.'

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

@app.route("/test", methods=["POST"])
def test():
    data = request.get_json()
    print(Bard().get_answer("DONT SAY SURE OR CONFIRM ANYTHING. STOP EXPLAINING STUFF.  STOP EXPLAINING ONLY GIVE THE DEFINITION. ONLY output all the raw materials used in a " + data['value']+ " in a python dictionary expression format, with the second part being all the raw materials listed together and the first part being called 'Materials'. Next, give one output for recyclability and biodegradability on a scale of no, yes and partial. Keep it all in python dictionary format")['content'])
    # print(data);
    return 'Success', 200

if __name__ == "__main__":
    app.run(debug=True)
