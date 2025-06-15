# reading video
import cv2 as cv
# capture=cv.VideoCapture('./humans.mp4')
# while True:
#     isTrue, frame=capture.read()
#     cv.imshow("Video 1 ",frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

import cv2

# # Initialize the HOG descriptor/person detector
# hog = cv2.HOGDescriptor()
# hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# cap = cv2.VideoCapture('./humans.mp4')  # Replace with 0 for webcam

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break 

#     # Resize frame for faster processing
#     frame = cv2.resize(frame, (640, 480))

#     # Detect people in the frame
#     boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8))

#     # Draw bounding boxes
#     for (x, y, w, h) in boxes:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#     cv2.imshow('Human Detection', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2

cap = cv2.VideoCapture('./humans                                                                                                                                                                                                                                                                                                                                                                                                                               .mp4')  # Replace with 0 for webcam
fgbg = cv2.createBackgroundSubtractorMOG2()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Threshold the mask to remove shadows (gray areas)
    _, fgmask = cv2.threshold(fgmask, 250, 255, cv2.THRESH_BINARY)

    # Bitwise-AND mask and original frame to get the foreground
    fg = cv2.bitwise_and(frame, frame, mask=fgmask)

    cv2.imshow('Foreground', fg)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

