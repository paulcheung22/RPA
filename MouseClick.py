import win32api
import win32con
import time
import traceback


def click(position):
    try:
        win32api.SetCursorPos(position)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        print(position)
    except:
        traceback.print_exc()
        

time.sleep(3)


page = []
# 设置鼠标移动到的位置
# 0：视频列表中第一个视频的位置；
pos_0 = [(880, 374)]
page.append(pos_0)
# 1：视频简介中的开始播放按钮位置；
#pos_1 = [(851, 679), (851, 654), (851, 629), (851, 604), (851, 596), (851, 573), (851, 548)]
pos_1 = [(851, 654), (851, 629), (851, 604), (851, 596), (851, 573), (851, 548)]
page.append(pos_1)
# 2：视频播放器中开始暂停键位置；
pos_2 = [(846, 150), (62, 546), (62, 546), (39, 413), (39, 413), (76, 637), (76, 637), (428, 132), (428, 132), (500, 491), (500, 491)]
page.append(pos_2)
# 3：视频播放器关闭按键位置；
pos_3 = [(821, 29)]
page.append(pos_3)
# 4：视频简介关闭按键位置；
pos_4 = [(469, 21), (469, 21)]
page.append(pos_4)
# 5：视频列表刷新按钮位置；
pos_5 = [(84, 55)]
page.append(pos_5)

#设置每个页面点击后，停留的时间；
sleepTime = []
for m in range((len(page))):
    sleepTime.append(1) #先设置默认值

sleepTime[1] = 2 # 1，特殊值；
sleepTime[2] = 6*60  # 2，特殊值；


# 大循环，重复点击视频列表第一个视频的次数
Count = 9999999

for k in range(Count):
    for i in range(len(page)):
        posInCurrPage = page[i]

        for j in range(len(posInCurrPage)):
            pos = posInCurrPage[j]
            time.sleep(0.5)
            click(pos)

        time.sleep(sleepTime[i])

    print("Count="+ str(k))
            
