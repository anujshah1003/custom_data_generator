# -*- coding: utf-8 -*-

import cv2

vid = r'D:\Trainings-2019\custom_data_generator\activity_recognition\UCF-101\test\Archery\v_Archery_g18_c03.avi'

cap = cv2.VideoCapture(vid)
ret=True
while ret:
    ret,img = cap.read()
    
    cv2.imshow('img',img)
    cv2.waitKey(10)
    
cap.release()
cv2.destroyAllWindows()
