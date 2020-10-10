import cv2
from time import sleep
from PIL import Image
from collections import Counter
from webcolors import rgb_to_name
from config import *

cv2.namedWindow("preview")
camera = cv2.VideoCapture(0)

x = 100
y = 300

if camera.isOpened(): # try to get the first frame
	rval, frame = camera.read()
else:
	rval = False

def check_color(frame):
	cv2.imwrite(current_img_dir,frame)
	crop = frame[x:y,x:y].copy()
	cv2.imwrite("crop.png",crop)
	img = Image.open(crop_img_dir)
	colors = Counter(img.getdata()) # dict: color -> number
	_colors = sorted(colors, key=colors.get, reverse=True)
	for color in _colors:
		try:
			print(rgb_to_name(color))
		except:
			continue

while rval:
	cv2.rectangle(frame,(x,x),(y,y),(0,0,255),3)
	cv2.imshow("preview", frame)
	rval, frame = camera.read()
	check_color(frame)
	key = cv2.waitKey(20)
	if key == 27: # exit on ESC
		break

camera.release()
cv2.destroyWindow("preview")
