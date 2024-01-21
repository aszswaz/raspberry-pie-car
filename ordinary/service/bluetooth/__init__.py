from threading import Thread

from dbus.mainloop.glib import DBusGMainLoop
import dbus
from dbus import Bus
from gi.repository import GLib


from .bth_advertisement import BthAdvertisement
from .constants import *
from .bth_application import BthApplication


class Service(Thread):
    def run(self) -> None:
        # 开启蓝牙 GATT 监听
        DBusGMainLoop(set_as_default=True)
        bus = dbus.SystemBus()

        start_advertisement(bus)
        start_gatt(bus)
        GLib.MainLoop().run()
        return None


def start_advertisement(bus: Bus):
    """
    启动广播告知 GATT 服务的存在
    """
    adv_interface = dbus.Interface(
        bus.get_object(BLUEZ_SERVICE_NAME, ADAPTER_PATH),
        ADVERTISING_MANAGER_INTERFACE
    )
    adv = BthAdvertisement(bus)
    adv_interface.RegisterAdvertisement(
        adv.obj_path, {},
        reply_handler=register_ad_cb,
        error_handler=register_ad_error_cb
    )
    return None


def start_gatt(bus: Bus):
    """
    通过蓝牙的 GATT 协议接收控制指令
    """
    service_manager = dbus.Interface(
        bus.get_object(BLUEZ_SERVICE_NAME, ADAPTER_PATH),
        constants.GATT_MANAGER_INTERFACE
    )

    app = BthApplication(bus)
    service_manager.RegisterApplication(
        app.obj_path, {},
        reply_handler=register_app,
        error_handler=register_app_error
    )
    return None


def register_app():
    print("Bluetooth GATT application registered")
    return None


def register_app_error(error):
    print("Failed to register Bluetooth application:", error)
    return None


def register_ad_cb():
    print('Advertisement registered OK')


def register_ad_error_cb(error):
    print('Error: Failed to register advertisement: ' + str(error))
