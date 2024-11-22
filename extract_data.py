# %%
# Prepare the environment
import os
from bfio import BioReader
import numpy as np
from PIL import Image
from pathlib import Path


# Paths to the input and output Zarr files
input_zarr_file = 'data/test.ome.zarr'

# check if the image data npy file exists
# if it does, load it
# else, read the input zarr file and save it to a npy file

data_file = Path('image_data.npy')
if data_file.exists():
    study_data = np.load('image_data.npy')
else:
    # Read the input Zarr file
    br = BioReader(input_zarr_file)
    image_data = br[:]

    # Slice a portion of the data
    study_data = image_data[0:2000, 0:2000, 0:500]

    # Move last dimension to the first
    study_data = np.moveaxis(study_data, -1, 0)

    # Save the data to a npy file
    np.save('image_data.npy', study_data)

    # Export study data to jpg files per slice (first dimension) in folder
    # 'slices'
    os.makedirs('slices', exist_ok=True)
    for i in range(study_data.shape[0]):
        im_array_8bit = (
            study_data[i] / np.max(study_data[i]) * 255).astype(np.uint8)
        im = Image.fromarray(im_array_8bit)

        # Use an integer to name the files, starting from 000001 to 999999
        im.save(f'data/slices/{i:06d}.jpg')