from dbus.service import Object, ObjectPath, method
import dbus

from .constants import *
from .bth_characteristic import BthCharacteristic


class BthService(Object):
    obj_path = ObjectPath(f"{BUS_NAMESPACE}/BthService")
    obj_name = f"{BUS_NAME}.BthService"

    # org.bluez.GattService 的属性
    primary = True

    def __init__(self, bus, callback) -> None:
        super().__init__(bus, self.obj_path, self.obj_name)
        self.chtic = BthCharacteristic(bus, self.obj_path, callback)
        return None

    @method(
        dbus_interface=DBUS_PROPERTIES,
        in_signature="s",
        out_signature="a{sv}"
    )
    def GetAll(self, _) -> dict:
        """
        bluez 需要获取 BthService 的属性
        """
        return self.get_properties()

    def get_properties(self):
        return {
            "UUID": SERVICE_UUID,
            "Primary": self.primary,
            "Characteristics": dbus.Array(
                [self.chtic.obj_path],
                signature="o"
            )
        }
