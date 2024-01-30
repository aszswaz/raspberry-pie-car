package cn.aszswaz.car

import android.Manifest.permission
import android.annotation.SuppressLint
import android.bluetooth.BluetoothManager
import android.content.Context
import android.content.pm.PackageManager.PERMISSION_GRANTED
import android.os.Bundle
import android.os.Handler
import android.util.Log
import android.view.MotionEvent
import android.view.View
import android.view.View.OnClickListener
import android.view.View.OnTouchListener
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat.checkSelfPermission

class MainActivity : AppCompatActivity(), OnTouchListener, OnClickListener {
    companion object {
        const val ADDRESS = "D8:3A:DD:56:AF:08"
    }

    private lateinit var handler: BluetoothHandler
    private lateinit var client: GattClient

    @SuppressLint("ClickableViewAccessibility")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        handler = BluetoothHandler(this)
        client = GattClient(handler)

        val buttons = intArrayOf(
            R.id.btn_left_front,
            R.id.btn_forward,
            R.id.btn_right_front,
            R.id.btn_pan_left,
            R.id.btn_stop,
            R.id.btn_pan_right,
            R.id.btn_rear_left,
            R.id.btn_backward,
            R.id.btn_right_back,
            R.id.btn_turn_left,
            R.id.btn_turn_right
        )
        for (id in buttons) findViewById<Button>(id).setOnTouchListener(this)

        val statusView = findViewById<TextView>(R.id.text_status)
        statusView.setOnClickListener(this)
    }

    @SuppressLint("ClickableViewAccessibility")
    override fun onTouch(v: View, event: MotionEvent): Boolean {
        // 按下按钮
        if (event.action == MotionEvent.ACTION_DOWN) {
            val command = when (v.id) {
                R.id.btn_left_front -> LEFT_FRONT
                R.id.btn_forward -> FORWARD
                R.id.btn_right_front -> RIGHT_FRONT
                R.id.btn_pan_left -> PAN_LEFT
                R.id.btn_stop -> STOP
                R.id.btn_pan_right -> PAN_RIGHT
                R.id.btn_rear_left -> REAR_LEFT
                R.id.btn_backward -> BACKWARD
                R.id.btn_right_back -> REAR_RIGHT
                R.id.btn_turn_left -> TURN_LEFT
                R.id.btn_turn_right -> TURN_RIGHT
                else -> STOP
            }
            client.writeByte(command)
        } else if (event.action == MotionEvent.ACTION_UP) {
            client.writeByte(STOP)
        }
        return false
    }

    override fun onClick(v: View?) {
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
}