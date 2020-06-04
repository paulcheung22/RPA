import win32api
import win32con
import time


def click(postion):
    win32api.SetCursorPos(postion)
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)


time.sleep(3)

# 设置鼠标移动到的位置
# 行表示一个视频从列表选择到播放完毕所有要点击的位置
# 0：视频列表中第一个视频的位置；1：视频简介中的开始播放按钮位置；2：视频播放器中开始暂停键位置；
# 3：视频播放器关闭按键位置；4：视频简介关闭按键位置；5：视频列表打开按钮位置；
pos = [
    (855, 418), (887, 667), (77, 432), (1028, 18), (471, 19), (117, 17)
]

# 大循环，重复点击视频列表第一个视频的次数
Count = 50

for k in range(Count):
    for i in range(len(pos)):
        if (i % 6) <= 1:  # 0,1：前两步，移动到视频列表（默认视频列表网页已经打开），然后单击对应的视频项；
            click(pos[i])
            time.sleep(3)
        elif (i % 6) == 2:  # 2：第三步，由于可能会有网络卡顿，需要有间隔地双击播放器暂停和播放键；
            n = 0
            while True:
                n += 1
                click(pos[i])
                click(pos[i])
                time.sleep(10)

                if n > 2:  # 60*60/10:
                    break
        elif (i % 6) == 3:  # 3：第四步，关闭视频播放网页；
            click(pos[i])
            time.sleep(1)
        elif (i % 6) == 4:  # 4：第五步，关闭视频介绍网页；
            click(pos[i])
            time.sleep(1)
        elif (i % 6) == 5:  # 5：第六步，打开视频列表页；
            click(pos[i])
            time.sleep(1)
