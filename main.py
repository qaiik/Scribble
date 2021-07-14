import pyautogui as pg
import time

words = [_.strip('\n') for _ in open("words.txt").readlines()]

length = int(input("Length: "))


time.sleep(2)
for word in words:
  if len(word) == length:
    pg.typewrite(word, interval=0.00)
    pg.press("enter")
    time.sleep(0.7)
