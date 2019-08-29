from imageio import imwrite

import io

IMAGE_FOLDER = './img'

def write_digit(matrix, name):
    folder = io.path.join(IMAGE_FOLDER, name, '.png')
    imwrite(name, matrix)
