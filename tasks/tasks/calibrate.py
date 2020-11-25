import pyautogui
from time import sleep

x = 590

heights = [225, 415, 590]

click_x = 820
click_y= [220,415,590]

one = "(255, 227, 0)"

two = "(83, 98, 255)"

three = "(111,249,255)"

def main(image):
	while True:
		mouse_x, mouse_y = pyautogui.position()
		print(mouse_x, mouse_y)
		if str(pyautogui.pixel(x, heights[i]))
		if str(pyautogui.pixel(x, heights[i])) in "(0, 0, 0)":
			#pyautogui.moveTo(click_x,click_y[i])
			sleep(0.1)
			#pyautogui.click(click_x,click_y[i])
			break
	