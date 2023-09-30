# Extract csv file from url link
import requests
import os

def extract(url="https://github.com/datasciencedojo/datasets/blob/master/titanic.csv", file_path="Data/titanic.csv", save_folder="Data"):
    # Make a directory if it doesn't exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    with requests.get(url) as response:
        with open(file_path, 'wb') as file:
            file.write(response.content)
    return file_path