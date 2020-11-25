import cv2
import os
import importlib
import numpy as np
import pyautogui
from time import sleep

def main(screen,image):
	tasks = os.listdir(f"tasks/tasks_img")
	for task in tasks:
		task_img = cv2.imread(f"tasks/tasks_img/{task}",0)
		res = cv2.matchTemplate(screen,task_img,cv2.TM_CCOEFF_NORMED)

		loc = np.where(res >= 0.7)
		for pt in zip(*loc[::-1]):
			task_name = task[:-4]
			print("Найдено задание:",task_name)
			
			try:
				lastmouse_posx, lastmouse_posy = pyautogui.position()
				importlib.import_module(f"tasks.tasks.{task_name}").main(image)
				pyautogui.moveTo(lastmouse_posx,lastmouse_posy)
				sleep(2)
			except Exception as e:
				print("Ошибка при выполнении задания:",e)	
			break

	