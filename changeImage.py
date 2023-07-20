#!/usr/bin/python3
"""
Write a Python script named changeImage.py to process supplier images.
"""
from PIL import Image
import os


def process_images(input_dir, output_dir):
    """
    process_image is a function that processes supplier images.
    in the input_dir and save them in the output_dir
    :param input_dir: path to the directory containing the original images
    :param output_dir: path to the directory to save the processed images
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(input_dir):
        if filename.endswith('.TIF'):
            input_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + '.JPEG'
            output_path = os.path.join(output_dir, output_filename)
            process_single_image(input_path, output_path)


def process_single_image(input_path, output_path):
    """
    process_single_image single image from RGBA to RGB.
    :param input_path: path to the image to process(input image)
    :param output_path: path to save the processed image
    """
    img = Image.open(input_path)

    # convert from RGBA to RGB
    rgb_image = img.convert('RGB')

    # change the resolution to 600x400 pixels
    resized_image = rgb_image.resize((600, 400))

    # save the processed image as JPEG format
    resized_image.save(output_path, format='JPEG')


def main():
    input_directory = "~/supplier-data/images"
    output_directory = "~/supplier-data/processed_images"
    process_images(input_directory, output_directory)


if __name__ == "__main__":
    main()
