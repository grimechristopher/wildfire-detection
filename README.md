# Wildfire Early Detection

> The Wildfire Detection project is a machine learning application developed in Python using the Tensorflow library. The goal of the project was to explore ways to quick detection of wildfires when they break out. 

> Developed in collaboration with Daniel Bernabe and Christopher Grime. 

## Description

The Wildfire Early Detection project looks for smoke in images and sends a notification out when smoke is detected. The goal of an early detection project like this is to quickly identify the breakout of wildfires allowing a headstart on mitigating the destruction of the fire.

Our first step was to train an image classifier to recognize smoke. To accomplish this, we used a Convolutional Neural Network to develop the smoke classification model. The dataset used to train the model used a modified version of the [aiformankind gridded dataset](https://github.com/aiformankind/lets-stop-wildfires-hackathon/blob/master/wildfire_smoke_challenge_1B.md). 

The script for detecting smoke uses the image classifier model for detection. It uses two scripts that were adapted from [pyimagesearch](https://www.pyimagesearch.com/2020/06/22/turning-any-cnn-image-classifier-into-an-object-detector-with-keras-tensorflow-and-opencv/) to split up large images from a camera and detect smoke in smaller chunks. 

### TODO: Info about getting images and sending notification

## Conclusion

The project allowed us to practice software development skills and develop a solution to a real-world problem. It was an excellent opportunity for an introduction to machine learning. 

---
