import cv2
import easyocr
import imutils as imutils
import matplotlib.pyplot as plt
import numpy as np

# read image
image_path = 'test_img_rec.png'

img = cv2.imread(image_path)

# instance text detector
reader = easyocr.Reader(['en'], gpu=False)

# detect text on image
text_ = reader.readtext(img)

threshold = 0.25
# draw bbox and text
for t_, t in enumerate(text_):
    print(t)

    bbox, text, score = t

    if score > threshold:
        cv2.rectangle(img, (int(bbox[0][0]),int(bbox[0][1])), (int(bbox[2][0]),int(bbox[2][1])), (0, 255, 0), 5)
        cv2.putText(img, text, (int(bbox[0][0]),int(bbox[0][1])), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()


################################
#signature recognition matching
###############################

import cv2
from skimage.metrics import structural_similarity as ssim

# TODO add contour detection for enhanced accuracy

def match(path1, path2):
    # read the images
    img1 = cv2.imread('sig_test.png')
    img2 = cv2.imread('sig_test.png')
    # turn images to grayscale
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # resize images for comparison
    img1 = cv2.resize(img1, (300, 300))
    img2 = cv2.resize(img2, (300, 300))
    # display both images
    # cv2.imshow("One", img1)
    # cv2.imshow("Two", img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    similarity_value = "{:.2f}".format(ssim(img1, img2)*100)
    # print("answer is ", float(similarity_value),
    #       "type=", type(similarity_value))
    return float(similarity_value)

print(match('t','e'))

