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
    import winsdk.windows.storage
except Exception:
    pass

class CausalityRelation(enum.IntEnum):
    ASSIGN_DELEGATE = 0
    JOIN = 1
    CHOICE = 2
    CANCEL = 3
    ERROR = 4

class CausalitySource(enum.IntEnum):
    APPLICATION = 0
    LIBRARY = 1
    SYSTEM = 2

class CausalitySynchronousWork(enum.IntEnum):
    COMPLETION_NOTIFICATION = 0
    PROGRESS_NOTIFICATION = 1
    EXECUTION = 2

class CausalityTraceLevel(enum.IntEnum):
    REQUIRED = 0
    IMPORTANT = 1
    VERBOSE = 2

class ErrorOptions(enum.IntFlag):
    NONE = 0
    SUPPRESS_EXCEPTIONS = 0x1
    FORCE_EXCEPTIONS = 0x2
    USE_SET_ERROR_INFO = 0x4
    SUPPRESS_SET_ERROR_INFO = 0x8

class LoggingFieldFormat(enum.IntEnum):
    DEFAULT = 0
    HIDDEN = 1
    STRING = 2
    BOOLEAN = 3
    HEXADECIMAL = 4
    PROCESS_ID = 5
    THREAD_ID = 6
    PORT = 7
    IPV4_ADDRESS = 8
    IPV6_ADDRESS = 9
    SOCKET_ADDRESS = 10
    XML = 11
    JSON = 12
    WIN32_ERROR = 13
    N_T_STATUS = 14
    H_RESULT = 15
    FILE_TIME = 16
    SIGNED = 17
    UNSIGNED = 18

class LoggingLevel(enum.IntEnum):
    VERBOSE = 0
    INFORMATION = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4

class LoggingOpcode(enum.IntEnum):
    INFO = 0
    START = 1
    STOP = 2
    REPLY = 6
    RESUME = 7
    SUSPEND = 8
    SEND = 9

class AsyncCausalityTracer(_winrt.Object):
    ...
    def trace_operation_completion(trace_level: CausalityTraceLevel, source: CausalitySource, platform_id: uuid.UUID, operation_id: _winrt.UInt64, status: winsdk.windows.foundation.AsyncStatus) -> None:
        ...
    def trace_operation_creation(trace_level: CausalityTraceLevel, source: CausalitySource, platform_id: uuid.UUID, operation_id: _winrt.UInt64, operation_name: str, related_context: _winrt.UInt64) -> None:
        ...
    def trace_operation_relation(trace_level: CausalityTraceLevel, source: CausalitySource, platform_id: uuid.UUID, operation_id: _winrt.UInt64, relation: CausalityRelation) -> None:
        ...
    def trace_synchronous_work_completion(trace_level: CausalityTraceLevel, source: CausalitySource, work: CausalitySynchronousWork) -> None:
        ...
    def trace_synchronous_work_start(trace_level: CausalityTraceLevel, source: CausalitySource, platform_id: uuid.UUID, operation_id: _winrt.UInt64, work: CausalitySynchronousWork) -> None:
        ...
    def add_tracing_status_changed(handler: winsdk.windows.foundation.EventHandler[TracingStatusChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_tracing_status_changed(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class ErrorDetails(_winrt.Object):
    ...
    description: str
    help_uri: winsdk.windows.foundation.Uri
    long_description: str
    def create_from_h_result_async(error_code: _winrt.Int32) -> winsdk.windows.foundation.IAsyncOperation[ErrorDetails]:
        ...

class FileLoggingSession(IFileLoggingSession, winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    name: str
    def __init__(self, name: str) -> None:
        ...
    def add_logging_channel(logging_channel: ILoggingChannel) -> None:
        ...
    def add_logging_channel(logging_channel: ILoggingChannel, max_level: LoggingLevel) -> None:
        ...
    def close() -> None:
        ...
    def close_and_save_to_file_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]:
        ...
    def remove_logging_channel(logging_channel: ILoggingChannel) -> None:
        ...
    def add_log_file_generated(handler: winsdk.windows.foundation.TypedEventHandler[IFileLoggingSession, LogFileGeneratedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_log_file_generated(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class LogFileGeneratedEventArgs(_winrt.Object):
    ...
    file: winsdk.windows.storage.StorageFile

class LoggingActivity(winsdk.windows.foundation.IClosable, ILoggingTarget, _winrt.Object):
    ...
    id: uuid.UUID
    name: str
    channel: LoggingChannel
    def __init__(self, activity_name: str, logging_channel: ILoggingChannel) -> None:
        ...
    def __init__(self, activity_name: str, logging_channel: ILoggingChannel, level: LoggingLevel) -> None:
        ...
    def close() -> None:
        ...
    def is_enabled() -> _winrt.Boolean:
        ...
    def is_enabled(level: LoggingLevel) -> _winrt.Boolean:
        ...
    def is_enabled(level: LoggingLevel, keywords: _winrt.Int64) -> _winrt.Boolean:
        ...
    def log_event(event_name: str) -> None:
        ...
    def log_event(event_name: str, fields: LoggingFields) -> None:
        ...
    def log_event(event_name: str, fields: LoggingFields, level: LoggingLevel) -> None:
        ...
    def log_event(event_name: str, fields: LoggingFields, level: LoggingLevel, options: LoggingOptions) -> None:
        ...
    def start_activity(start_event_name: str) -> LoggingActivity:
        ...
    def start_activity(start_event_name: str, fields: LoggingFields) -> LoggingActivity:
        ...
    def start_activity(start_event_name: str, fields: LoggingFields, level: LoggingLevel) -> LoggingActivity:
        ...
    def start_activity(start_event_name: str, fields: LoggingFields, level: LoggingLevel, options: LoggingOptions) -> LoggingActivity:
        ...
    def stop_activity(stop_event_name: str) -> None:
        ...
    def stop_activity(stop_event_name: str, fields: LoggingFields) -> None:
        ...
    def stop_activity(stop_event_name: str, fields: LoggingFields, options: LoggingOptions) -> None:
        ...

class LoggingChannel(ILoggingChannel, winsdk.windows.foundation.IClosable, ILoggingTarget, _winrt.Object):
    ...
    enabled: _winrt.Boolean
    level: LoggingLevel
    name: str
    id: uuid.UUID
    def __init__(self, name: str, options: LoggingChannelOptions) -> None:
        ...
    def __init__(self, name: str, options: LoggingChannelOptions, id: uuid.UUID) -> None:
        ...
    def __init__(self, name: str) -> None:
        ...
    def close() -> None:
        ...
    def is_enabled() -> _winrt.Boolean:
        ...
    def is_enabled(level: LoggingLevel) -> _winrt.Boolean:
        ...
    def is_enabled(level: LoggingLevel, keywords: _winrt.Int64) -> _winrt.Boolean:
        ...
    def log_event(event_name: str) -> None:
        ...
    def log_event(event_name: str, fields: LoggingFields) -> None:
        ...
    def log_event(event_name: str, fields: LoggingFields, level: LoggingLevel) -> None:
        ...
    def log_event(event_name: str, fields: LoggingFields, level: LoggingLevel, options: LoggingOptions) -> None:
        ...
    def log_message(event_string: str) -> None:
        ...
    def log_message(event_string: str, level: LoggingLevel) -> None:
        ...
    def log_value_pair(value1: str, value2: _winrt.Int32) -> None:
        ...
    def log_value_pair(value1: str, value2: _winrt.Int32, level: LoggingLevel) -> None:
        ...
    def start_activity(start_event_name: str) -> LoggingActivity:
        ...
    def start_activity(start_event_name: str, fields: LoggingFields) -> LoggingActivity:
        ...
    def start_activity(start_event_name: str, fields: LoggingFields, level: LoggingLevel) -> LoggingActivity:
        ...
    def start_activity(start_event_name: str, fields: LoggingFields, level: LoggingLevel, options: LoggingOptions) -> LoggingActivity:
        ...
    def add_logging_enabled(handler: winsdk.windows.foundation.TypedEventHandler[ILoggingChannel, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_logging_enabled(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class LoggingChannelOptions(_winrt.Object):
    ...
    group: uuid.UUID
    def __init__(self, ) -> None:
        ...
    def __init__(self, group: uuid.UUID) -> None:
        ...

class LoggingFields(_winrt.Object):
    ...
    def __init__(self, ) -> None:
        ...
    def add_boolean(name: str, value: _winrt.Boolean) -> None:
        ...
    def add_boolean(name: str, value: _winrt.Boolean, format: LoggingFieldFormat) -> None:
        ...
    def add_boolean(name: str, value: _winrt.Boolean, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_boolean_array(name: str, value: typing.Sequence[_winrt.Boolean]) -> None:
        ...
    def add_boolean_array(name: str, value: typing.Sequence[_winrt.Boolean], format: LoggingFieldFormat) -> None:
        ...
    def add_boolean_array(name: str, value: typing.Sequence[_winrt.Boolean], format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_char16(name: str, value: _winrt.Char16) -> None:
        ...
    def add_char16(name: str, value: _winrt.Char16, format: LoggingFieldFormat) -> None:
        ...
    def add_char16(name: str, value: _winrt.Char16, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_char16_array(name: str, value: typing.Sequence[_winrt.Char16]) -> None:
        ...
    def add_char16_array(name: str, value: typing.Sequence[_winrt.Char16], format: LoggingFieldFormat) -> None:
        ...
    def add_char16_array(name: str, value: typing.Sequence[_winrt.Char16], format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_date_time(name: str, value: winsdk.windows.foundation.DateTime) -> None:
        ...
    def add_date_time(name: str, value: winsdk.windows.foundation.DateTime, format: LoggingFieldFormat) -> None:
        ...
    def add_date_time(name: str, value: winsdk.windows.foundation.DateTime, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_date_time_array(name: str, value: typing.Sequence[winsdk.windows.foundation.DateTime]) -> None:
        ...
    def add_date_time_array(name: str, value: typing.Sequence[winsdk.windows.foundation.DateTime], format: LoggingFieldFormat) -> None:
        ...
    def add_date_time_array(name: str, value: typing.Sequence[winsdk.windows.foundation.DateTime], format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_double(name: str, value: _winrt.Double) -> None:
        ...
    def add_double(name: str, value: _winrt.Double, format: LoggingFieldFormat) -> None:
        ...
    def add_double(name: str, value: _winrt.Double, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_double_array(name: str, value: typing.Sequence[_winrt.Double]) -> None:
        ...
    def add_double_array(name: str, value: typing.Sequence[_winrt.Double], format: LoggingFieldFormat) -> None:
        ...
    def add_double_array(name: str, value: typing.Sequence[_winrt.Double], format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_empty(name: str) -> None:
        ...
    def add_empty(name: str, format: LoggingFieldFormat) -> None:
        ...
    def add_empty(name: str, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_guid(name: str, value: uuid.UUID) -> None:
        ...
    def add_guid(name: str, value: uuid.UUID, format: LoggingFieldFormat) -> None:
        ...
    def add_guid(name: str, value: uuid.UUID, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_guid_array(name: str, value: typing.Sequence[uuid.UUID]) -> None:
        ...
    def add_guid_array(name: str, value: typing.Sequence[uuid.UUID], format: LoggingFieldFormat) -> None:
        ...
    def add_guid_array(name: str, value: typing.Sequence[uuid.UUID], format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_int16(name: str, value: _winrt.Int16) -> None:
        ...
    def add_int16(name: str, value: _winrt.Int16, format: LoggingFieldFormat) -> None:
        ...
    def add_int16(name: str, value: _winrt.Int16, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_int16_array(name: str, value: typing.Sequence[_winrt.Int16]) -> None:
        ...
    def add_int16_array(name: str, value: typing.Sequence[_winrt.Int16], format: LoggingFieldFormat) -> None:
        ...
    def add_int16_array(name: str, value: typing.Sequence[_winrt.Int16], format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_int32(name: str, value: _winrt.Int32) -> None:
        ...
    def add_int32(name: str, value: _winrt.Int32, format: LoggingFieldFormat) -> None:
        ...
    def add_int32(name: str, value: _winrt.Int32, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_int32_array(name: str, value: typing.Sequence[_winrt.Int32]) -> None:
        ...
    def add_int32_array(name: str, value: typing.Sequence[_winrt.Int32], format: LoggingFieldFormat) -> None:
        ...
    def add_int32_array(name: str, value: typing.Sequence[_winrt.Int32], format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_int64(name: str, value: _winrt.Int64) -> None:
        ...
    def add_int64(name: str, value: _winrt.Int64, format: LoggingFieldFormat) -> None:
        ...
    def add_int64(name: str, value: _winrt.Int64, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_int64_array(name: str, value: typing.Sequence[_winrt.Int64]) -> None:
        ...
    def add_int64_array(name: str, value: typing.Sequence[_winrt.Int64], format: LoggingFieldFormat) -> None:
        ...
    def add_int64_array(name: str, value: typing.Sequence[_winrt.Int64], format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_point(name: str, value: winsdk.windows.foundation.Point) -> None:
        ...
    def add_point(name: str, value: winsdk.windows.foundation.Point, format: LoggingFieldFormat) -> None:
        ...
    def add_point(name: str, value: winsdk.windows.foundation.Point, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_point_array(name: str, value: typing.Sequence[winsdk.windows.foundation.Point]) -> None:
        ...
    def add_point_array(name: str, value: typing.Sequence[winsdk.windows.foundation.Point], format: LoggingFieldFormat) -> None:
        ...
    def add_point_array(name: str, value: typing.Sequence[winsdk.windows.foundation.Point], format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_rect(name: str, value: winsdk.windows.foundation.Rect) -> None:
        ...
    def add_rect(name: str, value: winsdk.windows.foundation.Rect, format: LoggingFieldFormat) -> None:
        ...
    def add_rect(name: str, value: winsdk.windows.foundation.Rect, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_rect_array(name: str, value: typing.Sequence[winsdk.windows.foundation.Rect]) -> None:
        ...
    def add_rect_array(name: str, value: typing.Sequence[winsdk.windows.foundation.Rect], format: LoggingFieldFormat) -> None:
        ...
    def add_rect_array(name: str, value: typing.Sequence[winsdk.windows.foundation.Rect], format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_single(name: str, value: _winrt.Single) -> None:
        ...
    def add_single(name: str, value: _winrt.Single, format: LoggingFieldFormat) -> None:
        ...
    def add_single(name: str, value: _winrt.Single, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_single_array(name: str, value: typing.Sequence[_winrt.Single]) -> None:
        ...
    def add_single_array(name: str, value: typing.Sequence[_winrt.Single], format: LoggingFieldFormat) -> None:
        ...
    def add_single_array(name: str, value: typing.Sequence[_winrt.Single], format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_size(name: str, value: winsdk.windows.foundation.Size) -> None:
        ...
    def add_size(name: str, value: winsdk.windows.foundation.Size, format: LoggingFieldFormat) -> None:
        ...
    def add_size(name: str, value: winsdk.windows.foundation.Size, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_size_array(name: str, value: typing.Sequence[winsdk.windows.foundation.Size]) -> None:
        ...
    def add_size_array(name: str, value: typing.Sequence[winsdk.windows.foundation.Size], format: LoggingFieldFormat) -> None:
        ...
    def add_size_array(name: str, value: typing.Sequence[winsdk.windows.foundation.Size], format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_string(name: str, value: str) -> None:
        ...
    def add_string(name: str, value: str, format: LoggingFieldFormat) -> None:
        ...
    def add_string(name: str, value: str, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_string_array(name: str, value: typing.Sequence[str]) -> None:
        ...
    def add_string_array(name: str, value: typing.Sequence[str], format: LoggingFieldFormat) -> None:
        ...
    def add_string_array(name: str, value: typing.Sequence[str], format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_time_span(name: str, value: winsdk.windows.foundation.TimeSpan) -> None:
        ...
    def add_time_span(name: str, value: winsdk.windows.foundation.TimeSpan, format: LoggingFieldFormat) -> None:
        ...
    def add_time_span(name: str, value: winsdk.windows.foundation.TimeSpan, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_time_span_array(name: str, value: typing.Sequence[winsdk.windows.foundation.TimeSpan]) -> None:
        ...
    def add_time_span_array(name: str, value: typing.Sequence[winsdk.windows.foundation.TimeSpan], format: LoggingFieldFormat) -> None:
        ...
    def add_time_span_array(name: str, value: typing.Sequence[winsdk.windows.foundation.TimeSpan], format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_uint16(name: str, value: _winrt.UInt16) -> None:
        ...
    def add_uint16(name: str, value: _winrt.UInt16, format: LoggingFieldFormat) -> None:
        ...
    def add_uint16(name: str, value: _winrt.UInt16, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_uint16_array(name: str, value: typing.Sequence[_winrt.UInt16]) -> None:
        ...
    def add_uint16_array(name: str, value: typing.Sequence[_winrt.UInt16], format: LoggingFieldFormat) -> None:
        ...
    def add_uint16_array(name: str, value: typing.Sequence[_winrt.UInt16], format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_uint32(name: str, value: _winrt.UInt32) -> None:
        ...
    def add_uint32(name: str, value: _winrt.UInt32, format: LoggingFieldFormat) -> None:
        ...
    def add_uint32(name: str, value: _winrt.UInt32, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_uint32_array(name: str, value: typing.Sequence[_winrt.UInt32]) -> None:
        ...
    def add_uint32_array(name: str, value: typing.Sequence[_winrt.UInt32], format: LoggingFieldFormat) -> None:
        ...
    def add_uint32_array(name: str, value: typing.Sequence[_winrt.UInt32], format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_uint64(name: str, value: _winrt.UInt64) -> None:
        ...
    def add_uint64(name: str, value: _winrt.UInt64, format: LoggingFieldFormat) -> None:
        ...
    def add_uint64(name: str, value: _winrt.UInt64, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_uint64_array(name: str, value: typing.Sequence[_winrt.UInt64]) -> None:
        ...
    def add_uint64_array(name: str, value: typing.Sequence[_winrt.UInt64], format: LoggingFieldFormat) -> None:
        ...
    def add_uint64_array(name: str, value: typing.Sequence[_winrt.UInt64], format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_uint8(name: str, value: _winrt.UInt8) -> None:
        ...
    def add_uint8(name: str, value: _winrt.UInt8, format: LoggingFieldFormat) -> None:
        ...
    def add_uint8(name: str, value: _winrt.UInt8, format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def add_uint8_array(name: str, value: typing.Sequence[_winrt.UInt8]) -> None:
        ...
    def add_uint8_array(name: str, value: typing.Sequence[_winrt.UInt8], format: LoggingFieldFormat) -> None:
        ...
    def add_uint8_array(name: str, value: typing.Sequence[_winrt.UInt8], format: LoggingFieldFormat, tags: _winrt.Int32) -> None:
        ...
    def begin_struct(name: str) -> None:
        ...
    def begin_struct(name: str, tags: _winrt.Int32) -> None:
        ...
    def clear() -> None:
        ...
    def end_struct() -> None:
        ...

class LoggingOptions(_winrt.Object):
    ...
    task: _winrt.Int16
    tags: _winrt.Int32
    related_activity_id: uuid.UUID
    opcode: LoggingOpcode
    keywords: _winrt.Int64
    activity_id: uuid.UUID
    def __init__(self, ) -> None:
        ...
    def __init__(self, keywords: _winrt.Int64) -> None:
        ...

class LoggingSession(ILoggingSession, winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    name: str
    def __init__(self, name: str) -> None:
        ...
    def add_logging_channel(logging_channel: ILoggingChannel) -> None:
        ...
    def add_logging_channel(logging_channel: ILoggingChannel, max_level: LoggingLevel) -> None:
        ...
    def close() -> None:
        ...
    def remove_logging_channel(logging_channel: ILoggingChannel) -> None:
        ...
    def save_to_file_async(folder: winsdk.windows.storage.IStorageFolder, file_name: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]:
        ...

class RuntimeBrokerErrorSettings(IErrorReportingSettings, _winrt.Object):
    ...
    def __init__(self, ) -> None:
        ...
    def get_error_options() -> ErrorOptions:
        ...
    def set_error_options(value: ErrorOptions) -> None:
        ...

class TracingStatusChangedEventArgs(_winrt.Object):
    ...
    enabled: _winrt.Boolean
    trace_level: CausalityTraceLevel

class IErrorReportingSettings(_winrt.Object):
    ...
    def get_error_options() -> ErrorOptions:
        ...
    def set_error_options(value: ErrorOptions) -> None:
        ...

class IFileLoggingSession(winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    name: str
    def add_logging_channel(logging_channel: ILoggingChannel) -> None:
        ...
    def add_logging_channel(logging_channel: ILoggingChannel, max_level: LoggingLevel) -> None:
        ...
    def close_and_save_to_file_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]:
        ...
    def remove_logging_channel(logging_channel: ILoggingChannel) -> None:
        ...
    def close() -> None:
        ...
    def add_log_file_generated(handler: winsdk.windows.foundation.TypedEventHandler[IFileLoggingSession, LogFileGeneratedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_log_file_generated(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class ILoggingChannel(winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    enabled: _winrt.Boolean
    level: LoggingLevel
    name: str
    def log_message(event_string: str) -> None:
        ...
    def log_message(event_string: str, level: LoggingLevel) -> None:
        ...
    def log_value_pair(value1: str, value2: _winrt.Int32) -> None:
        ...
    def log_value_pair(value1: str, value2: _winrt.Int32, level: LoggingLevel) -> None:
        ...
    def close() -> None:
        ...
    def add_logging_enabled(handler: winsdk.windows.foundation.TypedEventHandler[ILoggingChannel, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_logging_enabled(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class ILoggingSession(winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    name: str
    def add_logging_channel(logging_channel: ILoggingChannel) -> None:
        ...
    def add_logging_channel(logging_channel: ILoggingChannel, max_level: LoggingLevel) -> None:
        ...
    def remove_logging_channel(logging_channel: ILoggingChannel) -> None:
        ...
    def save_to_file_async(folder: winsdk.windows.storage.IStorageFolder, file_name: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]:
        ...
    def close() -> None:
        ...

class ILoggingTarget(_winrt.Object):
    ...
    def is_enabled() -> _winrt.Boolean:
        ...
    def is_enabled(level: LoggingLevel) -> _winrt.Boolean:
        ...
    def is_enabled(level: LoggingLevel, keywords: _winrt.Int64) -> _winrt.Boolean:
        ...
    def log_event(event_name: str) -> None:
        ...
    def log_event(event_name: str, fields: LoggingFields) -> None:
        ...
    def log_event(event_name: str, fields: LoggingFields, level: LoggingLevel) -> None:
        ...
    def log_event(event_name: str, fields: LoggingFields, level: LoggingLevel, options: LoggingOptions) -> None:
        ...
    def start_activity(start_event_name: str) -> LoggingActivity:
        ...
    def start_activity(start_event_name: str, fields: LoggingFields) -> LoggingActivity:
        ...
    def start_activity(start_event_name: str, fields: LoggingFields, level: LoggingLevel) -> LoggingActivity:
        ...
    def start_activity(start_event_name: str, fields: LoggingFields, level: LoggingLevel, options: LoggingOptions) -> LoggingActivity:
        ...

