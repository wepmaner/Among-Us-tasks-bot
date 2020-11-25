from time import sleep
import pyautogui

y = 562
widths = [420,487,554,621,688,755,822]

def main(image):
	return 0
	for x in widths:
		print(pyautogui.pixel(x, y))
		#pyautogui.moveTo(x,y)
		sleep(.06)
	#while True:
	#	print(pyautogui.position())
