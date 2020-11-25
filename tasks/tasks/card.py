import pyautogui
from time import sleep
from config import *



conduct_x, conduct_y = 1060, 300

def main(image):
	pyautogui.moveTo(PURSE_X,PURSE_Y)
	pyautogui.click(PURSE_X,PURSE_Y)
	sleep(0.5)
	pyautogui.moveTo(TERMINAL_LEFT_X,TERMINAL_LEFT_Y)

	pyautogui.dragTo(TERMINAL_RIGHT_X, TERMINAL_RIGHT_Y, SPEED_CARD, button='left')
	print(pyautogui.position())

	