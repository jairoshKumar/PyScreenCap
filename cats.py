import os
import sys
import webbrowser
import pyautogui
import time
import argparse
from PIL import Image

parser = argparse.ArgumentParser(description='Save webpage screenshots using query string.')
parser.add_argument('-q','--query', required=True,
                    help='a search string value')
parser.add_argument('-b','--browser', default='firefox', choices=['google-chrome', 'chrome', 'safari', 'firefox'],
                    help='preferred browser')
parser.add_argument('-o','--output-png', default='output.png',
                    help='Name for the screenshot image with extension')
parser.add_argument('-w','--wait-time', type=float, default=7.0,
                    help='wait time in seconds before taking the screen-shot')

args = parser.parse_args()

# Parse all args
wait_time = args.wait_time
sq = args.query
output_png = args.output_png
browser = args.browser

# Variable
ok = False
web_link = 'https://www.youtube.com/results?search_query='

def initialize_web_browser(browser_name):
    try:
        browser = webbrowser.get(browser_name)
    except Exception:
        print('Sorry {} is not supported'.format(browser_name))
        sys.exit()

    return browser


# Open browser
browser_obj = initialize_web_browser(browser)
browser_obj.open_new(web_link+sq)

# Wait
time.sleep(wait_time)

# Capture screen
screenshot = pyautogui.screenshot()
screenshot.save(output_png)
# screenshot.show()
os.system('open {}'.format(output_png))
