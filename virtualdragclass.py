import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import cvzone
import numpy as np
# Initialize webcam
capture = cv.VideoCapture(0)

# Property 3: Width of image
# Property 4: Height of image
capture.set(3, 1280)
capture.set(4, 720)


detector = HandDetector(detectionCon=0.7)

class DragRect():
    def __init__(self,centre,size=[150,150]):
        self.centre=centre
        self.size=size
        self.color=(255,0,255)
        self.dragging = False   

    def update(self,cursor):
        cx,cy=self.centre
        w,h=self.size
        if cx-w//2<cursor[0]<cx+w//2 and cy-h//2<cursor[1]<cy+h//2:
            self.color=(0,255,0)
            self.centre=cursor[0],cursor[1]
            self.dragging = True
        else:
            self.color=(255,0,255)
            self.dragging = False
    def stopdrag(self):
        self.dragging=False
        self.color=(255,0,255)

rectlist=[]
for x in range(5):
    rectlist.append(DragRect([x*250+150,150]))
while True:
    success, image = capture.read()
    if not success:
        print("Failed to capture image")
        break
    

    # This detects hands in the given image (usually a webcam frame)
    # hands : is a list of dictionaries with information like handedness (left/right), landmark positions, and bounding boxes.
    # image : annotated image of hand
    image = cv.flip(image, 1)
    hands, image = detector.findHands(image)

    # Correct handedness after flipping
    for hand in hands:  
        handType = hand["type"]
        hand["type"] = "Right" if handType == "Left" else "Left"

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
        for rect1 in rectlist:
            if length<40:
                cursor=landmarkList[8]
                # call the updated function
                rect1.update(cursor)
            else:
                rect1.stopdrag()

                # SOLID COLOR RECTANGLE
    # for rect1 in rectlist: 
    #     cx,cy=rect1.centre
    #     w,h=rect1.size
    #     cv.rectangle(image,(cx-w//2,cy-h//2),(cx+w//2,cy+w//2),rect1.color,cv.FILLED)
    #     cvzone.cornerRect(image,(cx-w//2,cy-h//2,w,h),20,rt=0)
    # Show the output image with annotations



    # CREATION OF RECTANGLE
    # 1st set of points is th top-left corner of the rectange
    # 2nd set of poitns is the bottom-right corner of the rectangle
    imgnew=np.zeros_like(image,np.uint8)
    for rect1 in rectlist: 
        cx,cy=rect1.centre
        w,h=rect1.size
        cv.rectangle(imgnew,(cx-w//2,cy-h//2),(cx+w//2,cy+w//2),rect1.color,cv.FILLED)
        cvzone.cornerRect(imgnew,(cx-w//2,cy-h//2,w,h),20,rt=0)

        out=image.copy()
        alpha=0  
        mask=imgnew.astype(bool)
        # print(mask.shape)
        out[mask]=cv.addWeighted(image,alpha,imgnew,1-alpha,0)[mask]
    cv.imshow("Image", out)

    # Press 'q' to break the loop and exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and destroy all OpenCV windows
capture.release()
cv.destroyAllWindows()
