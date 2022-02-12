# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.data.xml.dom
except Exception:
    pass

class XsltProcessor(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> XsltProcessor: ...
    @typing.overload
    def __init__(self, document: winsdk.windows.data.xml.dom.XmlDocument) -> None: ...
    @typing.overload
    def transform_to_document(self, input_node: winsdk.windows.data.xml.dom.IXmlNode) -> winsdk.windows.data.xml.dom.XmlDocument: ...
    @typing.overload
    def transform_to_string(self, input_node: winsdk.windows.data.xml.dom.IXmlNode) -> str: ...

