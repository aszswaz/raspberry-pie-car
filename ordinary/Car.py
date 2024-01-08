import time
import RPi._GPIO as GPIO

import PCA9685 as pca
from Motor import Motor

# PWM 分辨率
resolution = 0xFFF

# 左前轮
left_front = Motor(0, 1, 2)


def init():
    pca.setPWMFreq(50)


def forward():
    # 左前轮前进
    left_front.speed = 50
    pass


def stop():
    left_front.speed = 0
    pass
