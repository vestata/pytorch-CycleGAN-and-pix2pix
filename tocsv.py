import os
import numpy as np
from PIL import Image
import pandas as pd

def process_images_to_csv(input_folder, output_file):
    """
    Process all images in the given folder and save them as a CSV file.

    Parameters:
        input_folder (str): The path to the folder containing images.
        output_file (str): The path to the CSV file where results should be saved.
    """
    data = []  # This will store all image data.
    image_names = []  # This will store the names of the images.

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith((".png", ".jpg", ".jpeg")):  # Check for common image file extensions
            file_path = os.path.join(input_folder, filename)
            # Open the image, convert to grayscale, and convert to numpy array
            image = Image.open(file_path).convert('L')
            image_array = np.array(image)
            # Flatten the array to one dimension and append to data
            data.append(image_array.ravel())
            image_names.append(filename)

    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    # Optionally, if you want to add image names as an index or a column
    df.index = image_names  # Set filenames as index
    # Save the DataFrame to a CSV file
    df.to_csv(output_file, index=True, header=False)  # Change `header=True` if you want column headers

# Example usage
input_folder = '/home/nini/pytorch-CycleGAN-and-pix2pix/retmp/tmp2/test_latest/images'
output_file = 'output.csv'
process_images_to_csv(input_folder, output_file)