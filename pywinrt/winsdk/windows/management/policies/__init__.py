# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Management.Policies")

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

try:
    import winsdk.windows.system
except Exception:
    pass

class NamedPolicyKind(enum.IntEnum):
    INVALID = 0
    BINARY = 1
    BOOLEAN = 2
    INT32 = 3
    INT64 = 4
    STRING = 5

NamedPolicy = _ns_module.NamedPolicy
NamedPolicyData = _ns_module.NamedPolicyData
