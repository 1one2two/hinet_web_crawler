#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import time
import cv2
import os
import numpy as np

url = "http://hitc.hinet.net/newlogin/check/image.jsp"

def mse(im1, im2):
	err = np.sum((im1.astype('float') - im2.astype('float')) ** 2)
	err /= float(im1.shape[0] * im1.shape[0])
	
	return err

def get_image(index):
    urllib.request.urlretrieve(url, f"/home/user/桌面/hinet_img/{index}.jpg")
    img = cv2.imread(f"/home/user/桌面/hinet_img/{index}.jpg", cv2.IMREAD_GRAYSCALE)
    return img

def get_cut_img_loc(im):
    contours, hierarchy = cv2.findContours(im.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in contours], key=lambda x:x[1])
    arr = []

    for index, (c, _) in enumerate(cnts):
        (x, y, w, h) = cv2.boundingRect(c)
        try:
            if w > 5 and h > 10:
                add = True
                for i in range(0, len(arr)):
                    if abs(cnts[index][1] - arr[i][0]) <= 3:
                        add = False
                        break
                if add:
                    arr.append((x, y, w, h))
                    #print(x, y, w, h)
        except IndexError:
            pass
    return arr

def cut_image(im, arr):
    t = 0
    for i in arr:
        x = i[0]
        y = i[1]
        w = i[2]
        h = i[3]
        #cv2.imshow(str(x), im[y:y+h, x:x+w])
        img = im[y:y+h, x:x+w]
        img = cv2.resize(img, (9, 14))
        #cv2.imwrite(f"/home/user/桌面/hinet_img/num/{num}_{t}.jpg", img)
        t = t + 1
    return 0

def a(im, num):
    
    '''
    arr = []
    for tmp_png in [f for f in os.listdir('num') if not f.startswith('.')]:
        min_a = 9999999999
        min_png = None
        pic = cv2.imread('/home/user/桌面/hinet_img/num/' + tmp_png)
        
        #for directory in [f for f in os.listdir('num') if not f.startswith('.')]:
        for directory in range(10):
            print(directory)
            for png in [f for f in os.listdir('num/' + str(directory)) if not f.startswith('.')]:
                print(png)
                ref = cv2.imread('/home/user/桌面/hinet_img/num/' + str(directory) + '/' + png)
                if mse(ref, pic) < min_a:
                    min_a = mse(ref, pic)
                    min_png = directory
                    
        arr.append(min_png)
        print(''.join(arr))
    '''

#urllib.request.urlretrieve("http://hitc.hinet.net/newlogin/login_frame.jsp", f"./test.txt")
'''
for i in range(0, 100):
    im = cv2.imread(f"/home/user/桌面/hinet_img/{i}.jpg", cv2.IMREAD_GRAYSCALE)
    #cv2.imshow(f"{i}", im)
    retval, im = cv2.threshold(im, 130, 255, cv2.THRESH_BINARY_INV)
    #cv2.imshow(f"{i}_", im)
    a(im, i)
'''
cv2.waitKey(0)
cv2.destroyAllWindows() 