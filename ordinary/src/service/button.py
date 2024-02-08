"""
通过拓展板上的按钮切换手动和自动控制
"""

from threading import Thread
import time

import RPi._GPIO as GPIO

from controller import car
from controller.car_signal import CarSignal

# 按键
__BTN_PIN = 19


class ListenButton(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self) -> None:
        """
        监听按键，切换小车的运行状态
        """
        is_start = True
        while True:
            time.sleep(1)
            wait_button()
            is_start = not is_start
            if is_start:
                car.set_signal(CarSignal.READY)
            else:
                car.set_signal(CarSignal.STOPED)


def listen_button():
    # 初始化按钮的 GPIO，并上拉电阻保护树莓派
    GPIO.setup(__BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    wait_button()
    t = ListenButton()
    t.start()


def wait_button():
    # 等待用户按下按钮
    GPIO.wait_for_edge(__BTN_PIN, GPIO.RISING)
