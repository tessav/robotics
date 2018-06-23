import os
from PIL import Image

DIRECTORIES = [
    '/two_dollars',
    '/five_dollars',
    '/ten_dollars',
    '/background',
]
OPERATION = '/rotate_270'
IMG_SIZE = 256


def resize_image(image_path, save_path):
    im = Image.open(image_path)
    w, h = im.size
    s = h  # shorter side
    im = im.crop((w//2 - s//2, h//2 - s//2, w//2 + s//2, h//2 + s//2))
    im.thumbnail((IMG_SIZE, IMG_SIZE))
    im.save(save_path)


def rotate_90(image_path, save_path):
    im = Image.open(image_path)
    im = im.transpose(Image.ROTATE_90)
    im.save(save_path)


def rotate_180(image_path, save_path):
    im = Image.open(image_path)
    im = im.transpose(Image.ROTATE_180)
    im.save(save_path)


def rotate_270(image_path, save_path):
    im = Image.open(image_path)
    im = im.transpose(Image.ROTATE_270)
    im.save(save_path)


if __name__ == "__main__":
    for dir in DIRECTORIES:
        current = os.getcwd() + '/images' + dir
        save = os.getcwd() + '/images' + OPERATION + dir
        print(current)
        for file in os.listdir(current):
            if 'DS_Store' in file:
                continue
            if OPERATION == '/resize':
                resize_image(current + '/' + file, save + '/' + file)
            elif OPERATION == '/rotate_90':
                rotate_90(current + '/' + file, save + '/' + OPERATION + '_' + file)
            elif OPERATION == '/rotate_180':
                rotate_180(current + '/' + file, save + '/' + OPERATION + '_' + file)
            elif OPERATION == '/rotate_270':
                rotate_270(current + '/' + file, save + '/' + OPERATION + '_' + file)
            #break
        #break
