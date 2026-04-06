import pyautogui
import time

KEY_STRAFE_LEFT = 'z'
KEY_STRAFE_RIGHT = 'c'
KEY_FORWARD = 's'
KEY_BACK = 'x'
KEY_JUMP = 'space'

def move_forward():
    pyautogui.keyDown(KEY_FORWARD)

def stop_forward():
    pyautogui.keyUp(KEY_FORWARD)
 
def move_back():
    pyautogui.keyDown(KEY_BACK)

def stop_back():
    pyautogui.keyUp(KEY_BACK)

def strafe_left():
    pyautogui.keyDown(KEY_STRAFE_LEFT)

def stop_strafe_left():
    pyautogui.keyUp(KEY_STRAFE_LEFT)


def strafe_right():
    pyautogui.keyDown(KEY_STRAFE_RIGHT)

def stop_strafe_right():
    pyautogui.keyUp(KEY_STRAFE_RIGHT)

def jump():
    pyautogui.press(KEY_JUMP)

def bump_forward(duration=0.05):
    move_forward()
    time.sleep(duration)
    stop_forward()

def bump_back(duration=0.05):
    move_back()
    time.sleep(duration)
    stop_back()

def bump_strafe_left(duration=0.05):
    strafe_left()
    time.sleep(duration)
    stop_strafe_left()

def bump_strafe_right(duration=0.05):
    strafe_right()
    time.sleep(duration)
    stop_strafe_right()

#debug

if __name__ == "__main__":
    time.sleep(5)
    jump()
    print("Testing move functions...")
    bump_forward()
    time.sleep(1)
    bump_back()
    time.sleep(1)
    bump_strafe_left()
    time.sleep(1)
    bump_strafe_right()
    time.sleep(1)
    jump()
    print("Done testing.")





