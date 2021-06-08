import webbrowser
import pyautogui
import time
from PIL import Image

webbrowser.open('https://www.youtube.com/results?search_query=cats', new = 2)
time.sleep(10)

screenshot = pyautogui.screenshot()
output_file = "Cats.png"
screenshot.save(output_file)

screenshot.show()
