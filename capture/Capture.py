# import the necessary packages
import numpy as np
import pyautogui
import imutils
import cv2
import time
from time import sleep
from imagesearch import *
class Capture:
    def __init__(self):
        self.test = 1

    def capture(self):
        sleep(2)
        total = 0
        for i in range (0,10):
            start_time = time.time()
            image = pyautogui.screenshot("image/" + str(i) + ".png")
            #image = pyautogui.screenshot()

            #image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            #cv2.imwrite("image/" + str(i) + ".png", image)

            
            interval = time.time() - start_time
            print("%s--- %s seconds ---" % (str(i), interval))
            total+= interval
        print("avg: %s" % (total/10.0))

    def test_crop(self):
        image = cv2.imread("image/5.png")
        y = 140
        x = 500
        h = 630 - y
        w = 800 - x
        crop = image[y:y + h, x:x + w]
        cv2.imshow('Image', crop)
        cv2.waitKey(0)
        #120, 620
        #500, 800

    def test_gray(self):
        template = "./image/black_area_new.png"
        #img_gray = cv2.imread("./image/black_area.png",0)
        #cv2.imwrite("./black_gray.png", img_gray)
        im = cv2.imread("./origin_gray.png")
        imagesearcharea(template,0,0,1000,1000,0.8, im)



if __name__ == '__main__':
    capture = Capture()
    #capture.test_crop()
    #capture.capture()
    capture.test_gray()