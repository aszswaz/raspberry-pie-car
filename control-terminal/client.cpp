#include <iostream>

#include <windows.h>
#include <ws2bth.h>
#include <bluetoothapis.h>

#include "client.h"

#pragma comment(lib, "ws2_32.lib")
#pragma comment(lib, "bthprops.lib")

// 目标蓝牙设备地址
#define ADDRESS 0xD83ADD56AF08
// 要想目标设备发送的数据
#define MSG "Hello World!"
// RFCOMM 端口，取值范围：1 - 30
#define PORT 29

SOCKET sock = {};

#define SEND(value) send(sock, &value, sizeof(value), 0)

// 停止
const char STOP = 0;
// 向前
const char FORWARD = 1;
// 向后
const char BACKWARD = 2;
// 向左
const char LEFT = 3;
// 向右
const char RIGHT = 4;

int car_connect() {
    int code;
    WORD socketVersion = {};
    WSADATA sock_data = {};
    SOCKADDR_BTH addr = {};

    socketVersion = MAKEWORD(2, 2);
    code = WSAStartup(socketVersion, &sock_data);
    if (code) return 1;

    sock = socket(AF_BTH, SOCK_STREAM, BTHPROTO_RFCOMM);
    if (sock == INVALID_SOCKET) return 1;

    // 建立蓝牙 RFCOMM 连接
    addr.addressFamily = AF_BTH;
    addr.btAddr = ADDRESS;
    addr.port = PORT;
    code = connect(sock, (SOCKADDR *)&addr, sizeof(addr));
    if (code == SOCKET_ERROR) return 1;
    return 0;
}

void car_disconnect() {
    if (sock) closesocket(sock);
    WSACleanup();
}

void car_forward() {
    SEND(FORWARD);
}

void car_backward() {
    SEND(BACKWARD);
}

void car_left() {
    SEND(LEFT);
}

void car_right() {
    SEND(RIGHT);
}

void car_stop() {
    SEND(STOP);
}
