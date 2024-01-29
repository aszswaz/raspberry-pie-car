package cn.aszswaz.car

import android.Manifest.permission
import android.annotation.SuppressLint
import android.bluetooth.BluetoothManager
import android.content.Context
import android.content.pm.PackageManager.PERMISSION_GRANTED
import android.os.Bundle
import android.util.Log
import android.view.MotionEvent
import android.view.View
import android.view.View.OnTouchListener
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat.checkSelfPermission

class MainActivity : AppCompatActivity(), OnTouchListener {
    companion object {
        const val ADDRESS = "D8:3A:DD:56:AF:08"
    }

    private val client = GattClient()

    @SuppressLint("ClickableViewAccessibility")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val buttons = intArrayOf(
            R.id.btn_left_front,
            R.id.btn_forward,
            R.id.btn_right_front,
            R.id.btn_pan_left,
            R.id.btn_stop,
            R.id.btn_rear_left,
            R.id.btn_backward,
            R.id.btn_right_back,
            R.id.btn_turn_left,
            R.id.btn_turn_right
        )

        for (id in buttons) findViewById<Button>(id).setOnTouchListener(this)
    }

    override fun onStart() {
        super.onStart()

        try {
            if (checkSelfPermission(this, permission.BLUETOOTH) != PERMISSION_GRANTED) {
                return
            }
            val bthManager = getSystemService(Context.BLUETOOTH_SERVICE) as BluetoothManager
            val dev = bthManager.adapter.getRemoteDevice(ADDRESS)
            dev.connectGatt(this, false, client)
        } catch (e: Exception) {
            Log.e(MainActivity::class.simpleName, e.stackTraceToString())
        }
    }

    @SuppressLint("ClickableViewAccessibility")
    override fun onTouch(v: View, event: MotionEvent): Boolean {
        var command: Byte = STOP

        // 按下按钮
        if (
            event.action == MotionEvent.ACTION_DOWN
            || event.action == MotionEvent.ACTION_MOVE
        ) {
            when (v.id) {
                R.id.btn_left_front -> command = LEFT_FRONT
                R.id.btn_forward -> command = FORWARD
                R.id.btn_right_front -> command = RIGHT_FRONT
                R.id.btn_pan_left -> command = PAN_LEFT
                R.id.btn_stop -> command = STOP
                R.id.btn_rear_left -> command = REAR_LEFT
                R.id.btn_backward -> command = BACKWARD
                R.id.btn_right_back -> command = REAR_RIGHT
                R.id.btn_turn_left -> command = TURN_LEFT
                R.id.btn_turn_right -> command = TURN_RIGHT
            }
        }
        client.writeByte(command)
        return false
    }
}