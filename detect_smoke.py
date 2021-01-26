# Imports
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.models import load_model

from imutils.object_detection import non_max_suppression

from detection_helpers import sliding_window
from detection_helpers import image_pyramid

import numpy as np
import argparse
import imutils
import time
import cv2
from datetime import datetime
import settings


def checkImage(img_path):
    prob = 1

    # Load the classifier model
    model = load_model(settings.MODEL_PATH)

    # Load image
    img = cv2.imread(img_path)
    # Resize image
    img = imutils.resize(img, width=settings.WIDTH)
    windowHeight, windowWidth = img.shape[:2]
    # initialize the image pyramid
    pyramid = image_pyramid(img, scale=settings.PYR_SCALE, minSize=settings.MIN_SIZE) # Creates multiple sizes of image

    rois = [] # regions of interest
    coords = [] # coords of the rois

    start = time.time() # Log time

    for image in pyramid:
	    scale =  windowWidth / float(image.shape[1])
	    for (x, y, roiOrig) in sliding_window(image, settings.SLIDE_STEP_SIZE, settings.MIN_SIZE):
	    	x = int(x * scale)
	    	y = int(y * scale)
    		w = int(settings.IMG_SIZE / 2 * scale)
    		h = int(settings.IMG_SIZE / 2 * scale)
			
	    	roi = cv2.resize(roiOrig, settings.INPUT_SIZE)
    		roi = img_to_array(roi)
    		roi = preprocess_input(roi)
			
	    	rois.append(roi)
	    	coords.append((x, y, x + w, y + h))
    end = time.time()	

    rois = np.array(rois, dtype="float32") # Convert rois to numpy array
    # Classify each ROI
    preds = model.predict(rois)

    print(preds) # Print the predictions. predictions of 1 are smoke. anything less than 1 and it not sure.

    # Label the predictions
    labels = {}
    for (i, p) in enumerate(preds):
	    if preds[i][0] == 1: # If the prediction is sure it detects smoke
	    	label = "Smoke"
	    	box = coords[i]
	    	# add box around the detection
	    	temp = labels.get(label, [])
	    	temp.append((box, prob))
	    	labels[label] = temp	
    # For each area where smoke was detected
    for label in labels.keys():
	    img_out = img.copy()
	    for (box, prob) in labels[label]:
	    	(startX, startY, endX, endY) = box
	    	cv2.rectangle(img_out, (startX, startY), (endX, endY), (0, 204, 255), 2)
	    #cv2.imshow("Before", img_out)
	    img_out = img.copy()
			
	    boxes = np.array([p[0] for p in labels[label]])
	    boxes = non_max_suppression(boxes, prob)

	    for (startX, startY, endX, endY) in boxes:
	    	# draw the bounding box and label on the image
	    	cv2.rectangle(img_out, (startX, startY), (endX, endY), (0, 204, 255), 2)
	    	y = startY - 10 if startY - 10 > 10 else startY + 10
	    	cv2.putText(img_out, label, (startX, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.45, (0, 204, 255), 2)
	    #cv2.imshow("Detected Smoke", img_out)
	    cv2.imwrite("images/detected/" + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg", img_out)
	    #cv2.waitKey(0)