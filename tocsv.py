import os
import numpy as np
from PIL import Image
import pandas as pd
import sys

def process_images_to_csv(input_folder, output_file):
    """
    Process all images in the given folder and save them as a CSV file,
    with the first column labeled 'index' for image IDs and first row as header.

    Parameters:
        input_folder (str): The path to the folder containing images.
        output_file (str): The path to the CSV file where results should be saved.
    """
    data = []  # This will store all image data.
    ids = []  # This will store numeric ids.

    # Counter for numeric ids
    counter = 0

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):  # Check for common image file extensions
            file_path = os.path.join(input_folder, filename)
            try:
                image = Image.open(file_path).convert('RGB')
                image_array = np.array(image)
                # Flatten the array to one dimension and append to data
                data.append(image_array.flatten())
                ids.append(counter)  # Use a simple integer counter as the ID
                counter += 1  # Increment the counter for the next image
            except Exception as e:
                print(f"Failed to process image {file_path}: {e}")

    # Create a DataFrame from the data
    pixel_columns = [i for i in range(data[0].shape[0])]  # Generate pixel column names
    df = pd.DataFrame(data, columns=pixel_columns)
    df.insert(0, 'index', ids)  # Insert the ids column at the first position

    # Save the DataFrame to a CSV file with headers
    df.to_csv(output_file, index=False, header=True)  # Set header=True and provide headers

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python tocsv.py <input_folder> <output_file>")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    output_file = sys.argv[2]
    process_images_to_csv(input_folder, output_file)

