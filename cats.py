import webbrowser
import pyautogui
import time
from PIL import Image

# Variable
wait_time = 7 # in seconds

# Get user inputs
sq = input("Enter Search Query:")
wb = input("Preferred browser:")
output_file = input("Enter a title for the screenshot with the image extension:")

# Open browser
webbrowser.get(wb).open('https://www.youtube.com/results?search_query='+sq)

# Wait
time.sleep(wait_time)

# Capture screen
screenshot = pyautogui.screenshot()
screenshot.save(output_file)
screenshot.show()
