#!/usr/bin/python3

import RPi._GPIO as GPIO

from .controller.car_signal import CarSignal
from .controller import pca9685 as pca
from .controller import car
from .service import start

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
        car.set_signal(CarSignal.READY)

        start()
    finally:
        car.stop()
        GPIO.cleanup()


if __name__ == "__main__":
    main()
