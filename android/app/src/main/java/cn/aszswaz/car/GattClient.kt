package cn.aszswaz.car

import android.annotation.SuppressLint
import android.bluetooth.BluetoothGatt
import android.bluetooth.BluetoothGattCallback
import android.bluetooth.BluetoothProfile
import android.os.Build
import android.util.Log
import java.util.UUID

val SERVICE_UUID: UUID = UUID.fromString("e95dd91d-251d-470a-a062-fa1922dfa9a8")
val CHR_UUID: UUID = UUID.fromString("e95d93ee-251d-470a-a062-fa1922dfa9a8")

@Suppress("DEPRECATION")
@SuppressLint("MissingPermission")
class GattClient : BluetoothGattCallback() {
    companion object {
        val TAG = GattClient::class.simpleName
    }

    /**
     * 蓝牙设备的连接和关闭
     */
    override fun onConnectionStateChange(gatt: BluetoothGatt?, status: Int, newState: Int) {
        Log.i(TAG, "onConnectionStateChange: $status")
        if (status == BluetoothGatt.GATT_SUCCESS) {
            if (newState == BluetoothProfile.STATE_CONNECTED) {
                Log.i(TAG, "connect success")
                // 查询 service
                gatt?.discoverServices()
            } else if (newState == BluetoothProfile.STATE_DISCONNECTED) {
                gatt?.close()
            }
        }
    }

    override fun onServicesDiscovered(gatt: BluetoothGatt?, status: Int) {
        Log.i(TAG, "service size: ${gatt?.services?.size}")
        gatt?.let {
            val svc = it.getService(SERVICE_UUID)
            val characteristic = svc.getCharacteristic(CHR_UUID)

            val msg = "Hello World".toByteArray()
            if (Build.VERSION.SDK_INT <= 30) {
                characteristic.value = msg
                it.writeCharacteristic(characteristic)
            }
        }
    }
}