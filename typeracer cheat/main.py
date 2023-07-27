from PIL import Image, ImageGrab
import pytesseract
import pyautogui
import cv2
import keyboard
import time
from autocorrect import Speller

# getting the tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


# finding of the region to screenshot
get1 = input('\nPlace cursor at the top left of the region you want to capture, and then press enter \n')
pos1 = pyautogui.position()
get2 = input('Now place your cursor at the bottom right of the region you want to capture, and press enter \n')
pos2 = pyautogui.position()
width = pos2[0] - pos1[0]
height = pos2[1] - pos1[1]
pyautogui.screenshot("teehee.PNG", region=(pos1[0],pos1[1],width,height))
img = cv2.imread("teehee.PNG")

# convert the words in the text to strings
text = pytesseract.image_to_string(img)

time.sleep(2) # wait

text = " ".join(line.strip() for line in text.splitlines())

for i in text:  
    keyboard.press(i)
    keyboard.release(i)
    time.sleep(0.01)
