# Configure the parameters of our project
import os
import torch
import platform

# The device to be used for training and evaluation (Windows)
if platform.system() == "Darwin":
    if torch.backends.mps.is_available():
        DEVICE = torch.device("cpu")
    else:
        print ("MPS device for MacOS not found.")
    WORKING_DIRECTORY_PATH = "./SICOM_DeepLearning/Semantic_Segmentation_U-NET/"

elif platform.system() == 'Linux':
    WORKING_DIRECTORY_PATH = "/home/conversb/Semantic_Segmentation_U-NET/"
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

else:
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    WORKING_DIRECTORY_PATH = ""

######################################## General Settings ########################################
# Test or Train the model
TYPE_PROCESS = "train"  #value: {"train", "test"}
ID_SESSION = "train_15_12_23_part-3" # unique ID

# Activate Parallelism
ACTIVATE_PARALLELISM = False # Recommended to activate just for Gricad
NBR_WORKERS = 8 # 24 is the maximum for Gricad

if TYPE_PROCESS == "test":
    NBR_GPU = 1 # Work on gricad just with one GPU for testing
else:
    NBR_GPU = 3 # Adapt this one for the training mode

# Data Augmentation
AUG_DATA = True
GENERATE_AUGMENTED_DATA = False
AUGMENTED_DATA_SPLIT = 1

######################################## Training Settings #######################################
# Define some model parameters
# Define the test split which will separate our dataset into train and test
TEST_SPLIT = 0.15

# Unet Architecture
ENC_CHANNELS= (3, 16, 32, 64)
DEC_CHANNELS = (64, 32, 16)
# Number of class
NBR_CLASSES = 24
ACTIVATE_LABELED_CLASSES = True
# Size of input images
INPUT_IMAGE_HEIGHT = 128
INPUT_IMAGE_WIDTH = 128
BATCH_SIZE = 4
NUM_EPOCHS = 20
# Learning rate
INIT_LR = 0.01
# Threshold just usefull of one class unlabeled
THRESHOLD_TYPE = "mean"

# Vizualization parameters
# True if you want print graphs during the training
MODE_VISUALIZATION = False
VISUALIZATION_DIM = 1 # Lower or egual to NBR_CLASSES

# Early Stopping
EARLY_STOPPING_ACTIVATE = False
PATIENCE = 5

######################################## Test Settings ###########################################
# Number of image to test

SELECTED_IMAGE_TEST = 10

# Metrics
ALL_CONFUSION_MATRIX = False

##################################################################################################

# Define different paths
# The images dataset
IMAGE_DATASET_PATH = os.path.join(WORKING_DIRECTORY_PATH, "dataset", "semantic_drone_dataset", "original_images")
# The RGB color masks of the dataset
MASK_DATASET_PATH = os.path.join(WORKING_DIRECTORY_PATH, "dataset", "semantic_drone_dataset", "RGB_color_image_masks")
# Labels
LABEL_PATH = os.path.join(WORKING_DIRECTORY_PATH, "dataset", "semantic_drone_dataset", "class_dict_seg.csv")
# The output directory
BASE_OUTPUT = os.path.join(WORKING_DIRECTORY_PATH, "output")
# The testing image path
TEST_PATHS = os.path.sep.join([BASE_OUTPUT, ID_SESSION, "test_paths.txt"])
# The model training plot path
PLOT_TRAIN_PATH = os.path.sep.join([BASE_OUTPUT, ID_SESSION, "train_plots"])
# The model test plot path
PLOT_TEST_PATH = os.path.sep.join([BASE_OUTPUT, ID_SESSION, "test_plots"])
# The output serialized model path to save it
MODEL_PATH = os.path.join(BASE_OUTPUT, ID_SESSION, "unet_tgs_salt.pth")
# metric plot path
PLOT_METRICS = os.path.join(BASE_OUTPUT, ID_SESSION, "metrics_plots")
# Path augmented data
AUGMENTED_DATA_IMAGE_PATH = os.path.join(WORKING_DIRECTORY_PATH, "dataset", "semantic_drone_dataset", "augmented_data", "images")
AUGMENTED_DATA_MASK_PATH = os.path.join(WORKING_DIRECTORY_PATH, "dataset", "semantic_drone_dataset", "augmented_data", "masks")

# List of image types
IMAGE_TYPES = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")

# If we will be pinning memory during data loading
PIN_MEMORY = True if( DEVICE == "cuda" or DEVICE == "mps") else False
