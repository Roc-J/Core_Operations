#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

import cv2
import numpy as np

img1 = cv2.imread('ml.jpg')
img2 = cv2.imread('opencv_log.jpg')

dst = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
cv2.imshow('result', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()