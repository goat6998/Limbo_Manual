

import pyautogui as gui
import sys

print('中断するにはCrt+Cを入力してください。')

test = 0.01
print(str(test).isdigit())
print(str(test).isdecimal())
print(str(test).isnumeric())

try:
    while True:
       x=input("取得したい箇所にカーソルを当てEnterキー押してください\n")
       print(gui.position())

       
except KeyboardInterrupt:
    print('\n終了')
    sys.exit()