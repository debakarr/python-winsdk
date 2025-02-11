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

class PrintTicketFeatureSelectionType(enum.IntEnum):
    PICK_ONE = 0
    PICK_MANY = 1

class PrintTicketParameterDataType(enum.IntEnum):
    INTEGER = 0
    NUMERIC_STRING = 1
    STRING = 2

class PrintTicketValueType(enum.IntEnum):
    INTEGER = 0
    STRING = 1
    UNKNOWN = 2

Self = typing.TypeVar('Self')

class PrintTicketCapabilities(_winrt.Object):
    document_binding_feature: typing.Optional[PrintTicketFeature]
    document_collate_feature: typing.Optional[PrintTicketFeature]
    document_duplex_feature: typing.Optional[PrintTicketFeature]
    document_hole_punch_feature: typing.Optional[PrintTicketFeature]
    document_input_bin_feature: typing.Optional[PrintTicketFeature]
    document_n_up_feature: typing.Optional[PrintTicketFeature]
    document_staple_feature: typing.Optional[PrintTicketFeature]
    job_passcode_feature: typing.Optional[PrintTicketFeature]
    name: str
    page_borderless_feature: typing.Optional[PrintTicketFeature]
    page_media_size_feature: typing.Optional[PrintTicketFeature]
    page_media_type_feature: typing.Optional[PrintTicketFeature]
    page_orientation_feature: typing.Optional[PrintTicketFeature]
    page_output_color_feature: typing.Optional[PrintTicketFeature]
    page_output_quality_feature: typing.Optional[PrintTicketFeature]
    page_resolution_feature: typing.Optional[PrintTicketFeature]
    xml_namespace: str
    xml_node: typing.Optional[winsdk.windows.data.xml.dom.IXmlNode]
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintTicketCapabilities: ...
    def get_feature(self, name: str, xml_namespace: str) -> typing.Optional[PrintTicketFeature]: ...
    def get_parameter_definition(self, name: str, xml_namespace: str) -> typing.Optional[PrintTicketParameterDefinition]: ...

class PrintTicketFeature(_winrt.Object):
    display_name: str
    name: str
    options: typing.Optional[winsdk.windows.foundation.collections.IVectorView[PrintTicketOption]]
    selection_type: PrintTicketFeatureSelectionType
    xml_namespace: str
    xml_node: typing.Optional[winsdk.windows.data.xml.dom.IXmlNode]
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintTicketFeature: ...
    def get_option(self, name: str, xml_namespace: str) -> typing.Optional[PrintTicketOption]: ...
    def get_selected_option(self) -> typing.Optional[PrintTicketOption]: ...
    def set_selected_option(self, value: typing.Optional[PrintTicketOption]) -> None: ...

class PrintTicketOption(_winrt.Object):
    display_name: str
    name: str
    xml_namespace: str
    xml_node: typing.Optional[winsdk.windows.data.xml.dom.IXmlNode]
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintTicketOption: ...
    def get_property_node(self, name: str, xml_namespace: str) -> typing.Optional[winsdk.windows.data.xml.dom.IXmlNode]: ...
    def get_property_value(self, name: str, xml_namespace: str) -> typing.Optional[PrintTicketValue]: ...
    def get_scored_property_node(self, name: str, xml_namespace: str) -> typing.Optional[winsdk.windows.data.xml.dom.IXmlNode]: ...
    def get_scored_property_value(self, name: str, xml_namespace: str) -> typing.Optional[PrintTicketValue]: ...

class PrintTicketParameterDefinition(_winrt.Object):
    data_type: PrintTicketParameterDataType
    name: str
    range_max: _winrt.Int32
    range_min: _winrt.Int32
    unit_type: str
    xml_namespace: str
    xml_node: typing.Optional[winsdk.windows.data.xml.dom.IXmlNode]
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintTicketParameterDefinition: ...

class PrintTicketParameterInitializer(_winrt.Object):
    value: typing.Optional[PrintTicketValue]
    name: str
    xml_namespace: str
    xml_node: typing.Optional[winsdk.windows.data.xml.dom.IXmlNode]
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintTicketParameterInitializer: ...

class PrintTicketValue(_winrt.Object):
    type: PrintTicketValueType
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintTicketValue: ...
    def get_value_as_integer(self) -> _winrt.Int32: ...
    def get_value_as_string(self) -> str: ...

class WorkflowPrintTicket(_winrt.Object):
    document_binding_feature: typing.Optional[PrintTicketFeature]
    document_collate_feature: typing.Optional[PrintTicketFeature]
    document_duplex_feature: typing.Optional[PrintTicketFeature]
    document_hole_punch_feature: typing.Optional[PrintTicketFeature]
    document_input_bin_feature: typing.Optional[PrintTicketFeature]
    document_n_up_feature: typing.Optional[PrintTicketFeature]
    document_staple_feature: typing.Optional[PrintTicketFeature]
    job_passcode_feature: typing.Optional[PrintTicketFeature]
    name: str
    page_borderless_feature: typing.Optional[PrintTicketFeature]
    page_media_size_feature: typing.Optional[PrintTicketFeature]
    page_media_type_feature: typing.Optional[PrintTicketFeature]
    page_orientation_feature: typing.Optional[PrintTicketFeature]
    page_output_color_feature: typing.Optional[PrintTicketFeature]
    page_output_quality_feature: typing.Optional[PrintTicketFeature]
    page_resolution_feature: typing.Optional[PrintTicketFeature]
    xml_namespace: str
    xml_node: typing.Optional[winsdk.windows.data.xml.dom.IXmlNode]
    @staticmethod
    def _from(obj: _winrt.Object) -> WorkflowPrintTicket: ...
    def get_capabilities(self) -> typing.Optional[PrintTicketCapabilities]: ...
    def get_feature(self, name: str, xml_namespace: str) -> typing.Optional[PrintTicketFeature]: ...
    def get_parameter_initializer(self, name: str, xml_namespace: str) -> typing.Optional[PrintTicketParameterInitializer]: ...
    def merge_and_validate_ticket(self, delta_shema_ticket: typing.Optional[WorkflowPrintTicket]) -> typing.Optional[WorkflowPrintTicket]: ...
    def notify_xml_changed_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def set_parameter_initializer_as_integer(self, name: str, xml_namespace: str, integer_value: _winrt.Int32) -> typing.Optional[PrintTicketParameterInitializer]: ...
    def set_parameter_initializer_as_string(self, name: str, xml_namespace: str, string_value: str) -> typing.Optional[PrintTicketParameterInitializer]: ...
    def validate_async(self) -> winsdk.windows.foundation.IAsyncOperation[WorkflowPrintTicketValidationResult]: ...

class WorkflowPrintTicketValidationResult(_winrt.Object):
    extended_error: winsdk.windows.foundation.HResult
    validated: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> WorkflowPrintTicketValidationResult: ...

