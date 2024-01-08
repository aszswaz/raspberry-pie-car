#!/usr/bin/python3

import RPi._GPIO as GPIO
import time

import PCA9685
import Car as car

# 右侧和左侧红外避障传感器
sensorRight = 16
sensorLeft = 12
# 按键
btnPin = 19


def main():
    try:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(sensorRight, GPIO.IN)
        GPIO.setup(sensorLeft, GPIO.IN)
        GPIO.setup(
            btnPin, GPIO.IN,
            pull_up_down=GPIO.PUD_UP
        )
        PCA9685.init()
        car.init()

        car.forward()
        time.sleep(10)
    finally:
        car.stop()
        GPIO.cleanup()


if __name__ == "__main__":
    main()
