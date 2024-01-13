#!/usr/bin/python3

import RPi._GPIO as GPIO
import time

from controller.car_signal import CarSignal
from controller import pca9685 as pca
from controller import car
from service.button import listen_button

# 右侧和左侧红外避障传感器
sensorRight = 16
sensorLeft = 12


def main():
    try:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(sensorRight, GPIO.IN)
        GPIO.setup(sensorLeft, GPIO.IN)

        pca.init()
        car.init()
        listen_button()
        car.set_signal(CarSignal.READY)

        while True:
            if car.get_signal() == CarSignal.STOPED:
                continue
            time.sleep(2)
            car.forward()
            time.sleep(5)
            car.stop()
            time.sleep(2)
            car.back()
            time.sleep(5)
            car.stop()
            time.sleep(2)
            car.move_right()
            time.sleep(5)
            car.stop()
            time.sleep(2)
            car.move_left()
            time.sleep(5)
            car.stop()
    finally:
        car.stop()
        GPIO.cleanup()


if __name__ == "__main__":
    main()
