import cv2
import os
import numpy as np
from PIL import ImageGrab


'''def get_room(screen):
	lobby_pach = "rooms/lobby.png"
	lobby = cv2.imread(lobby_pach,0)
	res = cv2.matchTemplate(screen,lobby,cv2.TM_CCOEFF_NORMED)

	loc = np.where(res >= 0.7)
	for pt in zip(*loc[::-1]):
		map_image = ImageGrab.grab(bbox=(92,45,374,72))
		map_name = pytesseract.image_to_string(map_image)
		print(map_name)
		return map_name
	return False'''

last_text = None
def main(screen,map_name):
	global last_text
	rooms = os.listdir(f"rooms/{map_name}")
	for room in rooms:
		room_img = cv2.imread(f"rooms/{map_name}/{room}",0)
		res = cv2.matchTemplate(screen,room_img,cv2.TM_CCOEFF_NORMED)
		#print(res)

		loc = np.where(res >= 0.7)
		for pt in zip(*loc[::-1]):
			if not last_text == room[:-4]:
				last_text = room[:-4]
				print(last_text)