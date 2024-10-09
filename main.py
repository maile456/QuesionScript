import pyautogui
import pytesseract
import cv2
import time
import keyboard
import numpy as np

# 设置 Tesseract OCR 的路径
pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract-5.4.1\tesseract.exe'

# 定义屏幕区域的坐标
first_number_box = (282, 347, 100, 100)  # 第一个数字的区域
second_number_box = (459, 361, 200, 200)  # 第二个数字的区域
answer_box_location = (170, 888)  # 答案绘制位置

# 获取指定区域的数字
def get_number(box):
    screenshot = pyautogui.screenshot(region=box)  # 截取指定区域的屏幕
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # 转换为 BGR 格式
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换为灰度图
    number_text = pytesseract.image_to_string(gray, config='--psm 6')  # 提取文本
    return number_text.strip()  # 返回提取的数字

# 输入答案
def input_answer(answer):
    if answer == ">":
        draw_greater_than()  # 绘制大于符号
    elif answer == "<":
        draw_less_than()  # 绘制小于符号
    time.sleep(0.1)  # 暂停以确保绘制完成

# 绘制大于符号
def draw_greater_than():
    pyautogui.moveTo(170, 888)  # 移动到绘制位置
    pyautogui.mouseDown()  # 按下鼠标
    pyautogui.moveTo(250, 950, duration=0)  # 移动到大于符号的尖端位置
    pyautogui.moveTo(170, 1000, duration=0.2)  # 移动到结束位置
    pyautogui.mouseUp()  # 放开鼠标

# 绘制小于符号
def draw_less_than():
    pyautogui.moveTo(170, 888)  # 移动到绘制位置
    pyautogui.mouseDown()  # 按下鼠标
    pyautogui.moveTo(120, 950, duration=0)  # 移动到小于符号的尖端位置
    pyautogui.moveTo(170, 1000, duration=0.2)  # 移动到结束位置
    pyautogui.mouseUp()  # 放开鼠标

print("半糖脚本启动！")  # 启动脚本提示
while True:
    if keyboard.is_pressed('q'):  # 检查是否按下退出键
        print("退出程序")  # 提示退出程序
        break  # 退出循环
    num1_text = get_number(first_number_box)  # 获取第一个数字
    num2_text = get_number(second_number_box)  # 获取第二个数字

    # print(f"提取的数字: {num1_text}, {num2_text}")  # 可选：调试输出提取的数字

    if num1_text.isdigit() and num2_text.isdigit():  # 检查提取的文本是否为数字
        num1 = int(num1_text)  # 将文本转换为整数
        num2 = int(num2_text)  # 将文本转换为整数
        
        if num1 > num2:
            answer = ">"  # 如果第一个数字大于第二个，设置答案为大于
        elif num1 < num2:
            answer = "<"  # 如果第一个数字小于第二个，设置答案为小于
        
        input_answer(answer)  # 输入答案

    time.sleep(0.3)  # 等待题目刷新
