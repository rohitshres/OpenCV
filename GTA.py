import numpy as np
from PIL import ImageGrab
import cv2
import time


def process_img(original_image):
    process_img=cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
    process_img=cv2.Canny(process_img, threshold1=200,threshold2=300)
    return process_img




last_time=time.time()
while(True):
    screen=np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    # printscreen_numpy= np.array(printscreen_pil.getdata(),dtype='uint8').reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))
    new_screen=process_img(screen)
    cv2.imshow('window',new_screen)

    # cv2.imshow('window', cv2.cvtColor(screen,cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break