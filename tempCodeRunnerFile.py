import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

# Initialize webcam
capture = cv.VideoCapture(0)

# Property 3: Width of image
# Property 4: Height of image
capture.set(3, 1280)
capture.set(4, 720)
colorRec=(255,0,255)

# Initialize hand detector with confidence threshold
detector = HandDetector(detectionCon=0.7)
# This sets the minimum confidence threshold for detection to 0.8 (i.e., 80%).
# If the confidence of detecting a hand is below 80%, it will ignore the detection.

while True:
    success, image = capture.read()
    if not success:
        print("Failed to capture image")
        break
    image=cv.flip(image,1)

    # This detects hands in the given image (usually a webcam f