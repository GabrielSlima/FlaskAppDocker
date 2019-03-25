from flask import Flask
from flask import jsonify
import json
import time

app = Flask(__name__)

simpleResponseData = '{"status": 200, "response": "Success!"}'


@app.route('/app/api', methods=['GET', 'POST'])
def firebaseApi():
    time.sleep(5)
    return jsonify(json.loads(simpleResponseData))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
