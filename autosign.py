import pyautogui
import time

# wechat in WOA
def openWechat():
    time.sleep(0.5)
    pyautogui.keyDown('winleft')
    time.sleep(0.05)
    pyautogui.keyUp('winleft')
    time.sleep(0.5)
    pyautogui.typewrite(['w','e','c','h','a','t','space'], interval=0.25)
    time.sleep(0.5)
    pyautogui.typewrite(['down','down'], interval=0.25)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(20)

def openJy(x, y):
    #time.sleep(0.5)
    #yautogui.moveTo(300,1000)
    pyautogui.click(x, y)
    time.sleep(0.5)
    pyautogui.click(x-100, y)
    time.sleep(0.5)
    pyautogui.typewrite(['j','i','u','y','i','n','z','h','e','n','j','i','n','g','space'], interval=0.25)
    time.sleep(0.5)
    pyautogui.click(x, y+198)

def position():
    print("按下Ctrl+c可退出...")

    try:
        while True:
            x, y = pyautogui.position()
            pstr = 'X: ' + str(x).rjust(4) + '    Y: ' + str(y).rjust(4)
            print(pstr)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print('\n')


if __name__ == "__main__":
    #openWechat()
    #openJy(570, 92)
    position()
