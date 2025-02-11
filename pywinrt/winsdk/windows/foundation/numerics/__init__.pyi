# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

Self = typing.TypeVar('Self')

class Matrix3x2:
    m11: _winrt.Single
    m12: _winrt.Single
    m21: _winrt.Single
    m22: _winrt.Single
    m31: _winrt.Single
    m32: _winrt.Single
    def __init__(self, m11: _winrt.Single, m12: _winrt.Single, m21: _winrt.Single, m22: _winrt.Single, m31: _winrt.Single, m32: _winrt.Single) -> None: ...

class Matrix4x4:
    m11: _winrt.Single
    m12: _winrt.Single
    m13: _winrt.Single
    m14: _winrt.Single
    m21: _winrt.Single
    m22: _winrt.Single
    m23: _winrt.Single
    m24: _winrt.Single
    m31: _winrt.Single
    m32: _winrt.Single
    m33: _winrt.Single
    m34: _winrt.Single
    m41: _winrt.Single
    m42: _winrt.Single
    m43: _winrt.Single
    m44: _winrt.Single
    def __init__(self, m11: _winrt.Single, m12: _winrt.Single, m13: _winrt.Single, m14: _winrt.Single, m21: _winrt.Single, m22: _winrt.Single, m23: _winrt.Single, m24: _winrt.Single, m31: _winrt.Single, m32: _winrt.Single, m33: _winrt.Single, m34: _winrt.Single, m41: _winrt.Single, m42: _winrt.Single, m43: _winrt.Single, m44: _winrt.Single) -> None: ...

class Plane:
    normal: Vector3
    d: _winrt.Single
    def __init__(self, normal: Vector3, d: _winrt.Single) -> None: ...

class Quaternion:
    x: _winrt.Single
    y: _winrt.Single
    z: _winrt.Single
    w: _winrt.Single
    def __init__(self, x: _winrt.Single, y: _winrt.Single, z: _winrt.Single, w: _winrt.Single) -> None: ...

class Rational:
    numerator: _winrt.UInt32
    denominator: _winrt.UInt32
    def __init__(self, numerator: _winrt.UInt32, denominator: _winrt.UInt32) -> None: ...

class Vector2:
    x: _winrt.Single
    y: _winrt.Single
    def __init__(self, x: _winrt.Single, y: _winrt.Single) -> None: ...

class Vector3:
    x: _winrt.Single
    y: _winrt.Single
    z: _winrt.Single
    def __init__(self, x: _winrt.Single, y: _winrt.Single, z: _winrt.Single) -> None: ...

class Vector4:
    x: _winrt.Single
    y: _winrt.Single
    z: _winrt.Single
    w: _winrt.Single
    def __init__(self, x: _winrt.Single, y: _winrt.Single, z: _winrt.Single, w: _winrt.Single) -> None: ...

