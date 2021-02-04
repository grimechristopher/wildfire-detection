# run.py
# Used for testing and demonstrating how to call the checkImage function in detect_smoke 

import sys
from detect_smoke import *

#img_path = "images/test/1.jpg" # Default test image loaded 
#img_path = "images/test/2.jpg" # Default test image loaded 
#img_path = "images/test/3.jpg" # Default test image loaded 
#img_path = "images/test/5.jpg" # Default test image loaded -- issues
#img_path = "images/test/6.jpg" # Default test image loaded 
#img_path = "images/test/7.jpg" # Default test image loaded 
#img_path = "images/test/small_smoke.jpg" # Default test image loaded 
#img_path = "images/test/none.jpg" # Default test image loaded 
#img_path = "images/test/mine-1.jpg"
#img_path = "Test images/city.png"

img_paths = [ "images/test/1.jpg",
			  "images/test/2.jpg",
			  "images/test/3.jpg",
			  "images/test/5.jpg",
			  "images/test/6.jpg",
			  "images/test/7.jpg",
			  "images/test/small_smoke.jpg",
			  "images/test/none.jpg",
			  "images/test/mine-1.jpg",
			 ]

for path in img_paths:
	checkImage(path) # Call checkImage function in detect_smoke.py
