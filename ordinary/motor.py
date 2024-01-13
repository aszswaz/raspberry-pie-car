import RPi._GPIO as GPIO

import pca9685 as pca


class Motor:
    """
    电机
    """

    def __init__(
            self,
            reg_speed: int,
            reg_forward: int,
            reg_back: int,
            is_gpio=False
    ) -> None:
        # 控制电机转速的 PCA9685 寄存器
        self.reg_speed = reg_speed
        # 控制电机正转的 PCA9685（GPIO）寄存器
        self.reg_forward = reg_forward
        # 控制电机反转的 PCA9685（GPIO）寄存器
        self.reg_back = reg_back
        # reg_forward 和 reg_back 是否为 GPIO 寄存器
        self.is_gpio = is_gpio

        if is_gpio:
            GPIO.setup(reg_forward, GPIO.OUT)
            GPIO.setup(reg_back, GPIO.OUT)

    def forward(self, speed: int):
        # 设置前进速度
        pca.setDutycycle(self.reg_speed, speed)
        if self.is_gpio:
            GPIO.output(self.reg_forward, GPIO.HIGH)
            GPIO.output(self.reg_back, GPIO.LOW)
        else:
            # 打开前进电路
            pca.setPWM(self.reg_forward, 0, 4095)
            # 关闭后退电路
            pca.setPWM(self.reg_back, 0, 0)

    def back(self, speed: int):
        # 设置后退速度
        pca.setDutycycle(self.reg_speed, speed)
        if self.is_gpio:
            GPIO.output(self.reg_forward, GPIO.LOW)
            GPIO.output(self.reg_back, GPIO.HIGH)
        else:
            # 关闭前进电路
            pca.setPWM(self.reg_forward, 0, 0)
            # 开启后退电路
            pca.setPWM(self.reg_back, 0, 4095)

    def stop(self):
        pca.setDutycycle(self.reg_speed, 0)
        # 关闭前进和后退电路
        if self.is_gpio:
            GPIO.output(self.reg_forward, GPIO.LOW)
            GPIO.output(self.reg_back, GPIO.LOW)
        else:
            pca.setPWM(self.reg_forward, 0, 0)
            pca.setPWM(self.reg_back, 0, 0)
