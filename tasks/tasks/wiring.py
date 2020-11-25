from time import sleep
import pyautogui
#import keyboard


left_x = 400
right_x = 955

heights = [194, 328, 459, 590]

def get_pixel(im,x,y):
	return im.load()[x,y]

def main(image):
    pyautogui.PAUSE = 0
    right_color = dict()

    print("Starting Wiring Task")

    for y in heights:
        try:
            right_color.update({get_pixel(image,right_x,y):y})
        except Exception as e:
            print(e)
            pass
       	sleep(.06)
    print(right_color)

    for i in range(4):
        print(i)
        right_y = right_color[get_pixel(image,left_x,heights[i])]
        print(right_y)
        pyautogui.moveTo(left_x,heights[i])
        pyautogui.dragTo(right_x,right_y, .43, button='left')
        sleep(.06)
    print("Task complete")


'''def wiring_task():
    
    heights = [193, 328, 459, 590]
    if platform.system() == 'Linux':
        rightcolordict = {"RGB(red=255, green=0, blue=0)": 272, "RGB(red=0, green=0, blue=255)": 462,
                          "RGB(red=255, green=235, blue=4)": 647, "RGB(red=255, green=0, blue=255)": 833}
    elif platform.system() == 'Windows':
        rightcolordict = {"(255, 0, 0)": 272, "(0, 0, 255)": 462,
                          "(255, 235, 4)": 647, "(255, 0, 255)": 833}
    print("Starting Wiring Task")
    start_time = timeit.default_timer()
    # colordict[location"] = pixel color
    # to print 272,462,647,833 could be faster probably not
    for x in range(4):
        # 1905
        pyautogui.moveTo(390, heights[x])
        try:
            pyautogui.dragTo(943, rightcolordict[str(
                pyautogui.pixel(390, heights[x]))], .45, button='left')
            sleep(.05)
        except IndexError:
            print("no index try again")
        except KeyError:
            print("invalid key try again")
    print("Time to complete Wiring Task: " +
          str(round(timeit.default_timer() - start_time, 2)) + " seconds")'''


if __name__ == "__main__":
    main()
