package cn.aszswaz.car

import android.annotation.SuppressLint
import android.bluetooth.BluetoothGatt
import android.bluetooth.BluetoothGattCallback
import android.bluetooth.BluetoothGattCharacteristic
import android.bluetooth.BluetoothGattService
import android.bluetooth.BluetoothProfile
import android.os.Build
import java.util.UUID

@Suppress("DEPRECATION")
@SuppressLint("MissingPermission")
class GattClient : BluetoothGattCallback() {
    companion object {
        val SERVICE_UUID: UUID = UUID.fromString("e95dd91d-251d-470a-a062-fa1922dfa9a8")
        val CHR_UUID: UUID = UUID.fromString("e95d93ee-251d-470a-a062-fa1922dfa9a8")
    }

    private lateinit var gatt: BluetoothGatt
    private lateinit var svc: BluetoothGattService
    private lateinit var chr: BluetoothGattCharacteristic

    /**
     * 蓝牙设备的连接和关闭
     */
    override fun onConnectionStateChange(gatt: BluetoothGatt, status: Int, newState: Int) {
        if (status == BluetoothGatt.GATT_SUCCESS) {
            if (newState == BluetoothProfile.STATE_CONNECTED) {
                this.gatt = gatt
                // 查询 service
                gatt.discoverServices()
            } else if (newState == BluetoothProfile.STATE_DISCONNECTED) {
                gatt.close()
            }
        }
    }

    override fun onServicesDiscovered(gatt: BluetoothGatt, status: Int) {

        svc = gatt.getService(SERVICE_UUID)
        chr = svc.getCharacteristic(CHR_UUID)
    }

    fun writeByte(b: Byte) {
        if (!::chr.isInitialized) return
        if (Build.VERSION.SDK_INT <= 30) {
            chr.value = byteArrayOf(b)
            gatt.writeCharacteristic(chr)
        }
    }
}