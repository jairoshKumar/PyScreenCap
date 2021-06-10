import webbrowser
import pyautogui
import time
from PIL import Image

sq = input("Enter Search Query:")
wb = input("Preferred browser:")
output_file = input("Enter a title for the screenshot with the image extension:")

webbrowser.get(wb).open('https://www.youtube.com/results?search_query='+sq)
time.sleep(7)
screenshot = pyautogui.screenshot()
screenshot.save(output_file)
screenshot.show()
