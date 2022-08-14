import os
from PIL import Image, ImageFilter

def task(n=100_000_000):
    while n:
        n -= 1

def create_thumbnail(filename, size=(100,100),thumb_dir ='thumbs'):
    img = Image.open(filename)
    img = img.filter(ImageFilter.GaussianBlur())
    img.thumbnail(size)
    img.save(f'{thumb_dir}/{os.path.basename(filename)}')
    print(f'{filename} was processed...')