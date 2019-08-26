import numpy as np
import cv2
import shutil
import requests
import time
from requests_html import HTML
from selenium import webdriver
from PIL import Image
from pytesseract import image_to_string
import urllib3,os

def star(url):
    driver = webdriver.PhantomJS(executable_path=r'/home/user/下載/phantomjs-2.1.1-linux-i686/bin/phantomjs')  # PhantomJs
    driver.get(url)
    time.sleep(1)
    pageSource = driver.page_source  # 取得網頁原始碼
    print(pageSource)

star('http://parent.hinet.net/tparent/create_tparent.jsp')

# 创建网络请求
http = urllib3.PoolManager()
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36','Content-type':'text/json'}
c = "_ga=GA1.2.1837160296.1564150000; uuid=7e3a7662-d521-4a69-8d01-ac10250f31af; _huid=7e3a7662-d521-4a69-8d01-ac10250f31af; adid=7e3a7662-d521-4a69-8d01-ac10250f31af; _gid=GA1.2.1483222754.1564296987; JSESSIONID=A14257A44624DE783A87516919A6DDD3"

res = http.request('get','http://parent.hinet.net/tparent/check/image.jsp',headers=header, cookies=c)

f = open('./ys.png','wb')
f.write(np.array(res.data))
f.close()

img = Image.open("ys.png")
cv2.imshow('i', np.array(img))

cv2.waitKey(0)
cv2.destroyAllWindows()
