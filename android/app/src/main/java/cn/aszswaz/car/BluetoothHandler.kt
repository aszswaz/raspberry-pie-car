package cn.aszswaz.car

import android.os.Handler
import android.os.Looper
import android.os.Message
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import android.bluetooth.BluetoothProfile.*

/**
 * 处理蓝牙相关的 UI 事件
 */
class BluetoothHandler(
    app: AppCompatActivity
) : Handler(Looper.myLooper()!!) {

    private var statusView: TextView = app.findViewById(R.id.text_status)

    override fun handleMessage(msg: Message) {
        statusView.text = when (msg.what) {
            STATE_CONNECTING -> "正在连接小车"
            STATE_CONNECTED -> "小车已连接"
            STATE_DISCONNECTED -> "小车已断开连接"
            else -> "发生未知错误"
        }
    }
}