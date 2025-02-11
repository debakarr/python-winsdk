# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.data.xml.dom
import winsdk.windows.foundation
import winsdk.windows.foundation.collections
import winsdk.windows.security.credentials

class SyndicationErrorStatus(enum.IntEnum):
    UNKNOWN = 0
    MISSING_REQUIRED_ELEMENT = 1
    MISSING_REQUIRED_ATTRIBUTE = 2
    INVALID_XML = 3
    UNEXPECTED_CONTENT = 4
    UNSUPPORTED_FORMAT = 5

class SyndicationFormat(enum.IntEnum):
    ATOM10 = 0
    RSS20 = 1
    RSS10 = 2
    RSS092 = 3
    RSS091 = 4
    ATOM03 = 5

class SyndicationTextType(enum.IntEnum):
    TEXT = 0
    HTML = 1
    XHTML = 2

Self = typing.TypeVar('Self')

class RetrievalProgress:
    bytes_retrieved: _winrt.UInt32
    total_bytes_to_retrieve: _winrt.UInt32
    def __init__(self, bytes_retrieved: _winrt.UInt32, total_bytes_to_retrieve: _winrt.UInt32) -> None: ...

class TransferProgress:
    bytes_sent: _winrt.UInt32
    total_bytes_to_send: _winrt.UInt32
    bytes_retrieved: _winrt.UInt32
    total_bytes_to_retrieve: _winrt.UInt32
    def __init__(self, bytes_sent: _winrt.UInt32, total_bytes_to_send: _winrt.UInt32, bytes_retrieved: _winrt.UInt32, total_bytes_to_retrieve: _winrt.UInt32) -> None: ...

class SyndicationAttribute(_winrt.Object):
    value: str
    namespace: str
    name: str
    @staticmethod
    def _from(obj: _winrt.Object) -> SyndicationAttribute: ...
    @typing.overload
    def __init__(self, attribute_name: str, attribute_namespace: str, attribute_value: str) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...

class SyndicationCategory(_winrt.Object):
    term: str
    scheme: str
    label: str
    node_value: str
    node_namespace: str
    node_name: str
    language: str
    base_uri: typing.Optional[winsdk.windows.foundation.Uri]
    attribute_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationAttribute]]
    element_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[ISyndicationNode]]
    @staticmethod
    def _from(obj: _winrt.Object) -> SyndicationCategory: ...
    @typing.overload
    def __init__(self, term: str) -> None: ...
    @typing.overload
    def __init__(self, term: str, scheme: str, label: str) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    def get_xml_document(self, format: SyndicationFormat) -> typing.Optional[winsdk.windows.data.xml.dom.XmlDocument]: ...

class SyndicationClient(_winrt.Object):
    timeout: _winrt.UInt32
    server_credential: typing.Optional[winsdk.windows.security.credentials.PasswordCredential]
    proxy_credential: typing.Optional[winsdk.windows.security.credentials.PasswordCredential]
    max_response_buffer_size: _winrt.UInt32
    bypass_cache_on_retrieve: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> SyndicationClient: ...
    @typing.overload
    def __init__(self, server_credential: typing.Optional[winsdk.windows.security.credentials.PasswordCredential]) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    def retrieve_feed_async(self, uri: typing.Optional[winsdk.windows.foundation.Uri]) -> winsdk.windows.foundation.IAsyncOperationWithProgress[SyndicationFeed, RetrievalProgress]: ...
    def set_request_header(self, name: str, value: str) -> None: ...

class SyndicationContent(_winrt.Object):
    source_uri: typing.Optional[winsdk.windows.foundation.Uri]
    node_value: str
    base_uri: typing.Optional[winsdk.windows.foundation.Uri]
    language: str
    node_name: str
    node_namespace: str
    attribute_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationAttribute]]
    element_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[ISyndicationNode]]
    text: str
    type: str
    xml: typing.Optional[winsdk.windows.data.xml.dom.XmlDocument]
    @staticmethod
    def _from(obj: _winrt.Object) -> SyndicationContent: ...
    @typing.overload
    def __init__(self, text: str, type: SyndicationTextType) -> None: ...
    @typing.overload
    def __init__(self, source_uri: typing.Optional[winsdk.windows.foundation.Uri]) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    def get_xml_document(self, format: SyndicationFormat) -> typing.Optional[winsdk.windows.data.xml.dom.XmlDocument]: ...

class SyndicationError(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> SyndicationError: ...
    @staticmethod
    def get_status(hresult: _winrt.Int32) -> SyndicationErrorStatus: ...

class SyndicationFeed(_winrt.Object):
    title: typing.Optional[ISyndicationText]
    subtitle: typing.Optional[ISyndicationText]
    rights: typing.Optional[ISyndicationText]
    generator: typing.Optional[SyndicationGenerator]
    last_updated_time: winsdk.windows.foundation.DateTime
    image_uri: typing.Optional[winsdk.windows.foundation.Uri]
    icon_uri: typing.Optional[winsdk.windows.foundation.Uri]
    id: str
    first_uri: typing.Optional[winsdk.windows.foundation.Uri]
    items: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationItem]]
    last_uri: typing.Optional[winsdk.windows.foundation.Uri]
    links: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationLink]]
    next_uri: typing.Optional[winsdk.windows.foundation.Uri]
    previous_uri: typing.Optional[winsdk.windows.foundation.Uri]
    categories: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationCategory]]
    source_format: SyndicationFormat
    contributors: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationPerson]]
    authors: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationPerson]]
    node_value: str
    node_namespace: str
    node_name: str
    language: str
    base_uri: typing.Optional[winsdk.windows.foundation.Uri]
    attribute_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationAttribute]]
    element_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[ISyndicationNode]]
    @staticmethod
    def _from(obj: _winrt.Object) -> SyndicationFeed: ...
    @typing.overload
    def __init__(self, title: str, subtitle: str, uri: typing.Optional[winsdk.windows.foundation.Uri]) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    def get_xml_document(self, format: SyndicationFormat) -> typing.Optional[winsdk.windows.data.xml.dom.XmlDocument]: ...
    def load(self, feed: str) -> None: ...
    def load_from_xml(self, feed_document: typing.Optional[winsdk.windows.data.xml.dom.XmlDocument]) -> None: ...

class SyndicationGenerator(_winrt.Object):
    version: str
    uri: typing.Optional[winsdk.windows.foundation.Uri]
    text: str
    node_value: str
    node_namespace: str
    node_name: str
    language: str
    base_uri: typing.Optional[winsdk.windows.foundation.Uri]
    attribute_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationAttribute]]
    element_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[ISyndicationNode]]
    @staticmethod
    def _from(obj: _winrt.Object) -> SyndicationGenerator: ...
    @typing.overload
    def __init__(self, text: str) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    def get_xml_document(self, format: SyndicationFormat) -> typing.Optional[winsdk.windows.data.xml.dom.XmlDocument]: ...

class SyndicationItem(_winrt.Object):
    title: typing.Optional[ISyndicationText]
    source: typing.Optional[SyndicationFeed]
    rights: typing.Optional[ISyndicationText]
    summary: typing.Optional[ISyndicationText]
    published_date: winsdk.windows.foundation.DateTime
    comments_uri: typing.Optional[winsdk.windows.foundation.Uri]
    id: str
    last_updated_time: winsdk.windows.foundation.DateTime
    content: typing.Optional[SyndicationContent]
    edit_uri: typing.Optional[winsdk.windows.foundation.Uri]
    links: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationLink]]
    authors: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationPerson]]
    categories: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationCategory]]
    contributors: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationPerson]]
    item_uri: typing.Optional[winsdk.windows.foundation.Uri]
    e_tag: str
    edit_media_uri: typing.Optional[winsdk.windows.foundation.Uri]
    node_value: str
    node_namespace: str
    node_name: str
    language: str
    base_uri: typing.Optional[winsdk.windows.foundation.Uri]
    attribute_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationAttribute]]
    element_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[ISyndicationNode]]
    @staticmethod
    def _from(obj: _winrt.Object) -> SyndicationItem: ...
    @typing.overload
    def __init__(self, title: str, content: typing.Optional[SyndicationContent], uri: typing.Optional[winsdk.windows.foundation.Uri]) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    def get_xml_document(self, format: SyndicationFormat) -> typing.Optional[winsdk.windows.data.xml.dom.XmlDocument]: ...
    def load(self, item: str) -> None: ...
    def load_from_xml(self, item_document: typing.Optional[winsdk.windows.data.xml.dom.XmlDocument]) -> None: ...

class SyndicationLink(_winrt.Object):
    uri: typing.Optional[winsdk.windows.foundation.Uri]
    title: str
    resource_language: str
    relationship: str
    media_type: str
    length: _winrt.UInt32
    node_value: str
    node_namespace: str
    node_name: str
    language: str
    base_uri: typing.Optional[winsdk.windows.foundation.Uri]
    attribute_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationAttribute]]
    element_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[ISyndicationNode]]
    @staticmethod
    def _from(obj: _winrt.Object) -> SyndicationLink: ...
    @typing.overload
    def __init__(self, uri: typing.Optional[winsdk.windows.foundation.Uri]) -> None: ...
    @typing.overload
    def __init__(self, uri: typing.Optional[winsdk.windows.foundation.Uri], relationship: str, title: str, media_type: str, length: _winrt.UInt32) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    def get_xml_document(self, format: SyndicationFormat) -> typing.Optional[winsdk.windows.data.xml.dom.XmlDocument]: ...

class SyndicationNode(_winrt.Object):
    node_value: str
    node_namespace: str
    node_name: str
    language: str
    base_uri: typing.Optional[winsdk.windows.foundation.Uri]
    attribute_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationAttribute]]
    element_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[ISyndicationNode]]
    @staticmethod
    def _from(obj: _winrt.Object) -> SyndicationNode: ...
    @typing.overload
    def __init__(self, node_name: str, node_namespace: str, node_value: str) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    def get_xml_document(self, format: SyndicationFormat) -> typing.Optional[winsdk.windows.data.xml.dom.XmlDocument]: ...

class SyndicationPerson(_winrt.Object):
    node_value: str
    node_namespace: str
    node_name: str
    language: str
    base_uri: typing.Optional[winsdk.windows.foundation.Uri]
    attribute_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationAttribute]]
    element_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[ISyndicationNode]]
    uri: typing.Optional[winsdk.windows.foundation.Uri]
    name: str
    email: str
    @staticmethod
    def _from(obj: _winrt.Object) -> SyndicationPerson: ...
    @typing.overload
    def __init__(self, name: str) -> None: ...
    @typing.overload
    def __init__(self, name: str, email: str, uri: typing.Optional[winsdk.windows.foundation.Uri]) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    def get_xml_document(self, format: SyndicationFormat) -> typing.Optional[winsdk.windows.data.xml.dom.XmlDocument]: ...

class SyndicationText(_winrt.Object):
    node_value: str
    node_namespace: str
    node_name: str
    language: str
    base_uri: typing.Optional[winsdk.windows.foundation.Uri]
    attribute_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationAttribute]]
    element_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[ISyndicationNode]]
    xml: typing.Optional[winsdk.windows.data.xml.dom.XmlDocument]
    type: str
    text: str
    @staticmethod
    def _from(obj: _winrt.Object) -> SyndicationText: ...
    @typing.overload
    def __init__(self, text: str) -> None: ...
    @typing.overload
    def __init__(self, text: str, type: SyndicationTextType) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    def get_xml_document(self, format: SyndicationFormat) -> typing.Optional[winsdk.windows.data.xml.dom.XmlDocument]: ...

class ISyndicationClient(_winrt.Object):
    bypass_cache_on_retrieve: _winrt.Boolean
    max_response_buffer_size: _winrt.UInt32
    proxy_credential: typing.Optional[winsdk.windows.security.credentials.PasswordCredential]
    server_credential: typing.Optional[winsdk.windows.security.credentials.PasswordCredential]
    timeout: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> ISyndicationClient: ...
    def retrieve_feed_async(self, uri: typing.Optional[winsdk.windows.foundation.Uri]) -> winsdk.windows.foundation.IAsyncOperationWithProgress[SyndicationFeed, RetrievalProgress]: ...
    def set_request_header(self, name: str, value: str) -> None: ...

class ISyndicationNode(_winrt.Object):
    attribute_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationAttribute]]
    base_uri: typing.Optional[winsdk.windows.foundation.Uri]
    element_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[ISyndicationNode]]
    language: str
    node_name: str
    node_namespace: str
    node_value: str
    @staticmethod
    def _from(obj: _winrt.Object) -> ISyndicationNode: ...
    def get_xml_document(self, format: SyndicationFormat) -> typing.Optional[winsdk.windows.data.xml.dom.XmlDocument]: ...

class ISyndicationText(_winrt.Object):
    text: str
    type: str
    xml: typing.Optional[winsdk.windows.data.xml.dom.XmlDocument]
    attribute_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[SyndicationAttribute]]
    base_uri: typing.Optional[winsdk.windows.foundation.Uri]
    element_extensions: typing.Optional[winsdk.windows.foundation.collections.IVector[ISyndicationNode]]
    language: str
    node_name: str
    node_namespace: str
    node_value: str
    @staticmethod
    def _from(obj: _winrt.Object) -> ISyndicationText: ...
    def get_xml_document(self, format: SyndicationFormat) -> typing.Optional[winsdk.windows.data.xml.dom.XmlDocument]: ...

