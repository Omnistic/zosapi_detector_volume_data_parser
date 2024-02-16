import napari
import numpy as np


# Retrieve your temporary file path
detector_volume_text_file = 'D:/temporary_file.txt'

# This assumes you have the following setting in OpticStudio:
# Setup..OpticStudio Preferences..General..TXT File Encoding: Unicode
# Otherwise the numbering is different

# Constant lines numbers and offsets to parse the Detector Viewer data
SIZE_LINE = 8
DATA_START_LINE = 28
IN_BETWEEN_SLICES = 4

# Read all lines of the text file at once
with open(detector_volume_text_file, encoding="utf-16") as f:
    lines = f.readlines()

# Get the line with the Size information
size_information = lines[SIZE_LINE].split()

# Retrieve the pixel size of the data
pixel_size = np.array([size_information[11],
                       size_information[14],
                       size_information[17]]).astype(int)

# Initialize an empty array with the size of the data
volume_data = np.empty(pixel_size)

# Parse the rest of the text file based on the pixel size
for slice_id in range(pixel_size[2]):
    start_line = DATA_START_LINE + slice_id * ( pixel_size[1] + IN_BETWEEN_SLICES )
    end_line = start_line + pixel_size[1]
    slice_data = np.transpose(np.asarray([line.split('\t') for line in lines[start_line:end_line]]).astype(float)[:, 1:])
    volume_data[:, :, slice_id] = slice_data

# Display the data in Napari
viewer = napari.Viewer()
viewer.dims.ndisplay = 3
image_layer = viewer.add_image(volume_data)
image_layer.colormap = 'inferno'
image_layer.gamma = 0.5
napari.run()