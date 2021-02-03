# Imports
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import settings

# Data preparation
# Augmentation
# Used increase the variation in the dataset. This allows the algorithm to have more samples to train the model with. 
# https://www.tensorflow.org/tutorials/images/data_augmentation

# Constructs an augmented data generator
aug = ImageDataGenerator(
		rescale=1./255, 
		shear_range=0.2, 
		zoom_range=0.2, 
		horizontal_flip=True,
		)
aug = ImageDataGenerator(rescale=1./255)

# Create augmented data using the data generator that was just created
# images is the data that will train the model and test is used to validate
images = aug.flow_from_directory(settings.TRAIN_DIR, target_size=(settings.IMG_SIZE, settings.IMG_SIZE), batch_size=32, class_mode='binary')
test = aug.flow_from_directory(settings.TRAIN_DIR, target_size=(settings.IMG_SIZE, settings.IMG_SIZE), batch_size=32, class_mode='binary')

# Convolutional Neural Network (CNN)
# A CNN consists of 3 main parts: Convolution, Pooling, Flattening

# init CNN
model = Sequential()

# Convolution
model.add(Conv2D(16, (7, 7), padding="same", input_shape=(settings.IMG_SIZE, settings.IMG_SIZE, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(32, (3, 3), input_shape = (settings.IMG_SIZE, settings.IMG_SIZE, 3), activation='relu'))

# Pooling
# Pooling reduces overfitting because CNN will only get the features that are important for classification
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(32, (3, 3), input_shape = (settings.IMG_SIZE, settings.IMG_SIZE, 3), activation='relu'))

model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(32, (3, 3), input_shape = (settings.IMG_SIZE, settings.IMG_SIZE, 3), activation='relu'))

model.add(MaxPooling2D(pool_size=(2,2)))

# Flattening
model.add(Flatten())
# Add layers to the CNN 
model.add(Dense(units = 128, activation='relu')) #Input layer
model.add(Dropout(0.5))
model.add(Dense(units=1, activation='sigmoid')) # Output Layer

# Compile the Model
model.compile(optimizer='adam', loss='binary_crossentropy',metrics=['accuracy'])
model.fit_generator(images, steps_per_epoch=40, epochs=settings.EPOCHS, validation_data=test, validation_steps=1000)

# Create and print classification report


# Output
model.save(settings.MODEL_PATH)