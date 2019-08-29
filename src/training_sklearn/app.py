from sklearn import datasets
from flask import Flask, jsonify, render_template, request
from PIL import Image
from io import BytesIO

import base64
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
    import re
    import numpy as np
    data = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAMCAgICAgMCAgIDAwMDBAYEBAQEBAgGBgUGCQgKCgkICQkKDA8MCgsOCwkJDRENDg8QEBEQCgwSExIQEw8QEBD/2wBDAQMDAwQDBAgEBAgQCwkLEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBD/wAARCAAIAAgDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAn/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AJVAA//Z'
    data = request.get_data().decode("utf-8")
    image_data = re.sub('^data:image/.+;base64,', '', data)
    decoded_data = base64.b64decode(image_data)
    im = Image.open(BytesIO(decoded_data))
    im = im.convert('L')
    matrix = np.array(im) / 20
    flat = matrix.flatten()

    global model
    return jsonify({
        'prediction': int(model.predict([flat])[0]),
        'data': str(flat)
    })

    # data = request.get_data()
    # decoded = base64.b64decode(data)
    # Image.open(decoded)

    # im = imageio.imread('astronaut.png')
    # im.shape  # im is a numpy array
    # (512, 512, 3)
    # imageio.imwrite('imageio:astronaut-gray.jpg', im[:, :, 0])


@app.route("/predict/<int:i>/")
def predict_index(i):
    global model
    return jsonify({
        'prediction': int(model.predict(digits.data[i:])[0]),
        'actual': int(digits.target[i])
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
