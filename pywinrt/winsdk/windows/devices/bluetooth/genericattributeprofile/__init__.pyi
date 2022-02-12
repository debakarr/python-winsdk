# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.devices.bluetooth
except Exception:
    pass

try:
    import winsdk.windows.devices.enumeration
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
    import winsdk.windows.storage.streams
except Exception:
    pass

class GattCharacteristicProperties(enum.IntFlag):
    NONE = 0
    BROADCAST = 0x1
    READ = 0x2
    WRITE_WITHOUT_RESPONSE = 0x4
    WRITE = 0x8
    NOTIFY = 0x10
    INDICATE = 0x20
    AUTHENTICATED_SIGNED_WRITES = 0x40
    EXTENDED_PROPERTIES = 0x80
    RELIABLE_WRITES = 0x100
    WRITABLE_AUXILIARIES = 0x200

class GattClientCharacteristicConfigurationDescriptorValue(enum.IntEnum):
    NONE = 0
    NOTIFY = 1
    INDICATE = 2

class GattCommunicationStatus(enum.IntEnum):
    SUCCESS = 0
    UNREACHABLE = 1
    PROTOCOL_ERROR = 2
    ACCESS_DENIED = 3

class GattOpenStatus(enum.IntEnum):
    UNSPECIFIED = 0
    SUCCESS = 1
    ALREADY_OPENED = 2
    NOT_FOUND = 3
    SHARING_VIOLATION = 4
    ACCESS_DENIED = 5

class GattProtectionLevel(enum.IntEnum):
    PLAIN = 0
    AUTHENTICATION_REQUIRED = 1
    ENCRYPTION_REQUIRED = 2
    ENCRYPTION_AND_AUTHENTICATION_REQUIRED = 3

class GattRequestState(enum.IntEnum):
    PENDING = 0
    COMPLETED = 1
    CANCELED = 2

class GattServiceProviderAdvertisementStatus(enum.IntEnum):
    CREATED = 0
    STOPPED = 1
    STARTED = 2
    ABORTED = 3
    STARTED_WITHOUT_ALL_ADVERTISEMENT_DATA = 4

class GattSessionStatus(enum.IntEnum):
    CLOSED = 0
    ACTIVE = 1

class GattSharingMode(enum.IntEnum):
    UNSPECIFIED = 0
    EXCLUSIVE = 1
    SHARED_READ_ONLY = 2
    SHARED_READ_AND_WRITE = 3

class GattWriteOption(enum.IntEnum):
    WRITE_WITH_RESPONSE = 0
    WRITE_WITHOUT_RESPONSE = 1

class GattCharacteristic(_winrt.Object):
    protection_level: GattProtectionLevel
    attribute_handle: _winrt.UInt16
    characteristic_properties: GattCharacteristicProperties
    presentation_formats: winsdk.windows.foundation.collections.IVectorView[GattPresentationFormat]
    user_description: str
    uuid: uuid.UUID
    service: GattDeviceService
    @staticmethod
    def _from(obj: _winrt.Object) -> GattCharacteristic: ...
    @typing.overload
    @staticmethod
    def convert_short_id_to_uuid(short_id: _winrt.UInt16) -> uuid.UUID: ...
    @typing.overload
    def get_all_descriptors(self) -> winsdk.windows.foundation.collections.IVectorView[GattDescriptor]: ...
    @typing.overload
    def get_descriptors(self, descriptor_uuid: uuid.UUID) -> winsdk.windows.foundation.collections.IVectorView[GattDescriptor]: ...
    @typing.overload
    def get_descriptors_async(self) -> winsdk.windows.foundation.IAsyncOperation[GattDescriptorsResult]: ...
    @typing.overload
    def get_descriptors_async(self, cache_mode: winsdk.windows.devices.bluetooth.BluetoothCacheMode) -> winsdk.windows.foundation.IAsyncOperation[GattDescriptorsResult]: ...
    @typing.overload
    def get_descriptors_for_uuid_async(self, descriptor_uuid: uuid.UUID) -> winsdk.windows.foundation.IAsyncOperation[GattDescriptorsResult]: ...
    @typing.overload
    def get_descriptors_for_uuid_async(self, descriptor_uuid: uuid.UUID, cache_mode: winsdk.windows.devices.bluetooth.BluetoothCacheMode) -> winsdk.windows.foundation.IAsyncOperation[GattDescriptorsResult]: ...
    @typing.overload
    def read_client_characteristic_configuration_descriptor_async(self) -> winsdk.windows.foundation.IAsyncOperation[GattReadClientCharacteristicConfigurationDescriptorResult]: ...
    @typing.overload
    def read_value_async(self) -> winsdk.windows.foundation.IAsyncOperation[GattReadResult]: ...
    @typing.overload
    def read_value_async(self, cache_mode: winsdk.windows.devices.bluetooth.BluetoothCacheMode) -> winsdk.windows.foundation.IAsyncOperation[GattReadResult]: ...
    @typing.overload
    def write_client_characteristic_configuration_descriptor_async(self, client_characteristic_configuration_descriptor_value: GattClientCharacteristicConfigurationDescriptorValue) -> winsdk.windows.foundation.IAsyncOperation[GattCommunicationStatus]: ...
    @typing.overload
    def write_client_characteristic_configuration_descriptor_with_result_async(self, client_characteristic_configuration_descriptor_value: GattClientCharacteristicConfigurationDescriptorValue) -> winsdk.windows.foundation.IAsyncOperation[GattWriteResult]: ...
    @typing.overload
    def write_value_async(self, value: winsdk.windows.storage.streams.IBuffer) -> winsdk.windows.foundation.IAsyncOperation[GattCommunicationStatus]: ...
    @typing.overload
    def write_value_async(self, value: winsdk.windows.storage.streams.IBuffer, write_option: GattWriteOption) -> winsdk.windows.foundation.IAsyncOperation[GattCommunicationStatus]: ...
    @typing.overload
    def write_value_with_result_async(self, value: winsdk.windows.storage.streams.IBuffer) -> winsdk.windows.foundation.IAsyncOperation[GattWriteResult]: ...
    @typing.overload
    def write_value_with_result_async(self, value: winsdk.windows.storage.streams.IBuffer, write_option: GattWriteOption) -> winsdk.windows.foundation.IAsyncOperation[GattWriteResult]: ...
    @typing.overload
    def add_value_changed(self, value_changed_handler: winsdk.windows.foundation.TypedEventHandler[GattCharacteristic, GattValueChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_value_changed(self, value_changed_event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class GattCharacteristicUuids(_winrt.Object):
    heart_rate_measurement: uuid.UUID
    battery_level: uuid.UUID
    blood_pressure_feature: uuid.UUID
    blood_pressure_measurement: uuid.UUID
    body_sensor_location: uuid.UUID
    csc_feature: uuid.UUID
    csc_measurement: uuid.UUID
    glucose_feature: uuid.UUID
    glucose_measurement: uuid.UUID
    glucose_measurement_context: uuid.UUID
    heart_rate_control_point: uuid.UUID
    intermediate_cuff_pressure: uuid.UUID
    intermediate_temperature: uuid.UUID
    measurement_interval: uuid.UUID
    record_access_control_point: uuid.UUID
    rsc_feature: uuid.UUID
    rsc_measurement: uuid.UUID
    s_c_control_point: uuid.UUID
    sensor_location: uuid.UUID
    temperature_measurement: uuid.UUID
    temperature_type: uuid.UUID
    gap_peripheral_preferred_connection_parameters: uuid.UUID
    gap_peripheral_privacy_flag: uuid.UUID
    gap_reconnection_address: uuid.UUID
    gatt_service_changed: uuid.UUID
    hardware_revision_string: uuid.UUID
    hid_control_point: uuid.UUID
    hid_information: uuid.UUID
    ieee1107320601_regulatory_certification_data_list: uuid.UUID
    ln_control_point: uuid.UUID
    ln_feature: uuid.UUID
    local_time_information: uuid.UUID
    location_and_speed: uuid.UUID
    manufacturer_name_string: uuid.UUID
    model_number_string: uuid.UUID
    navigation: uuid.UUID
    new_alert: uuid.UUID
    pnp_id: uuid.UUID
    position_quality: uuid.UUID
    protocol_mode: uuid.UUID
    cycling_power_feature: uuid.UUID
    report: uuid.UUID
    report_map: uuid.UUID
    ringer_control_point: uuid.UUID
    ringer_setting: uuid.UUID
    scan_interval_window: uuid.UUID
    scan_refresh: uuid.UUID
    serial_number_string: uuid.UUID
    software_revision_string: uuid.UUID
    support_unread_alert_category: uuid.UUID
    supported_new_alert_category: uuid.UUID
    system_id: uuid.UUID
    time_accuracy: uuid.UUID
    time_source: uuid.UUID
    time_update_control_point: uuid.UUID
    time_update_state: uuid.UUID
    time_with_dst: uuid.UUID
    time_zone: uuid.UUID
    tx_power_level: uuid.UUID
    unread_alert_status: uuid.UUID
    alert_category_id: uuid.UUID
    alert_category_id_bit_mask: uuid.UUID
    alert_level: uuid.UUID
    alert_notification_control_point: uuid.UUID
    alert_status: uuid.UUID
    boot_keyboard_input_report: uuid.UUID
    boot_keyboard_output_report: uuid.UUID
    boot_mouse_input_report: uuid.UUID
    current_time: uuid.UUID
    cycling_power_control_point: uuid.UUID
    reference_time_information: uuid.UUID
    cycling_power_measurement: uuid.UUID
    cycling_power_vector: uuid.UUID
    date_time: uuid.UUID
    day_date_time: uuid.UUID
    day_of_week: uuid.UUID
    dst_offset: uuid.UUID
    exact_time256: uuid.UUID
    firmware_revision_string: uuid.UUID
    gap_appearance: uuid.UUID
    gap_device_name: uuid.UUID
    @staticmethod
    def _from(obj: _winrt.Object) -> GattCharacteristicUuids: ...

class GattCharacteristicsResult(_winrt.Object):
    characteristics: winsdk.windows.foundation.collections.IVectorView[GattCharacteristic]
    protocol_error: typing.Optional[_winrt.UInt8]
    status: GattCommunicationStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> GattCharacteristicsResult: ...

class GattClientNotificationResult(_winrt.Object):
    protocol_error: typing.Optional[_winrt.UInt8]
    status: GattCommunicationStatus
    subscribed_client: GattSubscribedClient
    bytes_sent: _winrt.UInt16
    @staticmethod
    def _from(obj: _winrt.Object) -> GattClientNotificationResult: ...

class GattDescriptor(_winrt.Object):
    protection_level: GattProtectionLevel
    attribute_handle: _winrt.UInt16
    uuid: uuid.UUID
    @staticmethod
    def _from(obj: _winrt.Object) -> GattDescriptor: ...
    @typing.overload
    @staticmethod
    def convert_short_id_to_uuid(short_id: _winrt.UInt16) -> uuid.UUID: ...
    @typing.overload
    def read_value_async(self) -> winsdk.windows.foundation.IAsyncOperation[GattReadResult]: ...
    @typing.overload
    def read_value_async(self, cache_mode: winsdk.windows.devices.bluetooth.BluetoothCacheMode) -> winsdk.windows.foundation.IAsyncOperation[GattReadResult]: ...
    @typing.overload
    def write_value_async(self, value: winsdk.windows.storage.streams.IBuffer) -> winsdk.windows.foundation.IAsyncOperation[GattCommunicationStatus]: ...
    @typing.overload
    def write_value_with_result_async(self, value: winsdk.windows.storage.streams.IBuffer) -> winsdk.windows.foundation.IAsyncOperation[GattWriteResult]: ...

class GattDescriptorUuids(_winrt.Object):
    characteristic_aggregate_format: uuid.UUID
    characteristic_extended_properties: uuid.UUID
    characteristic_presentation_format: uuid.UUID
    characteristic_user_description: uuid.UUID
    client_characteristic_configuration: uuid.UUID
    server_characteristic_configuration: uuid.UUID
    @staticmethod
    def _from(obj: _winrt.Object) -> GattDescriptorUuids: ...

class GattDescriptorsResult(_winrt.Object):
    descriptors: winsdk.windows.foundation.collections.IVectorView[GattDescriptor]
    protocol_error: typing.Optional[_winrt.UInt8]
    status: GattCommunicationStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> GattDescriptorsResult: ...

class GattDeviceService(winsdk.windows.foundation.IClosable, _winrt.Object):
    attribute_handle: _winrt.UInt16
    device_id: str
    uuid: uuid.UUID
    device: winsdk.windows.devices.bluetooth.BluetoothLEDevice
    parent_services: winsdk.windows.foundation.collections.IVectorView[GattDeviceService]
    device_access_information: winsdk.windows.devices.enumeration.DeviceAccessInformation
    session: GattSession
    sharing_mode: GattSharingMode
    @staticmethod
    def _from(obj: _winrt.Object) -> GattDeviceService: ...
    @typing.overload
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def convert_short_id_to_uuid(short_id: _winrt.UInt16) -> uuid.UUID: ...
    @typing.overload
    @staticmethod
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[GattDeviceService]: ...
    @typing.overload
    @staticmethod
    def from_id_async(device_id: str, sharing_mode: GattSharingMode) -> winsdk.windows.foundation.IAsyncOperation[GattDeviceService]: ...
    @typing.overload
    def get_all_characteristics(self) -> winsdk.windows.foundation.collections.IVectorView[GattCharacteristic]: ...
    @typing.overload
    def get_all_included_services(self) -> winsdk.windows.foundation.collections.IVectorView[GattDeviceService]: ...
    @typing.overload
    def get_characteristics(self, characteristic_uuid: uuid.UUID) -> winsdk.windows.foundation.collections.IVectorView[GattCharacteristic]: ...
    @typing.overload
    def get_characteristics_async(self) -> winsdk.windows.foundation.IAsyncOperation[GattCharacteristicsResult]: ...
    @typing.overload
    def get_characteristics_async(self, cache_mode: winsdk.windows.devices.bluetooth.BluetoothCacheMode) -> winsdk.windows.foundation.IAsyncOperation[GattCharacteristicsResult]: ...
    @typing.overload
    def get_characteristics_for_uuid_async(self, characteristic_uuid: uuid.UUID) -> winsdk.windows.foundation.IAsyncOperation[GattCharacteristicsResult]: ...
    @typing.overload
    def get_characteristics_for_uuid_async(self, characteristic_uuid: uuid.UUID, cache_mode: winsdk.windows.devices.bluetooth.BluetoothCacheMode) -> winsdk.windows.foundation.IAsyncOperation[GattCharacteristicsResult]: ...
    @typing.overload
    @staticmethod
    def get_device_selector_for_bluetooth_device_id(bluetooth_device_id: winsdk.windows.devices.bluetooth.BluetoothDeviceId) -> str: ...
    @typing.overload
    @staticmethod
    def get_device_selector_for_bluetooth_device_id(bluetooth_device_id: winsdk.windows.devices.bluetooth.BluetoothDeviceId, cache_mode: winsdk.windows.devices.bluetooth.BluetoothCacheMode) -> str: ...
    @typing.overload
    @staticmethod
    def get_device_selector_for_bluetooth_device_id_and_uuid(bluetooth_device_id: winsdk.windows.devices.bluetooth.BluetoothDeviceId, service_uuid: uuid.UUID) -> str: ...
    @typing.overload
    @staticmethod
    def get_device_selector_for_bluetooth_device_id_and_uuid(bluetooth_device_id: winsdk.windows.devices.bluetooth.BluetoothDeviceId, service_uuid: uuid.UUID, cache_mode: winsdk.windows.devices.bluetooth.BluetoothCacheMode) -> str: ...
    @typing.overload
    @staticmethod
    def get_device_selector_from_short_id(service_short_id: _winrt.UInt16) -> str: ...
    @typing.overload
    @staticmethod
    def get_device_selector_from_uuid(service_uuid: uuid.UUID) -> str: ...
    @typing.overload
    def get_included_services(self, service_uuid: uuid.UUID) -> winsdk.windows.foundation.collections.IVectorView[GattDeviceService]: ...
    @typing.overload
    def get_included_services_async(self) -> winsdk.windows.foundation.IAsyncOperation[GattDeviceServicesResult]: ...
    @typing.overload
    def get_included_services_async(self, cache_mode: winsdk.windows.devices.bluetooth.BluetoothCacheMode) -> winsdk.windows.foundation.IAsyncOperation[GattDeviceServicesResult]: ...
    @typing.overload
    def get_included_services_for_uuid_async(self, service_uuid: uuid.UUID) -> winsdk.windows.foundation.IAsyncOperation[GattDeviceServicesResult]: ...
    @typing.overload
    def get_included_services_for_uuid_async(self, service_uuid: uuid.UUID, cache_mode: winsdk.windows.devices.bluetooth.BluetoothCacheMode) -> winsdk.windows.foundation.IAsyncOperation[GattDeviceServicesResult]: ...
    @typing.overload
    def open_async(self, sharing_mode: GattSharingMode) -> winsdk.windows.foundation.IAsyncOperation[GattOpenStatus]: ...
    @typing.overload
    def request_access_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.devices.enumeration.DeviceAccessStatus]: ...

class GattDeviceServicesResult(_winrt.Object):
    protocol_error: typing.Optional[_winrt.UInt8]
    services: winsdk.windows.foundation.collections.IVectorView[GattDeviceService]
    status: GattCommunicationStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> GattDeviceServicesResult: ...

class GattLocalCharacteristic(_winrt.Object):
    characteristic_properties: GattCharacteristicProperties
    descriptors: winsdk.windows.foundation.collections.IVectorView[GattLocalDescriptor]
    presentation_formats: winsdk.windows.foundation.collections.IVectorView[GattPresentationFormat]
    read_protection_level: GattProtectionLevel
    static_value: winsdk.windows.storage.streams.IBuffer
    subscribed_clients: winsdk.windows.foundation.collections.IVectorView[GattSubscribedClient]
    user_description: str
    uuid: uuid.UUID
    write_protection_level: GattProtectionLevel
    @staticmethod
    def _from(obj: _winrt.Object) -> GattLocalCharacteristic: ...
    @typing.overload
    def create_descriptor_async(self, descriptor_uuid: uuid.UUID, parameters: GattLocalDescriptorParameters) -> winsdk.windows.foundation.IAsyncOperation[GattLocalDescriptorResult]: ...
    @typing.overload
    def notify_value_async(self, value: winsdk.windows.storage.streams.IBuffer) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[GattClientNotificationResult]]: ...
    @typing.overload
    def notify_value_async(self, value: winsdk.windows.storage.streams.IBuffer, subscribed_client: GattSubscribedClient) -> winsdk.windows.foundation.IAsyncOperation[GattClientNotificationResult]: ...
    @typing.overload
    def add_read_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[GattLocalCharacteristic, GattReadRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_read_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_subscribed_clients_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[GattLocalCharacteristic, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_subscribed_clients_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_write_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[GattLocalCharacteristic, GattWriteRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_write_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class GattLocalCharacteristicParameters(_winrt.Object):
    write_protection_level: GattProtectionLevel
    user_description: str
    static_value: winsdk.windows.storage.streams.IBuffer
    read_protection_level: GattProtectionLevel
    characteristic_properties: GattCharacteristicProperties
    presentation_formats: winsdk.windows.foundation.collections.IVector[GattPresentationFormat]
    @staticmethod
    def _from(obj: _winrt.Object) -> GattLocalCharacteristicParameters: ...
    @typing.overload
    def __init__(self) -> None: ...

class GattLocalCharacteristicResult(_winrt.Object):
    characteristic: GattLocalCharacteristic
    error: winsdk.windows.devices.bluetooth.BluetoothError
    @staticmethod
    def _from(obj: _winrt.Object) -> GattLocalCharacteristicResult: ...

class GattLocalDescriptor(_winrt.Object):
    read_protection_level: GattProtectionLevel
    static_value: winsdk.windows.storage.streams.IBuffer
    uuid: uuid.UUID
    write_protection_level: GattProtectionLevel
    @staticmethod
    def _from(obj: _winrt.Object) -> GattLocalDescriptor: ...
    @typing.overload
    def add_read_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[GattLocalDescriptor, GattReadRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_read_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_write_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[GattLocalDescriptor, GattWriteRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_write_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class GattLocalDescriptorParameters(_winrt.Object):
    write_protection_level: GattProtectionLevel
    static_value: winsdk.windows.storage.streams.IBuffer
    read_protection_level: GattProtectionLevel
    @staticmethod
    def _from(obj: _winrt.Object) -> GattLocalDescriptorParameters: ...
    @typing.overload
    def __init__(self) -> None: ...

class GattLocalDescriptorResult(_winrt.Object):
    descriptor: GattLocalDescriptor
    error: winsdk.windows.devices.bluetooth.BluetoothError
    @staticmethod
    def _from(obj: _winrt.Object) -> GattLocalDescriptorResult: ...

class GattLocalService(_winrt.Object):
    characteristics: winsdk.windows.foundation.collections.IVectorView[GattLocalCharacteristic]
    uuid: uuid.UUID
    @staticmethod
    def _from(obj: _winrt.Object) -> GattLocalService: ...
    @typing.overload
    def create_characteristic_async(self, characteristic_uuid: uuid.UUID, parameters: GattLocalCharacteristicParameters) -> winsdk.windows.foundation.IAsyncOperation[GattLocalCharacteristicResult]: ...

class GattPresentationFormat(_winrt.Object):
    description: _winrt.UInt16
    exponent: _winrt.Int32
    format_type: _winrt.UInt8
    namespace: _winrt.UInt8
    unit: _winrt.UInt16
    bluetooth_sig_assigned_numbers: _winrt.UInt8
    @staticmethod
    def _from(obj: _winrt.Object) -> GattPresentationFormat: ...
    @typing.overload
    @staticmethod
    def from_parts(format_type: _winrt.UInt8, exponent: _winrt.Int32, unit: _winrt.UInt16, namespace_id: _winrt.UInt8, description: _winrt.UInt16) -> GattPresentationFormat: ...

class GattPresentationFormatTypes(_winrt.Object):
    bit2: _winrt.UInt8
    boolean: _winrt.UInt8
    d_uint16: _winrt.UInt8
    float: _winrt.UInt8
    float32: _winrt.UInt8
    float64: _winrt.UInt8
    nibble: _winrt.UInt8
    s_float: _winrt.UInt8
    s_int12: _winrt.UInt8
    s_int128: _winrt.UInt8
    s_int16: _winrt.UInt8
    s_int24: _winrt.UInt8
    s_int32: _winrt.UInt8
    s_int48: _winrt.UInt8
    s_int64: _winrt.UInt8
    s_int8: _winrt.UInt8
    struct: _winrt.UInt8
    uint12: _winrt.UInt8
    uint128: _winrt.UInt8
    uint16: _winrt.UInt8
    uint24: _winrt.UInt8
    uint32: _winrt.UInt8
    uint48: _winrt.UInt8
    uint64: _winrt.UInt8
    uint8: _winrt.UInt8
    utf16: _winrt.UInt8
    utf8: _winrt.UInt8
    @staticmethod
    def _from(obj: _winrt.Object) -> GattPresentationFormatTypes: ...

class GattProtocolError(_winrt.Object):
    attribute_not_found: _winrt.UInt8
    attribute_not_long: _winrt.UInt8
    insufficient_authentication: _winrt.UInt8
    insufficient_authorization: _winrt.UInt8
    insufficient_encryption: _winrt.UInt8
    insufficient_encryption_key_size: _winrt.UInt8
    insufficient_resources: _winrt.UInt8
    invalid_attribute_value_length: _winrt.UInt8
    invalid_handle: _winrt.UInt8
    invalid_offset: _winrt.UInt8
    invalid_pdu: _winrt.UInt8
    prepare_queue_full: _winrt.UInt8
    read_not_permitted: _winrt.UInt8
    request_not_supported: _winrt.UInt8
    unlikely_error: _winrt.UInt8
    unsupported_group_type: _winrt.UInt8
    write_not_permitted: _winrt.UInt8
    @staticmethod
    def _from(obj: _winrt.Object) -> GattProtocolError: ...

class GattReadClientCharacteristicConfigurationDescriptorResult(_winrt.Object):
    client_characteristic_configuration_descriptor: GattClientCharacteristicConfigurationDescriptorValue
    status: GattCommunicationStatus
    protocol_error: typing.Optional[_winrt.UInt8]
    @staticmethod
    def _from(obj: _winrt.Object) -> GattReadClientCharacteristicConfigurationDescriptorResult: ...

class GattReadRequest(_winrt.Object):
    length: _winrt.UInt32
    offset: _winrt.UInt32
    state: GattRequestState
    @staticmethod
    def _from(obj: _winrt.Object) -> GattReadRequest: ...
    @typing.overload
    def respond_with_protocol_error(self, protocol_error: _winrt.UInt8) -> None: ...
    @typing.overload
    def respond_with_value(self, value: winsdk.windows.storage.streams.IBuffer) -> None: ...
    @typing.overload
    def add_state_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[GattReadRequest, GattRequestStateChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_state_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class GattReadRequestedEventArgs(_winrt.Object):
    session: GattSession
    @staticmethod
    def _from(obj: _winrt.Object) -> GattReadRequestedEventArgs: ...
    @typing.overload
    def get_deferral(self) -> winsdk.windows.foundation.Deferral: ...
    @typing.overload
    def get_request_async(self) -> winsdk.windows.foundation.IAsyncOperation[GattReadRequest]: ...

class GattReadResult(_winrt.Object):
    status: GattCommunicationStatus
    value: winsdk.windows.storage.streams.IBuffer
    protocol_error: typing.Optional[_winrt.UInt8]
    @staticmethod
    def _from(obj: _winrt.Object) -> GattReadResult: ...

class GattReliableWriteTransaction(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> GattReliableWriteTransaction: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def commit_async(self) -> winsdk.windows.foundation.IAsyncOperation[GattCommunicationStatus]: ...
    @typing.overload
    def commit_with_result_async(self) -> winsdk.windows.foundation.IAsyncOperation[GattWriteResult]: ...
    @typing.overload
    def write_value(self, characteristic: GattCharacteristic, value: winsdk.windows.storage.streams.IBuffer) -> None: ...

class GattRequestStateChangedEventArgs(_winrt.Object):
    error: winsdk.windows.devices.bluetooth.BluetoothError
    state: GattRequestState
    @staticmethod
    def _from(obj: _winrt.Object) -> GattRequestStateChangedEventArgs: ...

class GattServiceProvider(_winrt.Object):
    advertisement_status: GattServiceProviderAdvertisementStatus
    service: GattLocalService
    @staticmethod
    def _from(obj: _winrt.Object) -> GattServiceProvider: ...
    @typing.overload
    @staticmethod
    def create_async(service_uuid: uuid.UUID) -> winsdk.windows.foundation.IAsyncOperation[GattServiceProviderResult]: ...
    @typing.overload
    def start_advertising(self) -> None: ...
    @typing.overload
    def start_advertising(self, parameters: GattServiceProviderAdvertisingParameters) -> None: ...
    @typing.overload
    def stop_advertising(self) -> None: ...
    @typing.overload
    def add_advertisement_status_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[GattServiceProvider, GattServiceProviderAdvertisementStatusChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_advertisement_status_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class GattServiceProviderAdvertisementStatusChangedEventArgs(_winrt.Object):
    error: winsdk.windows.devices.bluetooth.BluetoothError
    status: GattServiceProviderAdvertisementStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> GattServiceProviderAdvertisementStatusChangedEventArgs: ...

class GattServiceProviderAdvertisingParameters(_winrt.Object):
    is_discoverable: _winrt.Boolean
    is_connectable: _winrt.Boolean
    service_data: winsdk.windows.storage.streams.IBuffer
    @staticmethod
    def _from(obj: _winrt.Object) -> GattServiceProviderAdvertisingParameters: ...
    @typing.overload
    def __init__(self) -> None: ...

class GattServiceProviderResult(_winrt.Object):
    error: winsdk.windows.devices.bluetooth.BluetoothError
    service_provider: GattServiceProvider
    @staticmethod
    def _from(obj: _winrt.Object) -> GattServiceProviderResult: ...

class GattServiceUuids(_winrt.Object):
    battery: uuid.UUID
    blood_pressure: uuid.UUID
    cycling_speed_and_cadence: uuid.UUID
    generic_access: uuid.UUID
    generic_attribute: uuid.UUID
    glucose: uuid.UUID
    health_thermometer: uuid.UUID
    heart_rate: uuid.UUID
    running_speed_and_cadence: uuid.UUID
    alert_notification: uuid.UUID
    current_time: uuid.UUID
    cycling_power: uuid.UUID
    device_information: uuid.UUID
    human_interface_device: uuid.UUID
    immediate_alert: uuid.UUID
    link_loss: uuid.UUID
    location_and_navigation: uuid.UUID
    next_dst_change: uuid.UUID
    phone_alert_status: uuid.UUID
    reference_time_update: uuid.UUID
    scan_parameters: uuid.UUID
    tx_power: uuid.UUID
    @staticmethod
    def _from(obj: _winrt.Object) -> GattServiceUuids: ...

class GattSession(winsdk.windows.foundation.IClosable, _winrt.Object):
    maintain_connection: _winrt.Boolean
    can_maintain_connection: _winrt.Boolean
    device_id: winsdk.windows.devices.bluetooth.BluetoothDeviceId
    max_pdu_size: _winrt.UInt16
    session_status: GattSessionStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> GattSession: ...
    @typing.overload
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def from_device_id_async(device_id: winsdk.windows.devices.bluetooth.BluetoothDeviceId) -> winsdk.windows.foundation.IAsyncOperation[GattSession]: ...
    @typing.overload
    def add_max_pdu_size_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[GattSession, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_max_pdu_size_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_session_status_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[GattSession, GattSessionStatusChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_session_status_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class GattSessionStatusChangedEventArgs(_winrt.Object):
    error: winsdk.windows.devices.bluetooth.BluetoothError
    status: GattSessionStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> GattSessionStatusChangedEventArgs: ...

class GattSubscribedClient(_winrt.Object):
    max_notification_size: _winrt.UInt16
    session: GattSession
    @staticmethod
    def _from(obj: _winrt.Object) -> GattSubscribedClient: ...
    @typing.overload
    def add_max_notification_size_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[GattSubscribedClient, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_max_notification_size_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class GattValueChangedEventArgs(_winrt.Object):
    characteristic_value: winsdk.windows.storage.streams.IBuffer
    timestamp: winsdk.windows.foundation.DateTime
    @staticmethod
    def _from(obj: _winrt.Object) -> GattValueChangedEventArgs: ...

class GattWriteRequest(_winrt.Object):
    offset: _winrt.UInt32
    option: GattWriteOption
    state: GattRequestState
    value: winsdk.windows.storage.streams.IBuffer
    @staticmethod
    def _from(obj: _winrt.Object) -> GattWriteRequest: ...
    @typing.overload
    def respond(self) -> None: ...
    @typing.overload
    def respond_with_protocol_error(self, protocol_error: _winrt.UInt8) -> None: ...
    @typing.overload
    def add_state_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[GattWriteRequest, GattRequestStateChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_state_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class GattWriteRequestedEventArgs(_winrt.Object):
    session: GattSession
    @staticmethod
    def _from(obj: _winrt.Object) -> GattWriteRequestedEventArgs: ...
    @typing.overload
    def get_deferral(self) -> winsdk.windows.foundation.Deferral: ...
    @typing.overload
    def get_request_async(self) -> winsdk.windows.foundation.IAsyncOperation[GattWriteRequest]: ...

class GattWriteResult(_winrt.Object):
    protocol_error: typing.Optional[_winrt.UInt8]
    status: GattCommunicationStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> GattWriteResult: ...

