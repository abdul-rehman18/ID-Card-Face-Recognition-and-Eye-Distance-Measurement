# ID-Card-Face-Recognition-and-Eye-Distance-Measurement

This project is built using Flask and serves as a tool for comparing images of a person's face with an ID card image. It utilizes face recognition techniques to determine similarity between the images and also measures the distance between the eyes in the person's image.

# Features

Upload an ID card image and a person's image for comparison.
Utilize image processing techniques to assess the similarity between the images.
Calculate and display the similarity score and match result.
Measure the distance between the eyes in the person's image.
Provide feedback on whether the images match based on a predefined threshold.
Display a confusion matrix, F1 score, and accuracy of the matching predictions.

# Prerequisites

Flask
scikit-learn
OpenCV
NumPy
face_recognition
HTML/CSS

# Installation

Install the required packages using the following command:
```pip install Flask scikit-learn opencv-python numpy```

Also, Enter the following command to install cmake, dlib, face_recognition using pip
```pip install cmake ```
```pip install dlib```
```pip install face_recognition```

# Usage

On the frontend page, you'll find an upload form with fields to upload the ID card image and the person's image.
Choose the images you want to compare and click the "Submit" button.
The model will process the images using face recognition techniques and provide a similarity score and match result.
The distance between the eyes in the person's image will also be displayed.
The system will predict whether the images match based on a predefined threshold. The prediction will be displayed on the result page.
The confusion matrix, F1 score, and accuracy of the matching predictions will be printed on the frontend.

# Important Notes

The application supports image formats: JPG, JPEG, and PNG.
The similarity score threshold for predicting a match is set to 0.68. You can modify this threshold in the code as needed.
Ensure that the required dependencies are installed before running the code.

# Acknowledgments
The face recognition and eye distance measurement techniques are based on various libraries and resources available in the public domain. 
Special thanks to the developers and maintainers of Flask, face_recognition, scikit-learn and OpenCV for their excellent tools.



