from dbus import Bus
from dbus.service import Object, ObjectPath, method

from .bth_service import BthService
from .constants import *


class BthApplication(Object):
    obj_path = ObjectPath(f"{BUS_NAMESPACE}/BthApplication")
    obj_name = f"{BUS_NAME}.BthApplication"

    bth_service: BthService

    def __init__(self, bus: Bus, callback) -> None:
        super().__init__(bus, self.obj_path, self.obj_name)
        self.bth_service = BthService(bus, callback)
        return None

    @method(
        dbus_interface=DBUS_OM_IFACE,
        out_signature="a{oa{sa{sv}}}"
    )
    def GetManagedObjects(self):
        return {
            self.bth_service.obj_path: {
                GATT_SERVICE_INTERFACE: self.bth_service.get_properties()
            },
            self.bth_service.chtic.obj_path: {
                GATT_CHARACTERISTIC_INTERFACE: self.bth_service.chtic.get_properties()
            }
        }
