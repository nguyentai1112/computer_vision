from imagesearch import *
from time import sleep

if __name__ == '__main__':
    sleep(2)

   # self.y1 = 140
    #self.y2 = 630
    #self.x1 = 500
    #self.x2 = 800
    x1 = 300
    y1 = 140
    x2 = 620
    y2 = 600
    start_time = time.time()
    pos = imagesearcharea("./image/start.png", x1, y1, x2, y2)
    #pos = imagesearch("./image/start.png")
    interval = time.time() - start_time
    print("--- %s seconds ---" % interval)

    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.moveTo(x1 + pos[0], y1+ pos[1])
        pyautogui.click()

    else:
        print("image not found")