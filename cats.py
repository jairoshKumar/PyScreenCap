import webbrowser
import pyautogui
import time
from PIL import Image

webbrowser.open('https://www.youtube.com/results?search_query=cats', new = 2)
time.sleep(7)

screenshot = pyautogui.screenshot()
screenshot.save("Cats.png")

screenshot.show()
