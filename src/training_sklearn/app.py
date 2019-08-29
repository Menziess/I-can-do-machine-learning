from sklearn import datasets
from flask import Flask, jsonify, render_template, request
from training_sklearn.utils import data_to_arr

import pickle


def load_model(path):
    with open(path, 'rb') as f:
        return pickle.load(f)


digits = datasets.load_digits()
model = load_model('./src/models/clf.pickle')


# Boot app
app = Flask(__name__,
            static_folder="./frontend/static",
            template_folder="./frontend")


# Handle generic 404
@app.errorhandler(404)
def not_found(e):
    return jsonify({
        'title': e.name,
        'status': e.code,
        'detail': e.description,
    })


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict_image():
    data = request.get_data().decode("utf-8")
    arr = data_to_arr(data, 0.06)

    global model
    return jsonify({
        'prediction': int(model.predict([arr])[0]),
        'data': str(arr)
    })


@app.route("/predict/<int:i>/")
def predict_index(i):
    global model
    return jsonify({
        'prediction': int(model.predict(digits.data[i:])[0]),
        'actual': int(digits.target[i])
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
