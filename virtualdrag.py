import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

# Initialize webcam
capture = cv.VideoCapture(0)

# Property 3: Width of image
# Property 4: Height of image
capture.set(3, 1280)
capture.set(4, 720)
colorRec=(255,0,255)

cx,cy,w,h=100,100,200,200 # initial coordinates of the rectangle
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

    # This detects hands in the given image (usually a webcam frame)
    # hands : is a list of dictionaries with information like handedness (left/right), landmark positions, and bounding boxes.
    # image : annotated image of hand
    hands, image = detector.findHands(image)

    if hands:
        # Get the first hand detected : although both hands will be detected but only landmarks for one hand will be printed or incorporated
        hand = hands[0]
        # landmarkList stores the list of landmarks detected on hand with coordinate ids for each
        landmarkList = hand["lmList"]

        # length between the two fingers : coordinates 8 and 12
        # info : Contains the coordinates of the two points and the center.
        point1 = landmarkList[8][:2]
        point2 = landmarkList[12][:2]
        length = detector.findDistance(point1, point2, image)[0]
        print(length)
 
        # bounding box is a rectangle that tightly encloses an object detected in an image — like a hand, face, or object
        bbox = hand["bbox"]
        # Example: Print position of index finger tip (landmark ID 8)
        # print("Index finger tip position:", landmarkList[8])
        if length<30:
            cursor=landmarkList[8] # cursor is fingertips whose coordinate is 8 in landmarklist
            if cx-w//2<cursor[0]<cx+w//2 and cy-h//2<cursor[1]<cy+h//2:
                colorRec=(0,255,0)
                cx,cy=cursor[0],cursor[1]
            else:
                colorRec=(255,0,255)

    # CREATION OF RECTANGLE
    # 1st set of points is th top-left corner of the rectange
    # 2nd set of poitns is the bottom-right corner of the rectangle
    cv.rectangle(image,(cx-w//2,cy-h//2),(cx+w//2,cy+w//2),colorRec,cv.FILLED)
    # Show the output image with annotations
    cv.imshow("Image", image)

    # Press 'q' to break the loop and exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and destroy all OpenCV windows
capture.release()
cv.destroyAllWindows()
