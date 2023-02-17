import pyautogui
import time

pyautogui.position ()

def Click (x, y):
    pyautogui.click (x, y)
    pyautogui.click ()
    Click (1284, 392)

def Fill (x, y, text):
    Click (x, y)
    time.sleep (5) 
    pyautogui.write (text)

pyautogui.position ()
pyautogui.position ()

def Auto (Food, Other):
    Fill (1284, 392, Food)
    Fill (1284, 538, Other)
    Click (1264, 624)

Auto ('Kor Kao', 'KaoPaiNaiHuaJai')