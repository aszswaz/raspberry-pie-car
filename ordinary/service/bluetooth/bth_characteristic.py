from dbus.service import Object, ObjectPath, method

from .constants import *
from ..commands import execute_command


class BthCharacteristic(Object):
    obj_path = ObjectPath(f"{BUS_NAMESPACE}/BthCharacteristic")
    obj_name = f"{BUS_NAME}.BthCharacteristic"

    def __init__(self, bus, svc_path) -> None:
        super().__init__(bus, self.obj_path, self.obj_name)
        self.svc_path = svc_path
        return None

    @method(
        dbus_interface=DBUS_PROPERTIES,
        in_signature="s",
        out_signature="a{sv}"
    )
    def GetAll(self, _) -> dict:
        return self.get_properties()

    @method(
        dbus_interface=GATT_CHARACTERISTIC_INTERFACE,
        in_signature="aya{sv}"
    )
    def WriteValue(self, value, _):
        """
        接收客户端传入的数据
        """
        try:
            buf = [int(item) for item in value]
            execute_command(buf[0])
        except Exception as err:
            print(err)
        return None

    def get_properties(self):
        return {
            "Service": self.svc_path,
            "UUID": CHR_UUID,
            "Flags": ["write"]
        }
