import pyautogui as pg
import time

words = [_.strip('\n') for _ in open("words.txt").readlines()]

time.sleep(3)
for word in words:
  pg.typewrite(word)
  time.sleep(2.5)
