import os, sys
from PIL import Image


def main():
    user = os.getenv('USER') # To get the username from environment variable
    image_directory = '/home/{}/supplier-data/images/'.format(user)

    for image_name in os.listdir(image_directory):

        if not image_name.startswith('.') and 'tiff' in image_name:

            image_path = image_directory + image_name

            path = os.path.splitext(image_path)[0]
            new_path = '{}.jpeg'.format(path)

            im = Image.open(image_path)
            im.convert('RGB').resize((600, 400)).save(new_path, "JPEG")


if __name__ == "__main__":
    main()