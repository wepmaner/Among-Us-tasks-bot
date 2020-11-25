import pyautogui
from time import sleep

x = 680
y = 460

def main(image):
	pyautogui.moveTo(x,y)
	sleep(0.2)
	pyautogui.click(x,y)
	#print(pyautogui.position())