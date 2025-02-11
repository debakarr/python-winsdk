# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.foundation
import winsdk.windows.foundation.collections
import winsdk.windows.storage.streams

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

class SmsMessageFilter(enum.IntEnum):
    ALL = 0
    UNREAD = 1
    READ = 2
    SENT = 3
    DRAFT = 4

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

Self = typing.TypeVar('Self')

class SmsEncodedLength:
    segment_count: _winrt.UInt32
    character_count_last_segment: _winrt.UInt32
    characters_per_segment: _winrt.UInt32
    byte_count_last_segment: _winrt.UInt32
    bytes_per_segment: _winrt.UInt32
    def __init__(self, segment_count: _winrt.UInt32, character_count_last_segment: _winrt.UInt32, characters_per_segment: _winrt.UInt32, byte_count_last_segment: _winrt.UInt32, bytes_per_segment: _winrt.UInt32) -> None: ...

class DeleteSmsMessageOperation(_winrt.Object):
    error_code: winsdk.windows.foundation.HResult
    id: _winrt.UInt32
    status: winsdk.windows.foundation.AsyncStatus
    completed: typing.Optional[winsdk.windows.foundation.AsyncActionCompletedHandler]
    @staticmethod
    def _from(obj: _winrt.Object) -> DeleteSmsMessageOperation: ...
    def cancel(self) -> None: ...
    def close(self) -> None: ...
    def get_results(self) -> None: ...

class DeleteSmsMessagesOperation(_winrt.Object):
    error_code: winsdk.windows.foundation.HResult
    id: _winrt.UInt32
    status: winsdk.windows.foundation.AsyncStatus
    completed: typing.Optional[winsdk.windows.foundation.AsyncActionCompletedHandler]
    @staticmethod
    def _from(obj: _winrt.Object) -> DeleteSmsMessagesOperation: ...
    def cancel(self) -> None: ...
    def close(self) -> None: ...
    def get_results(self) -> None: ...

class GetSmsDeviceOperation(_winrt.Object):
    error_code: winsdk.windows.foundation.HResult
    id: _winrt.UInt32
    status: winsdk.windows.foundation.AsyncStatus
    completed: typing.Optional[winsdk.windows.foundation.AsyncOperationCompletedHandler[SmsDevice]]
    @staticmethod
    def _from(obj: _winrt.Object) -> GetSmsDeviceOperation: ...
    def cancel(self) -> None: ...
    def close(self) -> None: ...
    def get_results(self) -> typing.Optional[SmsDevice]: ...

class GetSmsMessageOperation(_winrt.Object):
    error_code: winsdk.windows.foundation.HResult
    id: _winrt.UInt32
    status: winsdk.windows.foundation.AsyncStatus
    completed: typing.Optional[winsdk.windows.foundation.AsyncOperationCompletedHandler[ISmsMessage]]
    @staticmethod
    def _from(obj: _winrt.Object) -> GetSmsMessageOperation: ...
    def cancel(self) -> None: ...
    def close(self) -> None: ...
    def get_results(self) -> typing.Optional[ISmsMessage]: ...

class GetSmsMessagesOperation(_winrt.Object):
    error_code: winsdk.windows.foundation.HResult
    id: _winrt.UInt32
    status: winsdk.windows.foundation.AsyncStatus
    progress: typing.Optional[winsdk.windows.foundation.AsyncOperationProgressHandler[winsdk.windows.foundation.collections.IVectorView[ISmsMessage], _winrt.Int32]]
    completed: typing.Optional[winsdk.windows.foundation.AsyncOperationWithProgressCompletedHandler[winsdk.windows.foundation.collections.IVectorView[ISmsMessage], _winrt.Int32]]
    @staticmethod
    def _from(obj: _winrt.Object) -> GetSmsMessagesOperation: ...
    def cancel(self) -> None: ...
    def close(self) -> None: ...
    def get_results(self) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[ISmsMessage]]: ...

class SendSmsMessageOperation(_winrt.Object):
    error_code: winsdk.windows.foundation.HResult
    id: _winrt.UInt32
    status: winsdk.windows.foundation.AsyncStatus
    completed: typing.Optional[winsdk.windows.foundation.AsyncActionCompletedHandler]
    @staticmethod
    def _from(obj: _winrt.Object) -> SendSmsMessageOperation: ...
    def cancel(self) -> None: ...
    def close(self) -> None: ...
    def get_results(self) -> None: ...

class SmsAppMessage(_winrt.Object):
    protocol_id: _winrt.Int32
    port_number: _winrt.Int32
    is_delivery_notification_enabled: _winrt.Boolean
    retry_attempt_count: _winrt.Int32
    encoding: SmsEncoding
    body: str
    callback_number: str
    binary_body: typing.Optional[winsdk.windows.storage.streams.IBuffer]
    to: str
    teleservice_id: _winrt.Int32
    from_: str
    timestamp: winsdk.windows.foundation.DateTime
    cellular_class: CellularClass
    device_id: str
    message_class: SmsMessageClass
    message_type: SmsMessageType
    sim_icc_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> SmsAppMessage: ...
    def __init__(self) -> None: ...

class SmsBinaryMessage(_winrt.Object):
    format: SmsDataFormat
    id: _winrt.UInt32
    message_class: SmsMessageClass
    @staticmethod
    def _from(obj: _winrt.Object) -> SmsBinaryMessage: ...
    def __init__(self) -> None: ...
    def get_data(self) -> _winrt.UInt8: ...
    def set_data(self, value: typing.Sequence[_winrt.UInt8]) -> None: ...

class SmsBroadcastMessage(_winrt.Object):
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
    @staticmethod
    def _from(obj: _winrt.Object) -> SmsBroadcastMessage: ...

class SmsDevice(_winrt.Object):
    account_phone_number: str
    cellular_class: CellularClass
    device_status: SmsDeviceStatus
    message_store: typing.Optional[SmsDeviceMessageStore]
    @staticmethod
    def _from(obj: _winrt.Object) -> SmsDevice: ...
    def calculate_length(self, message: typing.Optional[SmsTextMessage]) -> SmsEncodedLength: ...
    @staticmethod
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[SmsDevice]: ...
    @staticmethod
    def from_network_account_id_async(network_account_id: str) -> winsdk.windows.foundation.IAsyncOperation[SmsDevice]: ...
    @staticmethod
    def get_default_async() -> winsdk.windows.foundation.IAsyncOperation[SmsDevice]: ...
    @staticmethod
    def get_device_selector() -> str: ...
    def send_message_async(self, message: typing.Optional[ISmsMessage]) -> typing.Optional[SendSmsMessageOperation]: ...
    def add_sms_device_status_changed(self, event_handler: typing.Optional[SmsDeviceStatusChangedEventHandler]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_sms_device_status_changed(self, event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_sms_message_received(self, event_handler: typing.Optional[SmsMessageReceivedEventHandler]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_sms_message_received(self, event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class SmsDevice2(_winrt.Object):
    smsc_address: str
    account_phone_number: str
    cellular_class: CellularClass
    device_id: str
    device_status: SmsDeviceStatus
    parent_device_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> SmsDevice2: ...
    def calculate_length(self, message: typing.Optional[ISmsMessageBase]) -> SmsEncodedLength: ...
    @staticmethod
    def from_id(device_id: str) -> typing.Optional[SmsDevice2]: ...
    @staticmethod
    def from_parent_id(parent_device_id: str) -> typing.Optional[SmsDevice2]: ...
    @staticmethod
    def get_default() -> typing.Optional[SmsDevice2]: ...
    @staticmethod
    def get_device_selector() -> str: ...
    def send_message_and_get_result_async(self, message: typing.Optional[ISmsMessageBase]) -> winsdk.windows.foundation.IAsyncOperation[SmsSendMessageResult]: ...
    def add_device_status_changed(self, event_handler: winsdk.windows.foundation.TypedEventHandler[SmsDevice2, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_device_status_changed(self, event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class SmsDeviceMessageStore(_winrt.Object):
    max_messages: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> SmsDeviceMessageStore: ...
    def delete_message_async(self, message_id: _winrt.UInt32) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def delete_messages_async(self, message_filter: SmsMessageFilter) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def get_message_async(self, message_id: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[ISmsMessage]: ...
    def get_messages_async(self, message_filter: SmsMessageFilter) -> winsdk.windows.foundation.IAsyncOperationWithProgress[winsdk.windows.foundation.collections.IVectorView[ISmsMessage], _winrt.Int32]: ...

class SmsFilterRule(_winrt.Object):
    cellular_class: CellularClass
    broadcast_channels: typing.Optional[winsdk.windows.foundation.collections.IVector[_winrt.Int32]]
    broadcast_types: typing.Optional[winsdk.windows.foundation.collections.IVector[SmsBroadcastType]]
    device_ids: typing.Optional[winsdk.windows.foundation.collections.IVector[str]]
    imsi_prefixes: typing.Optional[winsdk.windows.foundation.collections.IVector[str]]
    message_type: SmsMessageType
    port_numbers: typing.Optional[winsdk.windows.foundation.collections.IVector[_winrt.Int32]]
    protocol_ids: typing.Optional[winsdk.windows.foundation.collections.IVector[_winrt.Int32]]
    sender_numbers: typing.Optional[winsdk.windows.foundation.collections.IVector[str]]
    teleservice_ids: typing.Optional[winsdk.windows.foundation.collections.IVector[_winrt.Int32]]
    text_message_prefixes: typing.Optional[winsdk.windows.foundation.collections.IVector[str]]
    wap_application_ids: typing.Optional[winsdk.windows.foundation.collections.IVector[str]]
    wap_content_types: typing.Optional[winsdk.windows.foundation.collections.IVector[str]]
    @staticmethod
    def _from(obj: _winrt.Object) -> SmsFilterRule: ...
    def __init__(self, message_type: SmsMessageType) -> None: ...

class SmsFilterRules(_winrt.Object):
    action_type: SmsFilterActionType
    rules: typing.Optional[winsdk.windows.foundation.collections.IVector[SmsFilterRule]]
    @staticmethod
    def _from(obj: _winrt.Object) -> SmsFilterRules: ...
    def __init__(self, action_type: SmsFilterActionType) -> None: ...

class SmsMessageReceivedEventArgs(_winrt.Object):
    binary_message: typing.Optional[SmsBinaryMessage]
    text_message: typing.Optional[SmsTextMessage]
    @staticmethod
    def _from(obj: _winrt.Object) -> SmsMessageReceivedEventArgs: ...

class SmsMessageReceivedTriggerDetails(_winrt.Object):
    app_message: typing.Optional[SmsAppMessage]
    broadcast_message: typing.Optional[SmsBroadcastMessage]
    message_type: SmsMessageType
    status_message: typing.Optional[SmsStatusMessage]
    text_message: typing.Optional[SmsTextMessage2]
    voicemail_message: typing.Optional[SmsVoicemailMessage]
    wap_message: typing.Optional[SmsWapMessage]
    @staticmethod
    def _from(obj: _winrt.Object) -> SmsMessageReceivedTriggerDetails: ...
    def accept(self) -> None: ...
    def drop(self) -> None: ...

class SmsMessageRegistration(_winrt.Object):
    id: str
    all_registrations: typing.Optional[winsdk.windows.foundation.collections.IVectorView[SmsMessageRegistration]]
    @staticmethod
    def _from(obj: _winrt.Object) -> SmsMessageRegistration: ...
    @staticmethod
    def register(id: str, filter_rules: typing.Optional[SmsFilterRules]) -> typing.Optional[SmsMessageRegistration]: ...
    def unregister(self) -> None: ...
    def add_message_received(self, event_handler: winsdk.windows.foundation.TypedEventHandler[SmsMessageRegistration, SmsMessageReceivedTriggerDetails]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_message_received(self, event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class SmsReceivedEventDetails(_winrt.Object):
    device_id: str
    message_index: _winrt.UInt32
    binary_message: typing.Optional[SmsBinaryMessage]
    message_class: SmsMessageClass
    @staticmethod
    def _from(obj: _winrt.Object) -> SmsReceivedEventDetails: ...

class SmsSendMessageResult(_winrt.Object):
    cellular_class: CellularClass
    is_error_transient: _winrt.Boolean
    is_successful: _winrt.Boolean
    message_reference_numbers: typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int32]]
    modem_error_code: SmsModemErrorCode
    network_cause_code: _winrt.Int32
    transport_failure_cause: _winrt.Int32
    @staticmethod
    def _from(obj: _winrt.Object) -> SmsSendMessageResult: ...

class SmsStatusMessage(_winrt.Object):
    cellular_class: CellularClass
    device_id: str
    message_class: SmsMessageClass
    message_type: SmsMessageType
    sim_icc_id: str
    status: _winrt.Int32
    body: str
    discharge_time: winsdk.windows.foundation.DateTime
    from_: str
    message_reference_number: _winrt.Int32
    service_center_timestamp: winsdk.windows.foundation.DateTime
    to: str
    @staticmethod
    def _from(obj: _winrt.Object) -> SmsStatusMessage: ...

class SmsTextMessage(_winrt.Object):
    id: _winrt.UInt32
    message_class: SmsMessageClass
    to: str
    from_: str
    encoding: SmsEncoding
    body: str
    part_count: _winrt.UInt32
    part_number: _winrt.UInt32
    part_reference_id: _winrt.UInt32
    timestamp: winsdk.windows.foundation.DateTime
    @staticmethod
    def _from(obj: _winrt.Object) -> SmsTextMessage: ...
    def __init__(self) -> None: ...
    @staticmethod
    def from_binary_data(format: SmsDataFormat, value: typing.Sequence[_winrt.UInt8]) -> typing.Optional[SmsTextMessage]: ...
    @staticmethod
    def from_binary_message(binary_message: typing.Optional[SmsBinaryMessage]) -> typing.Optional[SmsTextMessage]: ...
    def to_binary_messages(self, format: SmsDataFormat) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[ISmsBinaryMessage]]: ...

class SmsTextMessage2(_winrt.Object):
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
    from_: str
    timestamp: winsdk.windows.foundation.DateTime
    teleservice_id: _winrt.Int32
    @staticmethod
    def _from(obj: _winrt.Object) -> SmsTextMessage2: ...
    def __init__(self) -> None: ...

class SmsVoicemailMessage(_winrt.Object):
    cellular_class: CellularClass
    device_id: str
    message_class: SmsMessageClass
    message_type: SmsMessageType
    sim_icc_id: str
    body: str
    message_count: typing.Optional[typing.Optional[_winrt.Int32]]
    timestamp: winsdk.windows.foundation.DateTime
    to: str
    @staticmethod
    def _from(obj: _winrt.Object) -> SmsVoicemailMessage: ...

class SmsWapMessage(_winrt.Object):
    cellular_class: CellularClass
    device_id: str
    message_class: SmsMessageClass
    message_type: SmsMessageType
    sim_icc_id: str
    timestamp: winsdk.windows.foundation.DateTime
    application_id: str
    binary_body: typing.Optional[winsdk.windows.storage.streams.IBuffer]
    content_type: str
    from_: str
    headers: typing.Optional[winsdk.windows.foundation.collections.IMap[str, str]]
    to: str
    @staticmethod
    def _from(obj: _winrt.Object) -> SmsWapMessage: ...

class ISmsBinaryMessage(_winrt.Object):
    format: SmsDataFormat
    id: _winrt.UInt32
    message_class: SmsMessageClass
    @staticmethod
    def _from(obj: _winrt.Object) -> ISmsBinaryMessage: ...
    def get_data(self) -> _winrt.UInt8: ...
    def set_data(self, value: typing.Sequence[_winrt.UInt8]) -> None: ...

class ISmsDevice(_winrt.Object):
    account_phone_number: str
    cellular_class: CellularClass
    device_status: SmsDeviceStatus
    message_store: typing.Optional[SmsDeviceMessageStore]
    @staticmethod
    def _from(obj: _winrt.Object) -> ISmsDevice: ...
    def calculate_length(self, message: typing.Optional[SmsTextMessage]) -> SmsEncodedLength: ...
    def send_message_async(self, message: typing.Optional[ISmsMessage]) -> typing.Optional[SendSmsMessageOperation]: ...
    def add_sms_device_status_changed(self, event_handler: typing.Optional[SmsDeviceStatusChangedEventHandler]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_sms_device_status_changed(self, event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_sms_message_received(self, event_handler: typing.Optional[SmsMessageReceivedEventHandler]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_sms_message_received(self, event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class ISmsMessage(_winrt.Object):
    id: _winrt.UInt32
    message_class: SmsMessageClass
    @staticmethod
    def _from(obj: _winrt.Object) -> ISmsMessage: ...

class ISmsMessageBase(_winrt.Object):
    cellular_class: CellularClass
    device_id: str
    message_class: SmsMessageClass
    message_type: SmsMessageType
    sim_icc_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> ISmsMessageBase: ...

class ISmsTextMessage(_winrt.Object):
    body: str
    encoding: SmsEncoding
    from_: str
    part_count: _winrt.UInt32
    part_number: _winrt.UInt32
    part_reference_id: _winrt.UInt32
    timestamp: winsdk.windows.foundation.DateTime
    to: str
    id: _winrt.UInt32
    message_class: SmsMessageClass
    @staticmethod
    def _from(obj: _winrt.Object) -> ISmsTextMessage: ...
    def to_binary_messages(self, format: SmsDataFormat) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[ISmsBinaryMessage]]: ...

SmsDeviceStatusChangedEventHandler = typing.Callable[[typing.Optional[SmsDevice]], None]

SmsMessageReceivedEventHandler = typing.Callable[[typing.Optional[SmsDevice], typing.Optional[SmsMessageReceivedEventArgs]], None]

