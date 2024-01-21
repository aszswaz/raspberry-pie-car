BUS_NAME = "cn.aszswaz.car"
BUS_NAMESPACE = "/cn/aszswaz/car"
SERVICE_UUID = "e95dd91d-251d-470a-a062-fa1922dfa9a8"
CHR_UUID = "e95d93ee-251d-470a-a062-fa1922dfa9a8"

BLUEZ_SERVICE_NAME = "org.bluez"
BLUEZ_NAMESPACE = "/org/bluez"
ADAPTER_NAME = "hci0"
ADAPTER_PATH = f"{BLUEZ_NAMESPACE}/{ADAPTER_NAME}"
ADVERTISEMENT_INTERFACE = BLUEZ_SERVICE_NAME + ".LEAdvertisement1"
ADVERTISING_MANAGER_INTERFACE = BLUEZ_SERVICE_NAME + ".LEAdvertisingManager1"

DBUS_PROPERTIES = "org.freedesktop.DBus.Properties"
DBUS_OM_IFACE = 'org.freedesktop.DBus.ObjectManager'

GATT_MANAGER_INTERFACE = BLUEZ_SERVICE_NAME + ".GattManager1"
GATT_SERVICE_INTERFACE = BLUEZ_SERVICE_NAME + ".GattService1"
GATT_CHARACTERISTIC_INTERFACE = BLUEZ_SERVICE_NAME + ".GattCharacteristic1"
GATT_DESCRIPTOR_INTERFACE = BLUEZ_SERVICE_NAME + ".GattDescriptor1"

callback = None


def set_callback(call):
    global callback
    callback = call
