import pytesseract
import cv2
import re

img = cv2.imread('dataset/driverlicense/2.jpg', 0)

ret, threshold_img = cv2.threshold(img, 127, 255, 0)

cv2.imwrite('threshold.jpg', threshold_img)

data = pytesseract.image_to_string(threshold_img, lang="eng")

print(re.search(r'5.\s\d\w{2}\s\d{6}', data))

