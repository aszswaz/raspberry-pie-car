import RPi._GPIO as GPIO

import pca9685 as pca
from motor import Motor
from car_signal import CarSignal

# 行驶速度，建议在 30 ~ 99 以内取值
__speed = 50
# 小车的控制信号
__signal: CarSignal
# 小车的状态指示灯
__led_green = 6
__led_red = 5

# 左前轮
__left_front: Motor
# 右前轮
__right_front: Motor
# 左后轮
__left_back: Motor
# 右后轮
__right_back: Motor


def init():
    # 设置 PWM 频率
    pca.setPWMFreq(50)

    GPIO.setup(__led_green, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(__led_red, GPIO.OUT, initial=GPIO.LOW)

    global __left_front, __right_front, __left_back, __right_back
    __left_front = Motor(0x06, 0x0A, 0x0E)
    __right_front = Motor(0x1A, 0x12, 0x16)
    __left_back = Motor(0x1E, 0x26, 0x22)
    __right_back = Motor(0x32, 24, 25, True)

    set_signal(CarSignal.STOPED)


def set_signal(value: CarSignal):
    """
    设置小车的控制信号
    """
    global __signal
    __signal = value

    if value == CarSignal.READY:
        GPIO.output(__led_green, GPIO.HIGH)
        GPIO.output(__led_red, GPIO.LOW)
    elif value == CarSignal.STOPED:
        GPIO.output(__led_green, GPIO.LOW)
        GPIO.output(__led_red, GPIO.HIGH)
        stop()


def get_signal() -> CarSignal:
    return __signal


def forward():
    """
    前进
    """
    if __signal == CarSignal.STOPED:
        return
    __left_front.forward(__speed)
    __right_front.forward(__speed)
    __left_back.forward(__speed)
    __right_back.forward(__speed)
    pass


def back():
    """
    后退
    """
    if __signal == CarSignal.STOPED:
        return
    __left_front.back(__speed)
    __right_front.back(__speed)
    __left_back.back(__speed)
    __right_back.back(__speed)


def move_right():
    """
    向右平移
    """
    if __signal == CarSignal.STOPED:
        return
    __right_front.back(__speed)
    __right_back.forward(__speed)
    __left_front.forward(__speed)
    __left_back.back(__speed)


def move_left():
    """
    向左平移
    """
    if __signal == CarSignal.STOPED:
        return
    __right_front.forward(__speed)
    __right_back.back(__speed)
    __left_front.back(__speed)
    __left_back.forward(__speed)


def stop():
    __left_front.stop()
    __right_front.stop()
    __left_back.stop()
    __right_back.stop()
    pass
