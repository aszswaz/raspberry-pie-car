from ..controller import car

ACTIONS = {
    # 停止
    0x0: car.stop,
    # 向左前移动
    0x1: None,
    # 向正前方移动
    0x2: car.forward,
    # 向右前方移动
    0x3: None,
    # 向左平移
    0x4: car.move_left,
    # 向右平移
    0x5: car.move_right,
    # 向左后方移动
    0x6: None,
    # 向后方移动
    0x7: car.back,
    # 向右后方移动
    0x8: None,
    # 左转
    0x9: None,
    # 右转
    0xA: None
}


def execute_command(command: int):
    ACTIONS[command]()
    return None
