import cv2
import time
from mail import mail
from random import randint

def motion():

    time.sleep(3)
    print('started')
    cam = cv2.VideoCapture(0)
    i =0
    first = None
    while True:
        ret,img = cam.read()
        img = cv2.resize(img,(480,360))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray,(21,21),0)
        
        k = cv2.waitKey(500)
        if(k==ord('q')):
           break
        ret1 , first = cam.read()
        first = cv2.resize(first,(480,360))
        gray1 = cv2.cvtColor(first,cv2.COLOR_BGR2GRAY)
        first = cv2.GaussianBlur(gray1,(21,21),0)
        
        a = cv2.absdiff(gray,first)
        b = cv2.countNonZero(a)
        
        print('\n\n\n\n')
        cv2.imshow('a',img)
        cv2.imshow('ay',first)
        if(b >60000 and i > 3):
            print(a)
            x= 'img' + str(randint(44343,432355545)) + '.jpg'
            cv2.imwrite('C:\\Users\\ayush\\Desktop\\pyth\\test\\{}'.format(x),img)
            mail(x)
            
            break

        k = cv2.waitKey(1)
        
        
        i+=1
        
        if(k==ord('q')):
            break

        
    del(cam)
    cv2.destroyAllWindows()
