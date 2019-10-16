 
import cv2
import os
import time


gif = cv2.VideoCapture('a.gif')

for k in range(1,4):

    for i in range(10):
        while(True):
            ret, frame=gif.read()
            time.sleep(0.1)
            if ret == True:
                cv2.imshow('Frame',frame)
                cv2.resizeWindow('Frame',200,200)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break
        gif = cv2.VideoCapture(str(k)+'.gif')



    

gif.release()
# Closes all the frames
cv2.destroyAllWindows()
