# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.devices.bluetooth.genericattributeprofile
except Exception:
    pass

try:
    import winsdk.windows.devices.bluetooth.rfcomm
except Exception:
    pass

try:
    import winsdk.windows.devices.enumeration
except Exception:
    pass

try:
    import winsdk.windows.devices.radios
except Exception:
    pass

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.networking
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class BluetoothAddressType(enum.IntEnum):
    PUBLIC = 0
    RANDOM = 1
    UNSPECIFIED = 2

class BluetoothCacheMode(enum.IntEnum):
    CACHED = 0
    UNCACHED = 1

class BluetoothConnectionStatus(enum.IntEnum):
    DISCONNECTED = 0
    CONNECTED = 1

class BluetoothError(enum.IntEnum):
    SUCCESS = 0
    RADIO_NOT_AVAILABLE = 1
    RESOURCE_IN_USE = 2
    DEVICE_NOT_CONNECTED = 3
    OTHER_ERROR = 4
    DISABLED_BY_POLICY = 5
    NOT_SUPPORTED = 6
    DISABLED_BY_USER = 7
    CONSENT_REQUIRED = 8
    TRANSPORT_NOT_SUPPORTED = 9

class BluetoothLEPreferredConnectionParametersRequestStatus(enum.IntEnum):
    UNSPECIFIED = 0
    SUCCESS = 1
    DEVICE_NOT_AVAILABLE = 2
    ACCESS_DENIED = 3

class BluetoothMajorClass(enum.IntEnum):
    MISCELLANEOUS = 0
    COMPUTER = 1
    PHONE = 2
    NETWORK_ACCESS_POINT = 3
    AUDIO_VIDEO = 4
    PERIPHERAL = 5
    IMAGING = 6
    WEARABLE = 7
    TOY = 8
    HEALTH = 9

class BluetoothMinorClass(enum.IntEnum):
    UNCATEGORIZED = 0
    COMPUTER_DESKTOP = 1
    COMPUTER_SERVER = 2
    COMPUTER_LAPTOP = 3
    COMPUTER_HANDHELD = 4
    COMPUTER_PALM_SIZE = 5
    COMPUTER_WEARABLE = 6
    COMPUTER_TABLET = 7
    PHONE_CELLULAR = 1
    PHONE_CORDLESS = 2
    PHONE_SMART_PHONE = 3
    PHONE_WIRED = 4
    PHONE_ISDN = 5
    NETWORK_FULLY_AVAILABLE = 0
    NETWORK_USED01_TO17_PERCENT = 8
    NETWORK_USED17_TO33_PERCENT = 16
    NETWORK_USED33_TO50_PERCENT = 24
    NETWORK_USED50_TO67_PERCENT = 32
    NETWORK_USED67_TO83_PERCENT = 40
    NETWORK_USED83_TO99_PERCENT = 48
    NETWORK_NO_SERVICE_AVAILABLE = 56
    AUDIO_VIDEO_WEARABLE_HEADSET = 1
    AUDIO_VIDEO_HANDS_FREE = 2
    AUDIO_VIDEO_MICROPHONE = 4
    AUDIO_VIDEO_LOUDSPEAKER = 5
    AUDIO_VIDEO_HEADPHONES = 6
    AUDIO_VIDEO_PORTABLE_AUDIO = 7
    AUDIO_VIDEO_CAR_AUDIO = 8
    AUDIO_VIDEO_SET_TOP_BOX = 9
    AUDIO_VIDEO_HIFI_AUDIO_DEVICE = 10
    AUDIO_VIDEO_VCR = 11
    AUDIO_VIDEO_VIDEO_CAMERA = 12
    AUDIO_VIDEO_CAMCORDER = 13
    AUDIO_VIDEO_VIDEO_MONITOR = 14
    AUDIO_VIDEO_VIDEO_DISPLAY_AND_LOUDSPEAKER = 15
    AUDIO_VIDEO_VIDEO_CONFERENCING = 16
    AUDIO_VIDEO_GAMING_OR_TOY = 18
    PERIPHERAL_JOYSTICK = 1
    PERIPHERAL_GAMEPAD = 2
    PERIPHERAL_REMOTE_CONTROL = 3
    PERIPHERAL_SENSING = 4
    PERIPHERAL_DIGITIZER_TABLET = 5
    PERIPHERAL_CARD_READER = 6
    PERIPHERAL_DIGITAL_PEN = 7
    PERIPHERAL_HANDHELD_SCANNER = 8
    PERIPHERAL_HANDHELD_GESTURE = 9
    WEARABLE_WRISTWATCH = 1
    WEARABLE_PAGER = 2
    WEARABLE_JACKET = 3
    WEARABLE_HELMET = 4
    WEARABLE_GLASSES = 5
    TOY_ROBOT = 1
    TOY_VEHICLE = 2
    TOY_DOLL = 3
    TOY_CONTROLLER = 4
    TOY_GAME = 5
    HEALTH_BLOOD_PRESSURE_MONITOR = 1
    HEALTH_THERMOMETER = 2
    HEALTH_WEIGHING_SCALE = 3
    HEALTH_GLUCOSE_METER = 4
    HEALTH_PULSE_OXIMETER = 5
    HEALTH_HEART_RATE_MONITOR = 6
    HEALTH_HEALTH_DATA_DISPLAY = 7
    HEALTH_STEP_COUNTER = 8
    HEALTH_BODY_COMPOSITION_ANALYZER = 9
    HEALTH_PEAK_FLOW_MONITOR = 10
    HEALTH_MEDICATION_MONITOR = 11
    HEALTH_KNEE_PROSTHESIS = 12
    HEALTH_ANKLE_PROSTHESIS = 13
    HEALTH_GENERIC_HEALTH_MANAGER = 14
    HEALTH_PERSONAL_MOBILITY_DEVICE = 15

class BluetoothServiceCapabilities(enum.IntFlag):
    NONE = 0
    LIMITED_DISCOVERABLE_MODE = 0x1
    POSITIONING_SERVICE = 0x8
    NETWORKING_SERVICE = 0x10
    RENDERING_SERVICE = 0x20
    CAPTURING_SERVICE = 0x40
    OBJECT_TRANSFER_SERVICE = 0x80
    AUDIO_SERVICE = 0x100
    TELEPHONE_SERVICE = 0x200
    INFORMATION_SERVICE = 0x400

class BluetoothAdapter(_winrt.Object):
    bluetooth_address: _winrt.UInt64
    device_id: str
    is_advertisement_offload_supported: _winrt.Boolean
    is_central_role_supported: _winrt.Boolean
    is_classic_supported: _winrt.Boolean
    is_low_energy_supported: _winrt.Boolean
    is_peripheral_role_supported: _winrt.Boolean
    are_classic_secure_connections_supported: _winrt.Boolean
    are_low_energy_secure_connections_supported: _winrt.Boolean
    is_extended_advertising_supported: _winrt.Boolean
    max_advertisement_data_length: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothAdapter: ...
    @typing.overload
    @staticmethod
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[BluetoothAdapter]: ...
    @typing.overload
    @staticmethod
    def get_default_async() -> winsdk.windows.foundation.IAsyncOperation[BluetoothAdapter]: ...
    @typing.overload
    @staticmethod
    def get_device_selector() -> str: ...
    @typing.overload
    def get_radio_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.devices.radios.Radio]: ...

class BluetoothClassOfDevice(_winrt.Object):
    major_class: BluetoothMajorClass
    minor_class: BluetoothMinorClass
    raw_value: _winrt.UInt32
    service_capabilities: BluetoothServiceCapabilities
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothClassOfDevice: ...
    @typing.overload
    @staticmethod
    def from_parts(major_class: BluetoothMajorClass, minor_class: BluetoothMinorClass, service_capabilities: BluetoothServiceCapabilities) -> BluetoothClassOfDevice: ...
    @typing.overload
    @staticmethod
    def from_raw_value(raw_value: _winrt.UInt32) -> BluetoothClassOfDevice: ...

class BluetoothDevice(winsdk.windows.foundation.IClosable, _winrt.Object):
    bluetooth_address: _winrt.UInt64
    class_of_device: BluetoothClassOfDevice
    connection_status: BluetoothConnectionStatus
    device_id: str
    host_name: winsdk.windows.networking.HostName
    name: str
    rfcomm_services: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.devices.bluetooth.rfcomm.RfcommDeviceService]
    sdp_records: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.streams.IBuffer]
    device_information: winsdk.windows.devices.enumeration.DeviceInformation
    device_access_information: winsdk.windows.devices.enumeration.DeviceAccessInformation
    bluetooth_device_id: BluetoothDeviceId
    was_secure_connection_used_for_pairing: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothDevice: ...
    @typing.overload
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def from_bluetooth_address_async(address: _winrt.UInt64) -> winsdk.windows.foundation.IAsyncOperation[BluetoothDevice]: ...
    @typing.overload
    @staticmethod
    def from_host_name_async(host_name: winsdk.windows.networking.HostName) -> winsdk.windows.foundation.IAsyncOperation[BluetoothDevice]: ...
    @typing.overload
    @staticmethod
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[BluetoothDevice]: ...
    @typing.overload
    @staticmethod
    def get_device_selector() -> str: ...
    @typing.overload
    @staticmethod
    def get_device_selector_from_bluetooth_address(bluetooth_address: _winrt.UInt64) -> str: ...
    @typing.overload
    @staticmethod
    def get_device_selector_from_class_of_device(class_of_device: BluetoothClassOfDevice) -> str: ...
    @typing.overload
    @staticmethod
    def get_device_selector_from_connection_status(connection_status: BluetoothConnectionStatus) -> str: ...
    @typing.overload
    @staticmethod
    def get_device_selector_from_device_name(device_name: str) -> str: ...
    @typing.overload
    @staticmethod
    def get_device_selector_from_pairing_state(pairing_state: _winrt.Boolean) -> str: ...
    @typing.overload
    def get_rfcomm_services_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.devices.bluetooth.rfcomm.RfcommDeviceServicesResult]: ...
    @typing.overload
    def get_rfcomm_services_async(self, cache_mode: BluetoothCacheMode) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.devices.bluetooth.rfcomm.RfcommDeviceServicesResult]: ...
    @typing.overload
    def get_rfcomm_services_for_id_async(self, service_id: winsdk.windows.devices.bluetooth.rfcomm.RfcommServiceId) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.devices.bluetooth.rfcomm.RfcommDeviceServicesResult]: ...
    @typing.overload
    def get_rfcomm_services_for_id_async(self, service_id: winsdk.windows.devices.bluetooth.rfcomm.RfcommServiceId, cache_mode: BluetoothCacheMode) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.devices.bluetooth.rfcomm.RfcommDeviceServicesResult]: ...
    @typing.overload
    def request_access_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.devices.enumeration.DeviceAccessStatus]: ...
    @typing.overload
    def add_connection_status_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[BluetoothDevice, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_connection_status_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_name_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[BluetoothDevice, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_name_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_sdp_records_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[BluetoothDevice, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_sdp_records_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class BluetoothDeviceId(_winrt.Object):
    id: str
    is_classic_device: _winrt.Boolean
    is_low_energy_device: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothDeviceId: ...
    @typing.overload
    @staticmethod
    def from_id(device_id: str) -> BluetoothDeviceId: ...

class BluetoothLEAppearance(_winrt.Object):
    category: _winrt.UInt16
    raw_value: _winrt.UInt16
    sub_category: _winrt.UInt16
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEAppearance: ...
    @typing.overload
    @staticmethod
    def from_parts(appearance_category: _winrt.UInt16, appearance_sub_category: _winrt.UInt16) -> BluetoothLEAppearance: ...
    @typing.overload
    @staticmethod
    def from_raw_value(raw_value: _winrt.UInt16) -> BluetoothLEAppearance: ...

class BluetoothLEAppearanceCategories(_winrt.Object):
    barcode_scanner: _winrt.UInt16
    blood_pressure: _winrt.UInt16
    clock: _winrt.UInt16
    computer: _winrt.UInt16
    cycling: _winrt.UInt16
    display: _winrt.UInt16
    eye_glasses: _winrt.UInt16
    glucose_meter: _winrt.UInt16
    heart_rate: _winrt.UInt16
    human_interface_device: _winrt.UInt16
    keyring: _winrt.UInt16
    media_player: _winrt.UInt16
    outdoor_sport_activity: _winrt.UInt16
    phone: _winrt.UInt16
    pulse_oximeter: _winrt.UInt16
    remote_control: _winrt.UInt16
    running_walking: _winrt.UInt16
    tag: _winrt.UInt16
    thermometer: _winrt.UInt16
    uncategorized: _winrt.UInt16
    watch: _winrt.UInt16
    weight_scale: _winrt.UInt16
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEAppearanceCategories: ...

class BluetoothLEAppearanceSubcategories(_winrt.Object):
    barcode_scanner: _winrt.UInt16
    blood_pressure_arm: _winrt.UInt16
    blood_pressure_wrist: _winrt.UInt16
    card_reader: _winrt.UInt16
    cycling_cadence_sensor: _winrt.UInt16
    cycling_computer: _winrt.UInt16
    cycling_power_sensor: _winrt.UInt16
    cycling_speed_cadence_sensor: _winrt.UInt16
    cycling_speed_sensor: _winrt.UInt16
    digital_pen: _winrt.UInt16
    digitizer_tablet: _winrt.UInt16
    gamepad: _winrt.UInt16
    generic: _winrt.UInt16
    heart_rate_belt: _winrt.UInt16
    joystick: _winrt.UInt16
    keyboard: _winrt.UInt16
    location_display: _winrt.UInt16
    location_navigation_display: _winrt.UInt16
    location_navigation_pod: _winrt.UInt16
    location_pod: _winrt.UInt16
    mouse: _winrt.UInt16
    oximeter_fingertip: _winrt.UInt16
    oximeter_wrist_worn: _winrt.UInt16
    running_walking_in_shoe: _winrt.UInt16
    running_walking_on_hip: _winrt.UInt16
    running_walking_on_shoe: _winrt.UInt16
    sports_watch: _winrt.UInt16
    thermometer_ear: _winrt.UInt16
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEAppearanceSubcategories: ...

class BluetoothLEConnectionParameters(_winrt.Object):
    connection_interval: _winrt.UInt16
    connection_latency: _winrt.UInt16
    link_timeout: _winrt.UInt16
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEConnectionParameters: ...

class BluetoothLEConnectionPhy(_winrt.Object):
    receive_info: BluetoothLEConnectionPhyInfo
    transmit_info: BluetoothLEConnectionPhyInfo
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEConnectionPhy: ...

class BluetoothLEConnectionPhyInfo(_winrt.Object):
    is_coded_phy: _winrt.Boolean
    is_uncoded1_m_phy: _winrt.Boolean
    is_uncoded2_m_phy: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEConnectionPhyInfo: ...

class BluetoothLEDevice(winsdk.windows.foundation.IClosable, _winrt.Object):
    bluetooth_address: _winrt.UInt64
    connection_status: BluetoothConnectionStatus
    device_id: str
    gatt_services: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.devices.bluetooth.genericattributeprofile.GattDeviceService]
    name: str
    appearance: BluetoothLEAppearance
    bluetooth_address_type: BluetoothAddressType
    device_information: winsdk.windows.devices.enumeration.DeviceInformation
    device_access_information: winsdk.windows.devices.enumeration.DeviceAccessInformation
    bluetooth_device_id: BluetoothDeviceId
    was_secure_connection_used_for_pairing: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEDevice: ...
    @typing.overload
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def from_bluetooth_address_async(bluetooth_address: _winrt.UInt64) -> winsdk.windows.foundation.IAsyncOperation[BluetoothLEDevice]: ...
    @typing.overload
    @staticmethod
    def from_bluetooth_address_async(bluetooth_address: _winrt.UInt64, bluetooth_address_type: BluetoothAddressType) -> winsdk.windows.foundation.IAsyncOperation[BluetoothLEDevice]: ...
    @typing.overload
    @staticmethod
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[BluetoothLEDevice]: ...
    @typing.overload
    def get_connection_parameters(self) -> BluetoothLEConnectionParameters: ...
    @typing.overload
    def get_connection_phy(self) -> BluetoothLEConnectionPhy: ...
    @typing.overload
    @staticmethod
    def get_device_selector() -> str: ...
    @typing.overload
    @staticmethod
    def get_device_selector_from_appearance(appearance: BluetoothLEAppearance) -> str: ...
    @typing.overload
    @staticmethod
    def get_device_selector_from_bluetooth_address(bluetooth_address: _winrt.UInt64) -> str: ...
    @typing.overload
    @staticmethod
    def get_device_selector_from_bluetooth_address(bluetooth_address: _winrt.UInt64, bluetooth_address_type: BluetoothAddressType) -> str: ...
    @typing.overload
    @staticmethod
    def get_device_selector_from_connection_status(connection_status: BluetoothConnectionStatus) -> str: ...
    @typing.overload
    @staticmethod
    def get_device_selector_from_device_name(device_name: str) -> str: ...
    @typing.overload
    @staticmethod
    def get_device_selector_from_pairing_state(pairing_state: _winrt.Boolean) -> str: ...
    @typing.overload
    def get_gatt_service(self, service_uuid: uuid.UUID) -> winsdk.windows.devices.bluetooth.genericattributeprofile.GattDeviceService: ...
    @typing.overload
    def get_gatt_services_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.devices.bluetooth.genericattributeprofile.GattDeviceServicesResult]: ...
    @typing.overload
    def get_gatt_services_async(self, cache_mode: BluetoothCacheMode) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.devices.bluetooth.genericattributeprofile.GattDeviceServicesResult]: ...
    @typing.overload
    def get_gatt_services_for_uuid_async(self, service_uuid: uuid.UUID) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.devices.bluetooth.genericattributeprofile.GattDeviceServicesResult]: ...
    @typing.overload
    def get_gatt_services_for_uuid_async(self, service_uuid: uuid.UUID, cache_mode: BluetoothCacheMode) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.devices.bluetooth.genericattributeprofile.GattDeviceServicesResult]: ...
    @typing.overload
    def request_access_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.devices.enumeration.DeviceAccessStatus]: ...
    @typing.overload
    def request_preferred_connection_parameters(self, preferred_connection_parameters: BluetoothLEPreferredConnectionParameters) -> BluetoothLEPreferredConnectionParametersRequest: ...
    @typing.overload
    def add_connection_status_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[BluetoothLEDevice, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_connection_status_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_gatt_services_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[BluetoothLEDevice, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_gatt_services_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_name_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[BluetoothLEDevice, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_name_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_connection_parameters_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[BluetoothLEDevice, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_connection_parameters_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_connection_phy_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[BluetoothLEDevice, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_connection_phy_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class BluetoothLEPreferredConnectionParameters(_winrt.Object):
    connection_latency: _winrt.UInt16
    link_timeout: _winrt.UInt16
    max_connection_interval: _winrt.UInt16
    min_connection_interval: _winrt.UInt16
    balanced: BluetoothLEPreferredConnectionParameters
    power_optimized: BluetoothLEPreferredConnectionParameters
    throughput_optimized: BluetoothLEPreferredConnectionParameters
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEPreferredConnectionParameters: ...

class BluetoothLEPreferredConnectionParametersRequest(winsdk.windows.foundation.IClosable, _winrt.Object):
    status: BluetoothLEPreferredConnectionParametersRequestStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEPreferredConnectionParametersRequest: ...
    @typing.overload
    def close(self) -> None: ...

class BluetoothSignalStrengthFilter(_winrt.Object):
    sampling_interval: typing.Optional[winsdk.windows.foundation.TimeSpan]
    out_of_range_timeout: typing.Optional[winsdk.windows.foundation.TimeSpan]
    out_of_range_threshold_in_d_bm: typing.Optional[_winrt.Int16]
    in_range_threshold_in_d_bm: typing.Optional[_winrt.Int16]
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothSignalStrengthFilter: ...
    @typing.overload
    def __init__(self) -> None: ...

class BluetoothUuidHelper(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothUuidHelper: ...
    @typing.overload
    @staticmethod
    def from_short_id(short_id: _winrt.UInt32) -> uuid.UUID: ...
    @typing.overload
    @staticmethod
    def try_get_short_id(uuid: uuid.UUID) -> typing.Optional[_winrt.UInt32]: ...

