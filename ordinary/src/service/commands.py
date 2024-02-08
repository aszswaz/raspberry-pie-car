from ..controller import car

ACTIONS = {
    # 停止
    0x0: car.stop,
    # 向左前移动
    0x1: car.left_front,
    # 向正前方移动
    0x2: car.forward,
    # 向右前方移动
    0x3: car.right_front,
    # 向左平移
    0x4: car.move_left,
    # 向右平移
    0x5: car.move_right,
    # 向左后方移动
    0x6: car.rear_left,
    # 向后方移动
    0x7: car.back,
    # 向右后方移动
    0x8: car.rear_right,
    # 左转
    0x9: car.trun_left,
    # 右转
    0xA: car.trun_right
}


def execute_command(command: int):
    ACTIONS[command]()
    return None
