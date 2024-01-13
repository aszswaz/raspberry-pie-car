from enum import Enum, auto


class CarSignal(Enum):
    """
    小车的控制信号
    """

    # 小车准备就绪
    READY = auto()
    # 小车已停止
    STOPED = auto()
