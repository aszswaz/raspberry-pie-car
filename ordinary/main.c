#include <stdio.h>
#include <unistd.h>

#include <sys/socket.h>

#include <bluetooth/bluetooth.h>
#include <bluetooth/rfcomm.h>

#include <wiringPi.h>

// GPIO 的 WiringPi 编码
#define RIGHT_FORWARD 0
#define RIGHT_BACK    1
#define LEFT_FORWARD  2
#define LEFT_BACK     3

int sock = 0;

int init() {
    int code = 0;
    struct sockaddr_rc loc_addr = {};

    if (wiringPiSetup() < 0) return 1;
    
    pinMode(RIGHT_FORWARD, OUTPUT);
    pinMode(RIGHT_BACK, OUTPUT);
    pinMode(LEFT_FORWARD, OUTPUT);
    pinMode(LEFT_BACK, OUTPUT);

    sock = socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM);
    if (!sock) return 1;
    loc_addr.rc_family = AF_BLUETOOTH;
    loc_addr.rc_bdaddr = *BDADDR_ANY;
    loc_addr.rc_channel = (uint8_t)29;
    code = bind(sock, (struct sockaddr *)&loc_addr, sizeof(loc_addr));
    if (code) return 1;
    listen(sock, 1);
    return 0;
}

int main() {
    int client;
    char command;

    if (init()) return 1;

    /*
    digitalWrite(RIGHT_FORWARD, 0);
    digitalWrite(RIGHT_BACK, 0);
    digitalWrite(LEFT_FORWARD, 0);
    digitalWrite(LEFT_BACK, 0);
    */

    while(1) {
        client = accept(sock, NULL, NULL);
        while(read(client, &command, sizeof(command)) != -1) {
            switch(command) {
            case 0:
                // 停止
                digitalWrite(RIGHT_FORWARD, 0);
                digitalWrite(RIGHT_BACK, 0);
                digitalWrite(LEFT_FORWARD, 0);
                digitalWrite(LEFT_BACK, 0);
                break;
            case 1:
                // 向前
                digitalWrite(RIGHT_FORWARD, 1);
                digitalWrite(RIGHT_BACK, 0);
                digitalWrite(LEFT_FORWARD, 1);
                digitalWrite(LEFT_BACK, 0);
                break;
            case 2:
                // 向后
                digitalWrite(RIGHT_FORWARD, 0);
                digitalWrite(RIGHT_BACK, 1);
                digitalWrite(LEFT_FORWARD, 0);
                digitalWrite(LEFT_BACK, 1);
                break;
            case 3:
                // 向左
                digitalWrite(RIGHT_FORWARD, 1);
                digitalWrite(RIGHT_BACK, 0);
                digitalWrite(LEFT_FORWARD, 0);
                digitalWrite(LEFT_BACK, 1);
                break;
            case 4:
                // 向右
                digitalWrite(RIGHT_FORWARD, 0);
                digitalWrite(RIGHT_BACK, 1);
                digitalWrite(LEFT_FORWARD, 1);
                digitalWrite(LEFT_BACK, 0);
                break;
            }
        }
        close(client);
    }
}
