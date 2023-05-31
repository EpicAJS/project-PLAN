import cv2
import pickle
import cvzone
import numpy as np

cap = cv2.VideoCapture('IMG_0368_W.mp4')
#cap = cv2.resize(cap, (0, 0), fx=0.35, fy=0.35)

width, height = 237, 120
with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)


def empty(a):
    pass


cv2.namedWindow("Vals")
cv2.resizeWindow("Vals", 640, 240)
cv2.createTrackbar("Val1", "Vals", 30, 50, empty)
cv2.createTrackbar("Val2", "Vals", 25, 50, empty)
cv2.createTrackbar("Val3", "Vals", 9, 50, empty)


def checkSpaces():
    spaces = 0
    for pos in posList:
        x, y = pos
        w, h = width, height

        w2, h2 = width/2, height/2

        imgCrop = imgThres[y:y + h, x:x + w]
        count = cv2.countNonZero(imgCrop)

        if count < 900:
            color = (0, 200, 0)
            thic = 2
            spaces += 1
            cv2.circle(img, (x, y), 10, color, thic)
            cv2.circle(img, (x-w, y-h), 10, color, thic)
            cv2.circle(img, (x+w, y+h), 10, color, thic)

        else:
            color = (0, 0, 200)
            thic = 2

        cv2.rectangle(img, (x, y), (x + w, y + h), color, thic)

        cv2.putText(img, str(cv2.countNonZero(imgCrop)), (x, y + h - 6), cv2.FONT_HERSHEY_PLAIN, 1,
                    color, 2)

    cvzone.putTextRect(img, f'Free: {spaces}/{len(posList)}', (50, 60), thickness=3, offset=20,
                       colorR=(0, 200, 0))


while True:

    # Get image frame
    success, img = cap.read()
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    frame = cv2.resize(frame, (100, 50))

    print(frame.shape)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    # img = cv2.imread('WHSLOT1.png')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    # ret, imgThres = cv2.threshold(imgBlur, 150, 255, cv2.THRESH_BINARY)

    val1 = cv2.getTrackbarPos("Val1", "Vals")
    val2 = cv2.getTrackbarPos("Val2", "Vals")
    val3 = cv2.getTrackbarPos("Val3", "Vals")
    if val1 % 2 == 0: val1 += 1
    if val3 % 2 == 0: val3 += 1
    imgThres = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY_INV, val1, val2)
    imgThres = cv2.medianBlur(imgThres, val3)
    kernel = np.ones((3, 3), np.uint8)
    imgThres = cv2.dilate(imgThres, kernel, iterations=1)

    checkSpaces()
    # Display Output

    cv2.imshow("Image", img)
    # cv2.imshow("ImageGray", imgThres)
    # cv2.imshow("ImageBlur", imgBlur)
    key = cv2.waitKey(1)
    if key == ord('r'):
        pass