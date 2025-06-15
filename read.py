import cv2 as cv

# reading image
# img=cv.imread('./cat.webp')
# cv.imshow("Orange cat",img)

# cv.waitKey(0)

# # reading video
# capture=cv.VideoCapture('./timer.mp4')
# while True:
#     isTrue, frame=capture.read()
#     cv.imshow("Video 1 ",frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

# opening camera

capture=cv.VideoCapture(0)
while True:
    isTrue, frame=capture.read()
    cv.imshow("Video 1 ",frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

def rescaleframe(frame,scale=0.55):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# # # reading video
# capture=cv.VideoCapture('./timer.mp4')
# while True:
#     isTrue, frame=capture.read()
#     resized_frame=rescaleframe(frame)
#     cv.imshow("Video 2 ",resized_frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

