import cv2
from mtcnn import MTCNN #multi-task cascaded convolutional network

def EyeDistance(path):
    res=[]
# Load the image
    image_path = path  # Replace with your image filename
    image = cv2.imread(image_path)

# Initialize the MTCNN detector
    detector = MTCNN()

# Detect faces and landmarks in the image
    faces = detector.detect_faces(image)

# Check if any faces are detected
    if len(faces) > 0:
    # Get the first detected face
        face = faces[0]

    # Measure the known size of the reference object in millimeters
        known_object_size_mm = 35  # Example: credit card width

    # Measure the actual size of the reference object in pixels
        reference_object_width_pixels = abs(face['keypoints']['right_eye'][0] - face['keypoints']['left_eye'][0])
        # print(f"absolute Distance between eyes: {reference_object_width_pixels:.2f} mm")
    # Calculate the conversion factor: pixels to millimeters
        conversion_factor = known_object_size_mm / reference_object_width_pixels
        # print(f"Conversion factor: {conversion_factor:.2f} mm")

    # Measure the distance between eyes in pixels
        distance_pixels = abs(face['keypoints']['left_eye'][0] - face['keypoints']['right_eye'][0])
        # print(f"Distance pixel: {distance_pixels:.2f} mm")

    # Convert distance from pixels to millimeters
        distance_mm = distance_pixels * conversion_factor

        # print(f"Distance between eyes: {distance_mm:} mm")
        res.append(distance_mm)
        res.append(distance_pixels)
        res.append(conversion_factor)
        res.append(reference_object_width_pixels)
        return res
    else:
        print("No face detected in the image.")
        return 0