# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

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

class CellularClass(enum.IntEnum):
    NONE = 0
    GSM = 1
    CDMA = 2

class SmsBroadcastType(enum.IntEnum):
    OTHER = 0
    CMAS_PRESIDENTIAL = 1
    CMAS_EXTREME = 2
    CMAS_SEVERE = 3
    CMAS_AMBER = 4
    CMAS_TEST = 5
    E_U_ALERT1 = 6
    E_U_ALERT2 = 7
    E_U_ALERT3 = 8
    E_U_ALERT_AMBER = 9
    E_U_ALERT_INFO = 10
    ETWS_EARTHQUAKE = 11
    ETWS_TSUNAMI = 12
    ETWS_TSUNAMI_AND_EARTHQUAKE = 13
    LAT_ALERT_LOCAL = 14

class SmsDataFormat(enum.IntEnum):
    UNKNOWN = 0
    CDMA_SUBMIT = 1
    GSM_SUBMIT = 2
    CDMA_DELIVER = 3
    GSM_DELIVER = 4

class SmsDeviceStatus(enum.IntEnum):
    OFF = 0
    READY = 1
    SIM_NOT_INSERTED = 2
    BAD_SIM = 3
    DEVICE_FAILURE = 4
    SUBSCRIPTION_NOT_ACTIVATED = 5
    DEVICE_LOCKED = 6
    DEVICE_BLOCKED = 7

class SmsEncoding(enum.IntEnum):
    UNKNOWN = 0
    OPTIMAL = 1
    SEVEN_BIT_ASCII = 2
    UNICODE = 3
    GSM_SEVEN_BIT = 4
    EIGHT_BIT = 5
    LATIN = 6
    KOREAN = 7
    I_A5 = 8
    SHIFT_JIS = 9
    LATIN_HEBREW = 10

class SmsFilterActionType(enum.IntEnum):
    ACCEPT_IMMEDIATELY = 0
    DROP = 1
    PEEK = 2
    ACCEPT = 3

class SmsGeographicalScope(enum.IntEnum):
    NONE = 0
    CELL_WITH_IMMEDIATE_DISPLAY = 1
    LOCATION_AREA = 2
    PLMN = 3
    CELL = 4

class SmsMessageClass(enum.IntEnum):
    NONE = 0
    CLASS0 = 1
    CLASS1 = 2
    CLASS2 = 3
    CLASS3 = 4

class SmsMessageType(enum.IntEnum):
    BINARY = 0
    TEXT = 1
    WAP = 2
    APP = 3
    BROADCAST = 4
    VOICEMAIL = 5
    STATUS = 6

class SmsModemErrorCode(enum.IntEnum):
    OTHER = 0
    MESSAGING_NETWORK_ERROR = 1
    SMS_OPERATION_NOT_SUPPORTED_BY_DEVICE = 2
    SMS_SERVICE_NOT_SUPPORTED_BY_NETWORK = 3
    DEVICE_FAILURE = 4
    MESSAGE_NOT_ENCODED_PROPERLY = 5
    MESSAGE_TOO_LARGE = 6
    DEVICE_NOT_READY = 7
    NETWORK_NOT_READY = 8
    INVALID_SMSC_ADDRESS = 9
    NETWORK_FAILURE = 10
    FIXED_DIALING_NUMBER_RESTRICTED = 11

class SmsEncodedLength:
    segment_count: _winrt.UInt32
    character_count_last_segment: _winrt.UInt32
    characters_per_segment: _winrt.UInt32
    byte_count_last_segment: _winrt.UInt32
    bytes_per_segment: _winrt.UInt32
    def __init__(self, segment_count: _winrt.UInt32, character_count_last_segment: _winrt.UInt32, characters_per_segment: _winrt.UInt32, byte_count_last_segment: _winrt.UInt32, bytes_per_segment: _winrt.UInt32) -> None: ...

class SmsAppMessage(ISmsMessageBase, _winrt.Object):
    ...
    protocol_id: _winrt.Int32
    port_number: _winrt.Int32
    is_delivery_notification_enabled: _winrt.Boolean
    retry_attempt_count: _winrt.Int32
    encoding: SmsEncoding
    body: str
    callback_number: str
    binary_body: winsdk.windows.storage.streams.IBuffer
    to: str
    teleservice_id: _winrt.Int32
    from: str
    timestamp: winsdk.windows.foundation.DateTime
    cellular_class: CellularClass
    device_id: str
    message_class: SmsMessageClass
    message_type: SmsMessageType
    sim_icc_id: str
    def __init__(self, ) -> None:
        ...

class SmsBroadcastMessage(ISmsMessageBase, _winrt.Object):
    ...
    body: str
    broadcast_type: SmsBroadcastType
    channel: _winrt.Int32
    geographical_scope: SmsGeographicalScope
    is_emergency_alert: _winrt.Boolean
    is_user_popup_requested: _winrt.Boolean
    message_code: _winrt.Int32
    timestamp: winsdk.windows.foundation.DateTime
    to: str
    update_number: _winrt.Int32
    cellular_class: CellularClass
    device_id: str
    message_class: SmsMessageClass
    message_type: SmsMessageType
    sim_icc_id: str

class SmsDevice2(_winrt.Object):
    ...
    smsc_address: str
    account_phone_number: str
    cellular_class: CellularClass
    device_id: str
    device_status: SmsDeviceStatus
    parent_device_id: str
    def calculate_length(message: ISmsMessageBase) -> SmsEncodedLength:
        ...
    def from_id(device_id: str) -> SmsDevice2:
        ...
    def from_parent_id(parent_device_id: str) -> SmsDevice2:
        ...
    def get_default() -> SmsDevice2:
        ...
    def get_device_selector() -> str:
        ...
    def send_message_and_get_result_async(message: ISmsMessageBase) -> winsdk.windows.foundation.IAsyncOperation[SmsSendMessageResult]:
        ...
    def add_device_status_changed(event_handler: winsdk.windows.foundation.TypedEventHandler[SmsDevice2, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_device_status_changed(event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class SmsFilterRule(_winrt.Object):
    ...
    cellular_class: CellularClass
    broadcast_channels: winsdk.windows.foundation.collections.IVector[_winrt.Int32]
    broadcast_types: winsdk.windows.foundation.collections.IVector[SmsBroadcastType]
    device_ids: winsdk.windows.foundation.collections.IVector[str]
    imsi_prefixes: winsdk.windows.foundation.collections.IVector[str]
    message_type: SmsMessageType
    port_numbers: winsdk.windows.foundation.collections.IVector[_winrt.Int32]
    protocol_ids: winsdk.windows.foundation.collections.IVector[_winrt.Int32]
    sender_numbers: winsdk.windows.foundation.collections.IVector[str]
    teleservice_ids: winsdk.windows.foundation.collections.IVector[_winrt.Int32]
    text_message_prefixes: winsdk.windows.foundation.collections.IVector[str]
    wap_application_ids: winsdk.windows.foundation.collections.IVector[str]
    wap_content_types: winsdk.windows.foundation.collections.IVector[str]
    def __init__(self, message_type: SmsMessageType) -> None:
        ...

class SmsFilterRules(_winrt.Object):
    ...
    action_type: SmsFilterActionType
    rules: winsdk.windows.foundation.collections.IVector[SmsFilterRule]
    def __init__(self, action_type: SmsFilterActionType) -> None:
        ...

class SmsMessageReceivedTriggerDetails(_winrt.Object):
    ...
    app_message: SmsAppMessage
    broadcast_message: SmsBroadcastMessage
    message_type: SmsMessageType
    status_message: SmsStatusMessage
    text_message: SmsTextMessage2
    voicemail_message: SmsVoicemailMessage
    wap_message: SmsWapMessage
    def accept() -> None:
        ...
    def drop() -> None:
        ...

class SmsMessageRegistration(_winrt.Object):
    ...
    id: str
    all_registrations: winsdk.windows.foundation.collections.IVectorView[SmsMessageRegistration]
    def register(id: str, filter_rules: SmsFilterRules) -> SmsMessageRegistration:
        ...
    def unregister() -> None:
        ...
    def add_message_received(event_handler: winsdk.windows.foundation.TypedEventHandler[SmsMessageRegistration, SmsMessageReceivedTriggerDetails]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_message_received(event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class SmsSendMessageResult(_winrt.Object):
    ...
    cellular_class: CellularClass
    is_error_transient: _winrt.Boolean
    is_successful: _winrt.Boolean
    message_reference_numbers: winsdk.windows.foundation.collections.IVectorView[_winrt.Int32]
    modem_error_code: SmsModemErrorCode
    network_cause_code: _winrt.Int32
    transport_failure_cause: _winrt.Int32

class SmsStatusMessage(ISmsMessageBase, _winrt.Object):
    ...
    cellular_class: CellularClass
    device_id: str
    message_class: SmsMessageClass
    message_type: SmsMessageType
    sim_icc_id: str
    status: _winrt.Int32
    body: str
    discharge_time: winsdk.windows.foundation.DateTime
    from: str
    message_reference_number: _winrt.Int32
    service_center_timestamp: winsdk.windows.foundation.DateTime
    to: str

class SmsTextMessage2(ISmsMessageBase, _winrt.Object):
    ...
    message_type: SmsMessageType
    device_id: str
    cellular_class: CellularClass
    message_class: SmsMessageClass
    sim_icc_id: str
    retry_attempt_count: _winrt.Int32
    to: str
    is_delivery_notification_enabled: _winrt.Boolean
    encoding: SmsEncoding
    callback_number: str
    body: str
    protocol_id: _winrt.Int32
    from: str
    timestamp: winsdk.windows.foundation.DateTime
    teleservice_id: _winrt.Int32
    def __init__(self, ) -> None:
        ...

class SmsVoicemailMessage(ISmsMessageBase, _winrt.Object):
    ...
    cellular_class: CellularClass
    device_id: str
    message_class: SmsMessageClass
    message_type: SmsMessageType
    sim_icc_id: str
    body: str
    message_count: typing.Optional[_winrt.Int32]
    timestamp: winsdk.windows.foundation.DateTime
    to: str

class SmsWapMessage(ISmsMessageBase, _winrt.Object):
    ...
    cellular_class: CellularClass
    device_id: str
    message_class: SmsMessageClass
    message_type: SmsMessageType
    sim_icc_id: str
    timestamp: winsdk.windows.foundation.DateTime
    application_id: str
    binary_body: winsdk.windows.storage.streams.IBuffer
    content_type: str
    from: str
    headers: winsdk.windows.foundation.collections.IMap[str, str]
    to: str

class ISmsMessageBase(_winrt.Object):
    ...
    cellular_class: CellularClass
    device_id: str
    message_class: SmsMessageClass
    message_type: SmsMessageType
    sim_icc_id: str

