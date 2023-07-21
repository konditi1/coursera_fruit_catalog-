#!/usr/bin/python3
"""
Use Python requests module to upload the processed images
to the web server at [linux-instance-IP-Address]/upload
"""
import requests
import os


def upload_images(image_dir, server_url):
    """
    upload_images is a function that uploads the processed images
    to the web server at [linux-instance-IP-Address]/upload
    :param image_dir: path to the directory containing the processed images
    :param server_url: the url of the web server
    """
    for filename in os.listdir(image_dir):
        if filename.endswith('.JPEG'):
            image_path = os.path.join(image_dir, filename)
            with open(image_path, 'rb') as image_file:
                response = requests.post(server_url, files={'file': image_file})
                if response.status_code == 201:
                    print(f"successfully uploaded {filename} to {server_url}")
                else:
                    print(f"failed to upload {filename}. status code: {response.status_code}")


def main():
    # Replace 'your_images_directory' with the actual path of the directory containing processed images
    images_directory = "~/supplier-data/processed_images"

    # Replace 'your_server_url' with the URL of the server endpoint to upload images (e.g.,
    # 'http://your-server/upload/')
    server_url = "http://localhost/upload/"

    upload_images(images_directory, server_url)


if __name__ == "__main__":
    main()
