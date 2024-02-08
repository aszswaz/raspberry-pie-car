import socket

from dbus import Bus
from dbus.service import Object, ObjectPath, method

from .constants import *


class BthAdvertisement(Object):
    """
    蓝牙广播
    """

    obj_path = ObjectPath(f"{BUS_NAMESPACE}/BthAdvertisement")
    obj_name = f"{BUS_NAME}.BthAdvertisement"

    # 广播数据包的类型
    ad_type = "peripheral"
    # 设备是否可被发现
    discoverable = True

    def __init__(self, bus: Bus) -> None:
        super().__init__(bus, self.obj_path, self.obj_name)
        self.local_name = socket.gethostname()
        return None

    @method(
        dbus_interface=DBUS_PROPERTIES,
        in_signature="s",
        out_signature="a{sv}"
    )
    def GetAll(self, _):
        return {
            "Type": self.ad_type,
            "Discoverable": self.discoverable,
            "LocalName": self.local_name
        }

    @method(
        dbus_interface=ADVERTISEMENT_INTERFACE,
        in_signature="",
        out_signature=""
    )
    def Release(self):
        print(f"{self.obj_path}: Released")
        return None
