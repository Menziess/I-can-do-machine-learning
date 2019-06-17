from sklearn import datasets
from flask import Flask, jsonify
import pickle


def load_model(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

digits = datasets.load_digits()
model = load_model('./src/models/clf')


# Boot app
app = Flask(__name__)


# Handle generic 404
@app.errorhandler(404)
def not_found(e):
    return jsonify({
        'title': e.name,
        'status': e.code,
        'detail': e.description,
    })


@app.route("/<int:i>/")
def predict_index(i):
    global model
    return jsonify({
        'prediction': int(model.predict(digits.data[i:])[0]),
        'actual': int(digits.target[i])
    })



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
