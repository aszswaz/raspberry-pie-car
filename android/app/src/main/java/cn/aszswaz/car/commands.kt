@file:Suppress("unused")

package cn.aszswaz.car

// 停止移动
const val STOP: Byte = 0x0

// 向左前移动
const val LEFT_FRONT: Byte = 0x1

// 向前移动
const val FORWARD: Byte = 0x2

// 向右前移动
const val RIGHT_FRONT: Byte = 0x3

// 向左平移
const val PAN_LEFT: Byte = 0x4

// 向右平移
const val PAN_RIGHT: Byte = 0x5

// 向左后方移动
const val REAR_LEFT: Byte = 0x6

// 向后方移动
const val BACKWARD: Byte = 0x7

// 向右后方移动
const val REAR_RIGHT: Byte = 0x8

// 左转
const val TURN_LEFT: Byte = 0x9

// 右转
const val TURN_RIGHT: Byte = 0xA