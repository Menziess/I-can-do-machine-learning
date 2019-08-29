from base64 import b64decode
from numpy import array
from PIL import Image
from io import BytesIO
from re import sub


def data_to_arr(data, scalar):
    image_data = sub('^data:image/.+;base64,', '', data)
    decoded_data = b64decode(image_data)
    im = Image.open(BytesIO(decoded_data))
    im = im.convert('L')
    matrix = array(im) * scalar
    return matrix.flatten()
