from ..controller import car
from .bluetooth import Service as BluetoothService
from .commands import *

"""
智能小车的控制方式：
1. 拓展板上的按钮控制，主要是切换手动和自动驾驶
2. 蓝牙控制
"""

_actions = {
    STOP: car.stop,
    LEFT_FRONT: None,
    FORWARD: car.forward,
    RIGHT_FRONT: None,
    PAN_LEFT: car.move_left,
    PAN_RIGHT: car.move_right,
    REAR_LEFT: None,
    BACKWARD: car.back,
    REAR_RIGHT: None,
    TURN_LEFT: None,
    TURN_RIGHT: None
}


def start():
    BluetoothService(execute_instructions).start()
    return None


def execute_instructions(command: int):
    _actions[command]()
    return None
