import webbrowser
import pyautogui
import time
from PIL import Image

# Variable
wait_time = 7 # in seconds

# Get user inputs
sq = input("Enter Search Query:")
wb = input("Preferred browser:")

# Open browser
webbrowser.get(wb).open('https://www.youtube.com/results?search_query='+sq)

# Wait
time.sleep(wait_time)

# Capture screen
screenshot = pyautogui.screenshot()
output_file = "Search Result.png"
screenshot.save(output_file)
screenshot.show()
