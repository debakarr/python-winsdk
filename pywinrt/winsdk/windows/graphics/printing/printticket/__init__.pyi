# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.data.xml.dom
except Exception:
    pass

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

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

class PrintTicketCapabilities(_winrt.Object):
    ...
    document_binding_feature: PrintTicketFeature
    document_collate_feature: PrintTicketFeature
    document_duplex_feature: PrintTicketFeature
    document_hole_punch_feature: PrintTicketFeature
    document_input_bin_feature: PrintTicketFeature
    document_n_up_feature: PrintTicketFeature
    document_staple_feature: PrintTicketFeature
    job_passcode_feature: PrintTicketFeature
    name: str
    page_borderless_feature: PrintTicketFeature
    page_media_size_feature: PrintTicketFeature
    page_media_type_feature: PrintTicketFeature
    page_orientation_feature: PrintTicketFeature
    page_output_color_feature: PrintTicketFeature
    page_output_quality_feature: PrintTicketFeature
    page_resolution_feature: PrintTicketFeature
    xml_namespace: str
    xml_node: winsdk.windows.data.xml.dom.IXmlNode
    def get_feature(name: str, xml_namespace: str) -> PrintTicketFeature:
        ...
    def get_parameter_definition(name: str, xml_namespace: str) -> PrintTicketParameterDefinition:
        ...

class PrintTicketFeature(_winrt.Object):
    ...
    display_name: str
    name: str
    options: winsdk.windows.foundation.collections.IVectorView[PrintTicketOption]
    selection_type: PrintTicketFeatureSelectionType
    xml_namespace: str
    xml_node: winsdk.windows.data.xml.dom.IXmlNode
    def get_option(name: str, xml_namespace: str) -> PrintTicketOption:
        ...
    def get_selected_option() -> PrintTicketOption:
        ...
    def set_selected_option(value: PrintTicketOption) -> None:
        ...

class PrintTicketOption(_winrt.Object):
    ...
    display_name: str
    name: str
    xml_namespace: str
    xml_node: winsdk.windows.data.xml.dom.IXmlNode
    def get_property_node(name: str, xml_namespace: str) -> winsdk.windows.data.xml.dom.IXmlNode:
        ...
    def get_property_value(name: str, xml_namespace: str) -> PrintTicketValue:
        ...
    def get_scored_property_node(name: str, xml_namespace: str) -> winsdk.windows.data.xml.dom.IXmlNode:
        ...
    def get_scored_property_value(name: str, xml_namespace: str) -> PrintTicketValue:
        ...

class PrintTicketParameterDefinition(_winrt.Object):
    ...
    data_type: PrintTicketParameterDataType
    name: str
    range_max: _winrt.Int32
    range_min: _winrt.Int32
    unit_type: str
    xml_namespace: str
    xml_node: winsdk.windows.data.xml.dom.IXmlNode

class PrintTicketParameterInitializer(_winrt.Object):
    ...
    value: PrintTicketValue
    name: str
    xml_namespace: str
    xml_node: winsdk.windows.data.xml.dom.IXmlNode

class PrintTicketValue(_winrt.Object):
    ...
    type: PrintTicketValueType
    def get_value_as_integer() -> _winrt.Int32:
        ...
    def get_value_as_string() -> str:
        ...

class WorkflowPrintTicket(_winrt.Object):
    ...
    document_binding_feature: PrintTicketFeature
    document_collate_feature: PrintTicketFeature
    document_duplex_feature: PrintTicketFeature
    document_hole_punch_feature: PrintTicketFeature
    document_input_bin_feature: PrintTicketFeature
    document_n_up_feature: PrintTicketFeature
    document_staple_feature: PrintTicketFeature
    job_passcode_feature: PrintTicketFeature
    name: str
    page_borderless_feature: PrintTicketFeature
    page_media_size_feature: PrintTicketFeature
    page_media_type_feature: PrintTicketFeature
    page_orientation_feature: PrintTicketFeature
    page_output_color_feature: PrintTicketFeature
    page_output_quality_feature: PrintTicketFeature
    page_resolution_feature: PrintTicketFeature
    xml_namespace: str
    xml_node: winsdk.windows.data.xml.dom.IXmlNode
    def get_capabilities() -> PrintTicketCapabilities:
        ...
    def get_feature(name: str, xml_namespace: str) -> PrintTicketFeature:
        ...
    def get_parameter_initializer(name: str, xml_namespace: str) -> PrintTicketParameterInitializer:
        ...
    def merge_and_validate_ticket(delta_shema_ticket: WorkflowPrintTicket) -> WorkflowPrintTicket:
        ...
    def notify_xml_changed_async() -> winsdk.windows.foundation.IAsyncAction:
        ...
    def set_parameter_initializer_as_integer(name: str, xml_namespace: str, integer_value: _winrt.Int32) -> PrintTicketParameterInitializer:
        ...
    def set_parameter_initializer_as_string(name: str, xml_namespace: str, string_value: str) -> PrintTicketParameterInitializer:
        ...
    def validate_async() -> winsdk.windows.foundation.IAsyncOperation[WorkflowPrintTicketValidationResult]:
        ...

class WorkflowPrintTicketValidationResult(_winrt.Object):
    ...
    extended_error: winsdk.windows.foundation.HResult
    validated: _winrt.Boolean

