import cv2
import os

def scale_image(file, size=(400, 400)):
    if len(file.split(".")) == 1 or file.split(".")[1] != "jpg":
        return

    img = cv2.imread(file)
    img_res = cv2.resize(img, dsize=size, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('scaled/' + file, img_res)
    print(file + " scaled...")

for file in os.listdir():
    print
    scale_image(file)