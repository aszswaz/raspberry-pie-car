from ..controller import car
from .bluetooth import Service as BluetoothService
from .commands import *

"""
智能小车的控制方式：
1. 拓展板上的按钮控制，主要是切换手动和自动驾驶
2. 蓝牙控制
"""


def start():
    BluetoothService().start()
    return None
