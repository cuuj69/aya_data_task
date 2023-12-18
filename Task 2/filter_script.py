#!/usr/bin/python3

import os
import csv
import shutil

"""we need to read the csv files and get file names are for human and which ones are for background and then based on that seach use to filter and sort the images into human and background from the masks folder, the """

"""the csv file has two sections and image_id and mask_id, you can access what type of image you're looking for using the mask_id"""


def read_csv(csv_file_path):
    with open(csv_file_path, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        return list(csv_reader)

def determine_image_type(class_name):
    return class_name.lower()

def copy_files(csv_data, masks_folder, human_folder, background_folder):
    for row in csv_data:
        mask_id = row['mask_id']
        class_name = row['class_name']

        image_type = determine_image_type(class_name)

        source_path = os.path.join(masks_folder, f"{mask_id}.png")

        if image_type == 'human':
            destination_path = os.path.join(human_folder, f"{mask_id}.png")
        elif image_type == 'background':
            destination_path = os.path.join(background_folder, f"{mask_id}.png")
        else:
            print(f"Unknown image type for Mask ID: {mask_id}")
            continue

        shutil.copy(source_path, destination_path)
        print(f"Mask ID: {mask_id}, Image Type: {image_type}")

# CSV file path
csv_file_path = 'Task 2/instance_mask_annotations.csv'


_1 = 'Task 2/_1'
_2 = 'Task 2/_2'


os.makedirs(_1, exist_ok=True)
os.makedirs(_2, exist_ok=True)

# Read CSV file
csv_data = read_csv(csv_file_path)

copy_files(csv_data, 'Task 2/masks', _1, _2)
