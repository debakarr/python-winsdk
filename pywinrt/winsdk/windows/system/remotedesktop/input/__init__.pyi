# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

class RemoteTextConnection(winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    is_enabled: _winrt.Boolean
    def __init__(self, connection_id: uuid.UUID, pdu_forwarder: RemoteTextConnectionDataHandler) -> None:
        ...
    def close() -> None:
        ...
    def register_thread(thread_id: _winrt.UInt32) -> None:
        ...
    def report_data_received(pdu_data: typing.Sequence[_winrt.UInt8]) -> None:
        ...
    def unregister_thread(thread_id: _winrt.UInt32) -> None:
        ...

RemoteTextConnectionDataHandler = typing.Callable[[typing.Sequence[_winrt.UInt8]], _winrt.Boolean]

