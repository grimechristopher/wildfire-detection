# Settings
# Variable Settings
IMG_SIZE = 256  # the size images are resized before using to train models
TRAIN_DIR = "images/train" #image training directory
EPOCHS = 10 #The number of times the training script goes over the dataset
MODEL_PATH = "smoke_classifier.model" #Location to save/load the model

WIDTH = 1024 # Set images to be same width
SLIDE_STEP_SIZE = 32 # How far each window moves when scaning image for smoke
PYR_SCALE = 1.5 # ADD Pyramind scaling 
MIN_SIZE = (300, 150) # Find the cameras aspect ratio...
INPUT_SIZE = (IMG_SIZE, IMG_SIZE) # Size of the Classification dimensions. The dimesions need to be the same as the image size the models used
MODEL_PATH = "smoke_classifier.model" # USING IN BOTH