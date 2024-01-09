#include <iostream>
#include <conio.h>

#include "client.h"

#define UP 72
#define LEFT 75
#define RIGHT 77
#define DOWN 80
#define SPACE 32

int main() {
    int code;
    char command;

    // 与小车建立蓝牙连接
    code = car_connect();
    if (code) {
        std::cout << "connect error" << std::endl;
    }

    // 读取用户输入
    while((command = _getch()) != 0x1B) {
        // 如果读取到方向键
        if (command == -32) {
            command = _getch();
            switch (command) {
            case UP:
                car_forward();
                break;
            case LEFT:
                car_left();
                break;
            case RIGHT:
                car_right();
                break;
            case DOWN:
                car_backward();
                break;
            }
        } else if (command == SPACE) {
            car_stop();
        }
    }
    car_stop();
}