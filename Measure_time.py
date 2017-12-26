#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

import cv2
import time

img1 = cv2.imread('ml.jpg')

e1 = cv2.getTickCount()
t1 = time.time()
for i in xrange(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
t2 = time.time()
print(t2 - t1)
print(t)