"""
    PyAutoGUI——做职场高手,让所有GUI自动化,击败无聊的办公室重复性操作
        GUI:图形用户界面(Graphical User Interface)
            例如 办公软件,音乐播放器...
        作用：自动控制鼠标和键盘。
        文档：https://pyautogui.readthedocs.io/en/latest/install.html
        安装步骤：
            1. win + r : 打开运行窗口
            2. 输入cmd : 打开命令行窗口
            3. 在命令行中输入：pip install pyautogui
"""
# 在命令行(终端)中执行以下2行代码,便可获取鼠标位置
import pyautogui
# 显示鼠标位置
# pyautogui.displayMousePosition()

# 鼠标移动：pyautogui.moveTo(x轴坐标,y轴坐标,持续时间)
pyautogui.moveTo(34,331,3) # 移动到酷狗
# 双击：pyautogui.doubleClick()
pyautogui.doubleClick() # 双击打开酷狗

# pyautogui.moveTo(549,665,3) # 移动到播放按钮
# pyautogui.click() # 单击播放

# 截取播放按钮图片
# pyautogui.screenshot("play.png",(510,641,50,50))

pyautogui.sleep(3) # 睡眠3秒(等待酷狗打开)

# 定位播放按钮
btn_pos = pyautogui.locateOnScreen("play.png")
point_pos = pyautogui.center(btn_pos)
# 移动到播放按钮
pyautogui.moveTo(point_pos.x,point_pos.y,3)
pyautogui.click() # 单击播放

pyautogui.hotkey("win","d")