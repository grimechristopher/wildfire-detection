

# Settings
# Variable Settings
IMG_SIZE = 256
TRAIN_DIR = "images/train"
EPOCHS = 10
MODEL_PATH = "smoke_classifier.model"

WIDTH = 1024 # Set images to be same width 
#SLIDE_STEP_SIZE = 32 # How far each window moves 
SLIDE_STEP_SIZE = 32 # How far each window moves 
PYR_SCALE = 1.5 # ADD Pyramind scaling 
MIN_SIZE = (300, 150) # Find the cameras aspect ratio...
INPUT_SIZE = (IMG_SIZE, IMG_SIZE) # Size of the Classification dimensions
MODEL_PATH = "smoke_classifier.model" # USING IN BOTH