#pragma once

/**
 * 建立蓝牙连接
 * 
 * @return 0 成功建立蓝牙连接
 * @return 1 无法建立蓝牙连接
*/
int car_connect();

/**
 * 断开蓝牙连接
*/
void car_disconnect();

/**
 * 停止小车
*/
void car_stop();

/**
 * 小车向前运动
*/
void car_forward();

/**
 * 小车向后运动
*/
void car_backward();

/**
 * 小车向左旋转
*/
void car_left();

/**
 * 小车向右旋转
*/
void car_right();