import RPi._GPIO as GPIO

from . import pca9685 as pca
from .motor import Motor
from .car_signal import CarSignal

# 行驶速度，建议在 30 ~ 99 以内取值
speed = 50
# 小车的控制信号
signal: CarSignal
# 小车的状态指示灯
__led_green = 6
__led_red = 5

# 左前轮
wheel_left_front: Motor
# 右前轮
wheel_right_front: Motor
# 左后轮
wheel_left_back: Motor
# 右后轮
wheel_right_back: Motor


def init():
    # 设置 PWM 频率
    pca.setPWMFreq(50)

    GPIO.setup(__led_green, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(__led_red, GPIO.OUT, initial=GPIO.LOW)

    global wheel_left_front, wheel_right_front, wheel_left_back, wheel_right_back
    wheel_left_front = Motor(0x06, 0x0A, 0x0E)
    wheel_right_front = Motor(0x1A, 0x12, 0x16)
    wheel_left_back = Motor(0x1E, 0x26, 0x22)
    wheel_right_back = Motor(0x32, 24, 25, True)

    set_signal(CarSignal.STOPED)


def set_signal(value: CarSignal):
    """
    设置小车的控制信号
    """
    global signal
    signal = value

    if value == CarSignal.READY:
        GPIO.output(__led_green, GPIO.HIGH)
        GPIO.output(__led_red, GPIO.LOW)
    elif value == CarSignal.STOPED:
        GPIO.output(__led_green, GPIO.LOW)
        GPIO.output(__led_red, GPIO.HIGH)
        stop()


def get_signal() -> CarSignal:
    return signal


def stop():
    wheel_left_front.stop()
    wheel_right_front.stop()
    wheel_left_back.stop()
    wheel_right_back.stop()
    pass


def left_front():
    """
    向左前方平移
    """
    if signal == CarSignal.STOPED:
        return
    wheel_left_front.stop()
    wheel_right_front.forward(speed)
    wheel_left_back.forward(speed)
    wheel_right_back.stop()


def forward():
    """
    前进
    """
    if signal == CarSignal.STOPED:
        return
    wheel_right_front.forward(speed)
    wheel_right_back.forward(speed)
    wheel_left_front.forward(speed)
    wheel_left_back.forward(speed)


def right_front():
    """
    向右前方平移
    """
    if signal == CarSignal.STOPED:
        return
    wheel_left_front.forward(speed)
    wheel_right_front.stop()
    wheel_left_back.stop()
    wheel_right_back.forward(speed)


def rear_left():
    """
    向左后方平移
    """
    if signal == CarSignal.STOPED:
        return
    wheel_left_front.back(speed)
    wheel_right_front.stop()
    wheel_left_back.stop()
    wheel_right_back.back(speed)


def back():
    """
    后退
    """
    if signal == CarSignal.STOPED:
        return
    wheel_left_front.back(speed)
    wheel_right_front.back(speed)
    wheel_left_back.back(speed)
    wheel_right_back.back(speed)


def rear_right():
    """
    向右后方平移
    """
    if signal == CarSignal.STOPED:
        return
    wheel_left_front.stop()
    wheel_right_front.back(speed)
    wheel_left_back.back(speed)
    wheel_right_back.stop()


def move_right():
    """
    向右平移
    """
    if signal == CarSignal.STOPED:
        return
    wheel_right_front.back(speed)
    wheel_right_back.forward(speed)
    wheel_left_front.forward(speed)
    wheel_left_back.back(speed)


def move_left():
    """
    向左平移
    """
    if signal == CarSignal.STOPED:
        return
    wheel_right_front.forward(speed)
    wheel_right_back.back(speed)
    wheel_left_front.back(speed)
    wheel_left_back.forward(speed)


def trun_left():
    """
    左转
    """
    if signal == CarSignal.STOPED:
        return
    wheel_left_front.back(speed)
    wheel_right_front.forward(speed)
    wheel_left_back.back(speed)
    wheel_right_back.forward(speed)


def trun_right():
    """
    右转
    """
    if signal == CarSignal.STOPED:
        return
    wheel_left_front.forward(speed)
    wheel_right_front.back(speed)
    wheel_left_back.forward(speed)
    wheel_right_back.back(speed)
