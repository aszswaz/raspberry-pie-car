package cn.aszswaz.car

import android.Manifest.permission
import android.bluetooth.BluetoothManager
import android.content.Context
import android.content.pm.PackageManager.PERMISSION_GRANTED
import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat.checkSelfPermission

class MainActivity : AppCompatActivity() {
    companion object {
        val TAG = MainActivity::class.simpleName
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        try {
            val bthManager = getSystemService(Context.BLUETOOTH_SERVICE) as BluetoothManager
            val bthAdapter = bthManager.adapter
            val dev = bthAdapter.getRemoteDevice("D8:3A:DD:56:AF:08")
            if (checkSelfPermission(this, permission.BLUETOOTH) != PERMISSION_GRANTED) {
                return
            }
            dev.connectGatt(this, false, GattClient()).connect()
        } catch (e: Exception) {
            Log.e(MainActivity::class.simpleName, e.stackTraceToString())
        }
    }
}