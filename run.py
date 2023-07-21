#!/usr/bin/env python3

import os
import requests


def read_text_file(file_path):
    """
    Read the content of a text file and return its contents as a list of lines.
    param file_path: Path to the text file.
    return: List of lines in the text file.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines


def parse_fruit_data(lines):
    """
    Parse the content of the text file and extract the name, weight, and description of the fruit.
    :param lines: List of lines in the text file.
    :return: Dictionary containing the parsed data.
    """
    name = lines[0].strip()
    weight = int(lines[1].strip().split()[0])  # Extract the weight as an integer
    description = lines[2].strip()
    image_name = os.path.splitext(os.path.basename(lines[0].strip()))[0] + '.jpeg'
    return {
        "name": name,
        "weight": weight,
        "description": description,
        "image_name": image_name
    }


def upload_fruit_data(server_url, fruit_data):
    """
    Upload the fruit data to the Django server.
    :param server_url: The URL of the server endpoint to upload data (e.g., 'http://your-server/fruits/')
    :param fruit_data: Dictionary containing the fruit data.
    """
    response = requests.post(server_url, json=fruit_data)
    if response.status_code == 201:
        print(f"Successfully uploaded fruit: {fruit_data['name']}")
    else:
        print(f"Failed to upload fruit: {fruit_data['name']}. Status code: {response.status_code}")


def main():
    # Replace 'your_descriptions_directory' with the actual path of the directory containing text files
    descriptions_directory = '~/supplier-data/descriptions/'

    # Replace 'your_server_url' with the URL of the server endpoint to upload data (e.g., 'http://your-server/fruits/')
    server_url = "http://localhost/fruits/"

    for filename in os.listdir(descriptions_directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(descriptions_directory, filename)
            lines = read_text_file(file_path)
            fruit_data = parse_fruit_data(lines)
            upload_fruit_data(server_url, fruit_data)


if __name__ == "__main__":
    main()
