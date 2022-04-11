import sys
import cv2
import numpy as np


file_name = sys.path[0]+ '/00aca42a24e4ea6066cca2546150c36e.dicom.png'
img = cv2.imread(file_name)

rows, cols, _ = img.shape
print(rows)
print(cols)

cut_image = img[769:1118, 1526:1826]
#cv2.rectangle(img, (1526, 769), (1826, 1118), (0, 255,0), 3)

cv2.imwrite('out.png',cut_image)