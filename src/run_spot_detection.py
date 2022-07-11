import os

import smma.src.utilities as utilities
from smma.src import spot_detection as spd
from loguru import logger

logger.info('Import OK')

input_folder = utilities.locate_raw_drive_files(input_path='raw_data/raw_data.txt')
image_ids = {
    # "layout_name": "image_folder_name",
    'slide_layout_1': '',
    # 'slide_layout_2': '',
}

output_folder = 'results/test/'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ---------------Initial_cleanup---------------

spd.initial_cleanup(input_folder, image_ids, output_folder)

# -----------Optimise spot counting-----------
# Option 1: Via Napari


# Option 2: Automatically
image_location = f'{input_folder}/'
reference_image = ''
test_image = ''
spd.optimise_comdet(image_location, reference_image, test_image, max_pixels=5, max_threshold=10)


# ---------------Count spots---------------
            # CHANNEL: [SNR, SIZE]
thresholds = {'638': [8, 4]} 
spd.count_spots(output_folder, thresholds=thresholds)

# ------------------Visualise------------------
spd.visualise_heatmap(output_folder)
spd.visualise_examples(output_folder, example_wells=False, num_wells=10)