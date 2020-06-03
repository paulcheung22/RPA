import win32api
import win32con
import time

time.sleep(10)

win32api.SetCursorPos([20,20])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

