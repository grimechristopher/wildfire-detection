# From https://www.pyimagesearch.com/2020/06/22/turning-any-cnn-image-classifier-into-an-object-detector-with-keras-tensorflow-and-opencv/

import imutils

def sliding_window(image, step, ws):
	# image is the current image that is being looked at
	# Step of 4-5 is common... its how many pixels the box is being moved
	# ws is window size. The size of the box

	# slide a window across the image
	# Goes row by row; each column in row then moves to next row
	for y in range(0, image.shape[0] - ws[1], step):
		for x in range(0, image.shape[1] - ws[0], step):
			# yield the current window
			yield (x, y, image[y:y + ws[1], x:x + ws[0]])

# Allows to use multiple scales of the image			
def image_pyramid(image, scale=1.5, minSize=(224, 224)):
	# Scale is how much the size of the image is changed each time its resized
	# minSize is the smallest the input image can be
	
	# yield the original image
	yield image
	# keep looping over the image pyramid
	while True:
		# compute the dimensions of the next image in the pyramid
		w = int(image.shape[1] / scale)
		image = imutils.resize(image, width=w)
		# if the resized image does not meet the supplied minimum
		# size, then stop constructing the pyramid
		if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
			break
		# yield the next image in the pyramid
		yield image