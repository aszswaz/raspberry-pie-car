import time
import RPi._GPIO as GPIO

import PCA9685 as pca
from Motor import Motor

# 行驶速度，建议在 30 ~ 99 以内取值
speed = 50

# 左前轮
left_front = Motor(0x06, 0x0A, 0x0E)
right_front = Motor(0x1A, 0x12, 0x16)
left_back = Motor(0x1E, 0x26, 0x22)
right_back = Motor(0x32, 24, 25, True)


def init():
    pca.setPWMFreq(50)


def forward():
    # 左前轮前进
    left_front.speed = speed
    right_front.speed = speed
    left_back.speed = speed
    right_back.speed = speed
    pass


def back():
    left_front.speed = -speed
    right_front.speed = -speed
    left_back.speed = -speed
    right_back.speed = -speed


def stop():
    left_front.speed = 0
    right_front.speed = 0
    left_back.speed = 0
    right_back.speed = 0
    pass
