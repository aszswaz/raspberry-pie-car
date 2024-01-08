from smbus import SMBus
import math
import time


"""
通过 I2C 操作 PCA9685 芯片
PCA9685 是一块输出 PWM 信号的芯片
"""

__MODE1 = 0x00

__SUBADR1 = 0x02
__SUBADR2 = 0x03
__SUBADR3 = 0x04

__PRESCALE = 0xFE

__LED0_ON_L = 0x06
__LED0_ON_H = 0x07
__LED0_OFF_L = 0x08
__LED0_OFF_H = 0x09

__ALLLED_ON_L = 0xFA
__ALLLED_ON_H = 0xFB
__ALLLED_OFF_L = 0xFC
__ALLLED_OFF_H = 0xFD


# PCA9685 的 I2C 地址
address: int = 0x40

bus: SMBus


def init():
    """
    初始化 PCA9685
    """
    # 打开 I2C，与 PCA9685 芯片建立通信
    global bus
    bus = SMBus(1)
    __write(__MODE1, 0x00)


def __write(reg, value):
    "Writes an 8-bit value to the specified register/address"
    bus.write_byte_data(address, reg, value)


def __read(reg):
    "Read an unsigned byte from the I2C device"
    result = bus.read_byte_data(address, reg)
    return result


def setPWMFreq(freq):
    """
    设置 PWM 频率
    """
    # 25MHz
    prescaleval = 25000000.0
    # 12-bit
    prescaleval /= 4096.0
    prescaleval /= float(freq)
    prescaleval -= 1.0
    prescale = math.floor(prescaleval + 0.5)

    oldmode = __read(__MODE1)
    # sleep
    newmode = (oldmode & 0x7F) | 0x10
    # go to sleep
    __write(__MODE1, newmode)
    __write(
        __PRESCALE, int(math.floor(prescale))
    )
    __write(__MODE1, oldmode)
    time.sleep(0.005)
    __write(__MODE1, oldmode | 0x80)


def setPWM(channel, on, off):
    """
    设置通道的 PWM 的占空比
    @channel: 通道
    @on:
    @off: PWM 占空比，因为 PCA9685 是 12 位分辨率，所以 off 的值 0 ~ 0xFFF 就代表了占空比 0 ~ 100
    """

    __write(
        __LED0_ON_L +
        4 * channel, on & 0xFF
    )
    __write(
        __LED0_ON_H + 4 * channel, on >> 8
    )
    # 输出 off 的低八位
    __write(
        __LED0_OFF_L + 4 * channel, off & 0xFF
    )
    # 输出 off 的高四位
    __write(
        __LED0_OFF_H + 4 * channel, off >> 8
    )


def setDutycycle(channel, pulse):
    setPWM(channel, 0, int(pulse * (4096 / 100)))
