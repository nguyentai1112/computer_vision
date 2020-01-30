import pyautogui

from imagesearch import *
from time import sleep
import keyboard
import cv2

class PianoTiles:

    def __init__(self):
        #rectange that contains game's windows
        self.y1 = 140
        self.y2 = 630
        self.x1 = 320
        self.x2 = 650
        self.speed = 200 #toc do cua khung black drop, px/s

    def wait_to_start(self):
        start_time = time.time()
        pos = imagesearcharea("./image/start.png",self.x1, self.y1, self.x2, self.y2)
        interval = time.time() - start_time
        print("find start image takes %s seconds ---" % interval)

        if pos[0] != -1:
            print("position : ", pos[0], pos[1])
            pyautogui.moveTo(self.x1 + pos[0] + 50, self.y1 + pos[1] + 50)
            pyautogui.click()
            return True

        else:
            print("image not found")
            return False

    def play(self):

        start_time = time.time()
        pos = imagesearcharea("./image/black_area_new.png", self.x1 , self.y1, self.x2, self.y2, precision = 0.9)
        interval = time.time() - start_time
        print("find black area image takes %s seconds ---" % interval)

        if pos[0] != -1:
            print("position: ", self.x1 + pos[0], self.y1 + pos[1])
            #pyautogui.moveTo(self.x1 + pos[0] + 25, self.y1 + pos[1] + 150) #why 150
            start_time = time.time()
            pyautogui.moveTo(self.x1 + pos[0] + 27, self.y1 + pos[1] + 87 + int(interval*self.speed),duration=0.01)
            print("time to move takes %s seconds ---" % (time.time() - start_time))
            pyautogui.click(duration=0.1)
            print("time to move and click takes %s seconds ---" % (time.time() - start_time))

            #sys.exit(1)
            return True

        else:
            print("image not found")
            return False

    def crop(self, image):
        crop_img = image[self.y1:self.y2, self.x1:self.x2]
        cv2.imshow("cropped", crop_img)
        cv2.waitKey(0)


if __name__ == '__main__':
    game = PianoTiles()
    start_button_avaiable = False
    while start_button_avaiable != True:
        start_button_avaiable = game.wait_to_start()
        sleep(0.5)

    #sleep(1)
    is_running = True
    i=0
    pyautogui.PAUSE = 0
    while(i <10):

        is_running = game.play()
        if is_running:
            a = 1
        sleep(0.1)
        i = i + 1
