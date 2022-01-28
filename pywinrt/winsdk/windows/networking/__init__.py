# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Networking")

try:
    import winsdk.windows.networking.connectivity
except Exception:
    pass

class DomainNameType(enum.IntEnum):
    SUFFIX = 0
    FULLY_QUALIFIED = 1

class HostNameSortOptions(enum.IntFlag):
    NONE = 0
    OPTIMIZE_FOR_LONG_CONNECTIONS = 0x2

class HostNameType(enum.IntEnum):
    DOMAIN_NAME = 0
    IPV4 = 1
    IPV6 = 2
    BLUETOOTH = 3

EndpointPair = _ns_module.EndpointPair
HostName = _ns_module.HostName
