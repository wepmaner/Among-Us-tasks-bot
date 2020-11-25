from PIL import Image, ImageGrab
from time import sleep
import cv2
import numpy as np
import os
import pyautogui
from config import *
from tasks import tasks_manager
from rooms import rooms_manager
from setuptools import setup


if MONITOR_RESOLUTION:
	from win32api import GetSystemMetrics
	win_x,win_y = GetSystemMetrics(0), GetSystemMetrics(1)

last_text = ""

while True:
	#print(pyautogui.position())
	im = ImageGrab.grab(bbox=(0,0,win_x,win_y)) 
	im.save("screen.png")

	img_rgb = cv2.imread("screen.png")
	screen = cv2.cvtColor(img_rgb,cv2.COLOR_RGB2GRAY)

	rooms_manager.main(screen,"skeld")
	tasks_manager.main(screen,im)

Gdx.app.exit();