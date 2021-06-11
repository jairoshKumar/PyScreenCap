import webbrowser
import pyautogui
import time
from PIL import Image

# Variable
wait_time = 7 # in seconds
ok = False

# Get user inputs
sq = input("Enter Search Query:")

# File name input
output_file = input("Enter a title for the screenshot with the image extension:")

# Open browser
while (ok == False):
    wb = input("\nPlease select the preferred browser:\nPress 1 for chrome\nPress 2 for safari\n")
    if wb == '1':
        webbrowser.get("chrome").open('https://www.youtube.com/results?search_query='+sq)
        ok = True
        break
    elif wb == '2':
        webbrowser.get("safari").open('https://www.youtube.com/results?search_query='+sq)
        ok = True
        break
    else:
        print("\nPLEASE ENTER CORRECT INPUT!!")

# Wait
time.sleep(wait_time)

# Capture screen
screenshot = pyautogui.screenshot()
screenshot.save(output_file)
screenshot.show()
