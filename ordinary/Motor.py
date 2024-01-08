import PCA9685 as pca


class Motor:
    """
    电机
    """

    def __init__(
            self,
            channel: int,
            ain1: int, ain2: int
    ) -> None:
        # 电机的 PWM 通道
        self.channel = channel
        self.ain1 = ain1
        self.ain2 = ain2
        self._speed = 0
        pass

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed: int):
        self._speed = speed

        if speed == 0:
            pca.setPWM(self.channel, 0, 0)
            return
        if speed > 0:
            # 前进
            pca.setPWM(self.ain1, 0, 4095)
            pca.setPWM(self.ain2, 0, 0)
        elif speed < 0:
            speed = -speed
            pca.setPWM(self.ain1, 0, 0)
            pca.setPWM(self.ain2, 0, 4095)
        pca.setDutycycle(self.channel, speed)
