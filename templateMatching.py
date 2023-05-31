import numpy as np
import cv2

# img_rgb = cv2.imread('emptp2.jpg')
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
img = cv2.imread('Images/E4B&W.png', 0)
matchR = cv2.imread('Images/matchE4B&W.png', 0)
matchL = cv2.imread('Images/matchE4B&W2.png', 0)

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

    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


