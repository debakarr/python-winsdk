# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Data.Json")

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

class JsonErrorStatus(enum.IntEnum):
    UNKNOWN = 0
    INVALID_JSON_STRING = 1
    INVALID_JSON_NUMBER = 2
    JSON_VALUE_NOT_FOUND = 3
    IMPLEMENTATION_LIMIT = 4

class JsonValueType(enum.IntEnum):
    NULL = 0
    BOOLEAN = 1
    NUMBER = 2
    STRING = 3
    ARRAY = 4
    OBJECT = 5

JsonArray = _ns_module.JsonArray
JsonError = _ns_module.JsonError
JsonObject = _ns_module.JsonObject
JsonValue = _ns_module.JsonValue
IJsonValue = _ns_module.IJsonValue
