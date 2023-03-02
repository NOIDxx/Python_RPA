import webbrowser
import time
import pyperclip as pc
import pyautogui as pg
from datetime import datetime

url = 'https://www.google.com/?client=safari'

webbrowser.open(url)
time.sleep (2)

keyword = 'สภาพอากาศสวรรคโลก'
pc.copy(keyword)
time.sleep(1)
pg.keyDown('command')
pg.press('v')
pg.keyUp('command')
pg.press('enter')
time.sleep(2)

position = (259,495, 1020, 545)
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M')
filename =('{} {}.png'.format(timestamp, keyword))
pg.screenshot(filename, region=position)
