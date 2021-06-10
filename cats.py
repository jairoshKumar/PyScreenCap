import webbrowser
import pyautogui
import time
from PIL import Image

sq = input("Enter Search Query:")
wb = input("Preferred browser:")
webbrowser.get(wb).open('https://www.youtube.com/results?search_query='+sq)
time.sleep(7)

screenshot = pyautogui.screenshot()
output_file = "Search Result.png"
screenshot.save(output_file)

screenshot.show()
