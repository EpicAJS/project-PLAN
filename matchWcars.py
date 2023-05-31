import numpy as np
import cv2


img = cv2.imread('Images/EP3B&W.jpg', 0)
matchR = cv2.imread('Images/mEP3BWu.png', 0)
matchL = cv2.imread('Images/mEP3BWd.png', 0)

hR, wR = matchR.shape
hL, wL = matchL.shape
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED]

for method in methods:
    img2 = img.copy()

    resultR = cv2.matchTemplate(img2, matchR, method)
    resultL = cv2.matchTemplate(img2, matchL, method)

    threshold = .40
    locR = np.where(resultR >= threshold)
    locL = np.where(resultL >= threshold)

    for point in zip(*locR[::-1]):
        cv2.rectangle(img2, point, (point[0] + wR, point[1] + hR), (255, 0, 0), 1)
        cv2.putText(img, 'Empty Parking Spot', (10, 101),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    for point in zip(*locL[::-1]):
        cv2.rectangle(img2, point, (point[0] + wR, point[1] + hR), (255, 0, 0), 1)
        cv2.putText(img, 'Empty Parking Spot', (10, 101),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    corners = cv2.goodFeaturesToTrack(img2, 100, 0.11, 10)
    corners = np.int0(corners)

    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
