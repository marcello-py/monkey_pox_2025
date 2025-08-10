import pyautogui as pa
from time import sleep

pa.PAUSE = 3

pa.press('win')
pa.write('firefox')
pa.press('ENTER')
pa.write('windy')

sleep(5)

pa.press('ENTER')

sleep(5)

pa.hotkey('F10')
pa.hotkey('ctrl', 't')
pa.write('')

sleep(5)

pa.press('ENTER')

sleep(20)

pa.click(x=428, y=215)
pa.write('marcelo')
pa.press('ENTER')
pa.hotkey('ctrl', 'v')