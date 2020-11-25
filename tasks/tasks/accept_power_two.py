from time import sleep
import pyautogui

x = 682
y = 389

def main(image):
	pyautogui.moveTo(x,y)
	sleep(0.4)
	pyautogui.click(x,y)
