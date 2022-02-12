# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.applicationmodel.activation
except Exception:
    pass

try:
    import winsdk.windows.devices.printers
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

try:
    import winsdk.windows.graphics.printing.printticket
except Exception:
    pass

try:
    import winsdk.windows.storage
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

class PrintWorkflowJobAbortReason(enum.IntEnum):
    JOB_FAILED = 0
    USER_CANCELED = 1

class PrintWorkflowPdlConversionType(enum.IntEnum):
    XPS_TO_PDF = 0
    XPS_TO_PWGR = 1
    XPS_TO_PCLM = 2

class PrintWorkflowPrinterJobStatus(enum.IntEnum):
    ERROR = 0
    ABORTED = 1
    IN_PROGRESS = 2
    COMPLETED = 3

class PrintWorkflowSessionStatus(enum.IntEnum):
    STARTED = 0
    COMPLETED = 1
    ABORTED = 2
    CLOSED = 3
    PDL_DATA_AVAILABLE_FOR_MODIFICATION = 4

class PrintWorkflowSubmittedStatus(enum.IntEnum):
    SUCCEEDED = 0
    CANCELED = 1
    FAILED = 2

class PrintWorkflowUICompletionStatus(enum.IntEnum):
    COMPLETED = 0
    LAUNCH_FAILED = 1
    JOB_FAILED = 2
    USER_CANCELED = 3

class PrintWorkflowBackgroundSession(_winrt.Object):
    status: PrintWorkflowSessionStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowBackgroundSession: ...
    @typing.overload
    def start(self) -> None: ...
    @typing.overload
    def add_setup_requested(self, setup_event_handler: winsdk.windows.foundation.TypedEventHandler[PrintWorkflowBackgroundSession, PrintWorkflowBackgroundSetupRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_setup_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_submitted(self, submitted_event_handler: winsdk.windows.foundation.TypedEventHandler[PrintWorkflowBackgroundSession, PrintWorkflowSubmittedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_submitted(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class PrintWorkflowBackgroundSetupRequestedEventArgs(_winrt.Object):
    configuration: PrintWorkflowConfiguration
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowBackgroundSetupRequestedEventArgs: ...
    @typing.overload
    def get_deferral(self) -> winsdk.windows.foundation.Deferral: ...
    @typing.overload
    def get_user_print_ticket_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.graphics.printing.printticket.WorkflowPrintTicket]: ...
    @typing.overload
    def set_requires_u_i(self) -> None: ...

class PrintWorkflowConfiguration(_winrt.Object):
    job_title: str
    session_id: str
    source_app_display_name: str
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowConfiguration: ...
    @typing.overload
    def abort_print_flow(self, reason: PrintWorkflowJobAbortReason) -> None: ...

class PrintWorkflowForegroundSession(_winrt.Object):
    status: PrintWorkflowSessionStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowForegroundSession: ...
    @typing.overload
    def start(self) -> None: ...
    @typing.overload
    def add_setup_requested(self, setup_event_handler: winsdk.windows.foundation.TypedEventHandler[PrintWorkflowForegroundSession, PrintWorkflowForegroundSetupRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_setup_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_xps_data_available(self, xps_data_available_event_handler: winsdk.windows.foundation.TypedEventHandler[PrintWorkflowForegroundSession, PrintWorkflowXpsDataAvailableEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_xps_data_available(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class PrintWorkflowForegroundSetupRequestedEventArgs(_winrt.Object):
    configuration: PrintWorkflowConfiguration
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowForegroundSetupRequestedEventArgs: ...
    @typing.overload
    def get_deferral(self) -> winsdk.windows.foundation.Deferral: ...
    @typing.overload
    def get_user_print_ticket_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.graphics.printing.printticket.WorkflowPrintTicket]: ...

class PrintWorkflowJobActivatedEventArgs(winsdk.windows.applicationmodel.activation.IActivatedEventArgs, winsdk.windows.applicationmodel.activation.IActivatedEventArgsWithUser, _winrt.Object):
    kind: winsdk.windows.applicationmodel.activation.ActivationKind
    previous_execution_state: winsdk.windows.applicationmodel.activation.ApplicationExecutionState
    splash_screen: winsdk.windows.applicationmodel.activation.SplashScreen
    user: winsdk.windows.system.User
    session: PrintWorkflowJobUISession
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowJobActivatedEventArgs: ...

class PrintWorkflowJobBackgroundSession(_winrt.Object):
    status: PrintWorkflowSessionStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowJobBackgroundSession: ...
    @typing.overload
    def start(self) -> None: ...
    @typing.overload
    def add_job_starting(self, handler: winsdk.windows.foundation.TypedEventHandler[PrintWorkflowJobBackgroundSession, PrintWorkflowJobStartingEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_job_starting(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_pdl_modification_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[PrintWorkflowJobBackgroundSession, PrintWorkflowPdlModificationRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_pdl_modification_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class PrintWorkflowJobNotificationEventArgs(_winrt.Object):
    configuration: PrintWorkflowConfiguration
    printer_job: PrintWorkflowPrinterJob
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowJobNotificationEventArgs: ...
    @typing.overload
    def get_deferral(self) -> winsdk.windows.foundation.Deferral: ...

class PrintWorkflowJobStartingEventArgs(_winrt.Object):
    configuration: PrintWorkflowConfiguration
    printer: winsdk.windows.devices.printers.IppPrintDevice
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowJobStartingEventArgs: ...
    @typing.overload
    def get_deferral(self) -> winsdk.windows.foundation.Deferral: ...
    @typing.overload
    def set_skip_system_rendering(self) -> None: ...

class PrintWorkflowJobTriggerDetails(_winrt.Object):
    print_workflow_job_session: PrintWorkflowJobBackgroundSession
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowJobTriggerDetails: ...

class PrintWorkflowJobUISession(_winrt.Object):
    status: PrintWorkflowSessionStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowJobUISession: ...
    @typing.overload
    def start(self) -> None: ...
    @typing.overload
    def add_job_notification(self, handler: winsdk.windows.foundation.TypedEventHandler[PrintWorkflowJobUISession, PrintWorkflowJobNotificationEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_job_notification(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_pdl_data_available(self, handler: winsdk.windows.foundation.TypedEventHandler[PrintWorkflowJobUISession, PrintWorkflowPdlDataAvailableEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_pdl_data_available(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class PrintWorkflowObjectModelSourceFileContent(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowObjectModelSourceFileContent: ...
    @typing.overload
    def __init__(self, xps_stream: winsdk.windows.storage.streams.IInputStream) -> None: ...

class PrintWorkflowObjectModelTargetPackage(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowObjectModelTargetPackage: ...

class PrintWorkflowPdlConverter(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowPdlConverter: ...
    @typing.overload
    def convert_pdl_async(self, print_ticket: winsdk.windows.graphics.printing.printticket.WorkflowPrintTicket, input_stream: winsdk.windows.storage.streams.IInputStream, output_stream: winsdk.windows.storage.streams.IOutputStream) -> winsdk.windows.foundation.IAsyncAction: ...

class PrintWorkflowPdlDataAvailableEventArgs(_winrt.Object):
    configuration: PrintWorkflowConfiguration
    printer_job: PrintWorkflowPrinterJob
    source_content: PrintWorkflowPdlSourceContent
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowPdlDataAvailableEventArgs: ...
    @typing.overload
    def get_deferral(self) -> winsdk.windows.foundation.Deferral: ...

class PrintWorkflowPdlModificationRequestedEventArgs(_winrt.Object):
    configuration: PrintWorkflowConfiguration
    printer_job: PrintWorkflowPrinterJob
    source_content: PrintWorkflowPdlSourceContent
    u_i_launcher: PrintWorkflowUILauncher
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowPdlModificationRequestedEventArgs: ...
    @typing.overload
    def create_job_on_printer(self, target_content_type: str) -> PrintWorkflowPdlTargetStream: ...
    @typing.overload
    def create_job_on_printer_with_attributes(self, job_attributes: typing.Iterable[winsdk.windows.foundation.collections.IKeyValuePair[str, winsdk.windows.devices.printers.IppAttributeValue]], target_content_type: str) -> PrintWorkflowPdlTargetStream: ...
    @typing.overload
    def create_job_on_printer_with_attributes_buffer(self, job_attributes_buffer: winsdk.windows.storage.streams.IBuffer, target_content_type: str) -> PrintWorkflowPdlTargetStream: ...
    @typing.overload
    def get_deferral(self) -> winsdk.windows.foundation.Deferral: ...
    @typing.overload
    def get_pdl_converter(self, conversion_type: PrintWorkflowPdlConversionType) -> PrintWorkflowPdlConverter: ...

class PrintWorkflowPdlSourceContent(_winrt.Object):
    content_type: str
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowPdlSourceContent: ...
    @typing.overload
    def get_content_file_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]: ...
    @typing.overload
    def get_input_stream(self) -> winsdk.windows.storage.streams.IInputStream: ...

class PrintWorkflowPdlTargetStream(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowPdlTargetStream: ...
    @typing.overload
    def complete_stream_submission(self, status: PrintWorkflowSubmittedStatus) -> None: ...
    @typing.overload
    def get_output_stream(self) -> winsdk.windows.storage.streams.IOutputStream: ...

class PrintWorkflowPrinterJob(_winrt.Object):
    job_id: _winrt.Int32
    printer: winsdk.windows.devices.printers.IppPrintDevice
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowPrinterJob: ...
    @typing.overload
    def get_job_attributes(self, attribute_names: typing.Iterable[str]) -> winsdk.windows.foundation.collections.IMap[str, winsdk.windows.devices.printers.IppAttributeValue]: ...
    @typing.overload
    def get_job_attributes_as_buffer(self, attribute_names: typing.Iterable[str]) -> winsdk.windows.storage.streams.IBuffer: ...
    @typing.overload
    def get_job_print_ticket(self) -> winsdk.windows.graphics.printing.printticket.WorkflowPrintTicket: ...
    @typing.overload
    def get_job_status(self) -> PrintWorkflowPrinterJobStatus: ...
    @typing.overload
    def set_job_attributes(self, job_attributes: typing.Iterable[winsdk.windows.foundation.collections.IKeyValuePair[str, winsdk.windows.devices.printers.IppAttributeValue]]) -> winsdk.windows.devices.printers.IppSetAttributesResult: ...
    @typing.overload
    def set_job_attributes_from_buffer(self, job_attributes_buffer: winsdk.windows.storage.streams.IBuffer) -> winsdk.windows.devices.printers.IppSetAttributesResult: ...

class PrintWorkflowSourceContent(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowSourceContent: ...
    @typing.overload
    def get_job_print_ticket_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.graphics.printing.printticket.WorkflowPrintTicket]: ...
    @typing.overload
    def get_source_spool_data_as_stream_content(self) -> PrintWorkflowSpoolStreamContent: ...
    @typing.overload
    def get_source_spool_data_as_xps_object_model(self) -> PrintWorkflowObjectModelSourceFileContent: ...

class PrintWorkflowSpoolStreamContent(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowSpoolStreamContent: ...
    @typing.overload
    def get_input_stream(self) -> winsdk.windows.storage.streams.IInputStream: ...

class PrintWorkflowStreamTarget(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowStreamTarget: ...
    @typing.overload
    def get_output_stream(self) -> winsdk.windows.storage.streams.IOutputStream: ...

class PrintWorkflowSubmittedEventArgs(_winrt.Object):
    operation: PrintWorkflowSubmittedOperation
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowSubmittedEventArgs: ...
    @typing.overload
    def get_deferral(self) -> winsdk.windows.foundation.Deferral: ...
    @typing.overload
    def get_target(self, job_print_ticket: winsdk.windows.graphics.printing.printticket.WorkflowPrintTicket) -> PrintWorkflowTarget: ...

class PrintWorkflowSubmittedOperation(_winrt.Object):
    configuration: PrintWorkflowConfiguration
    xps_content: PrintWorkflowSourceContent
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowSubmittedOperation: ...
    @typing.overload
    def complete(self, status: PrintWorkflowSubmittedStatus) -> None: ...

class PrintWorkflowTarget(_winrt.Object):
    target_as_stream: PrintWorkflowStreamTarget
    target_as_xps_object_model_package: PrintWorkflowObjectModelTargetPackage
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowTarget: ...

class PrintWorkflowTriggerDetails(_winrt.Object):
    print_workflow_session: PrintWorkflowBackgroundSession
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowTriggerDetails: ...

class PrintWorkflowUIActivatedEventArgs(winsdk.windows.applicationmodel.activation.IActivatedEventArgsWithUser, winsdk.windows.applicationmodel.activation.IActivatedEventArgs, _winrt.Object):
    kind: winsdk.windows.applicationmodel.activation.ActivationKind
    previous_execution_state: winsdk.windows.applicationmodel.activation.ApplicationExecutionState
    splash_screen: winsdk.windows.applicationmodel.activation.SplashScreen
    user: winsdk.windows.system.User
    print_workflow_session: PrintWorkflowForegroundSession
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowUIActivatedEventArgs: ...

class PrintWorkflowUILauncher(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowUILauncher: ...
    @typing.overload
    def is_u_i_launch_enabled(self) -> _winrt.Boolean: ...
    @typing.overload
    def launch_and_complete_u_i_async(self) -> winsdk.windows.foundation.IAsyncOperation[PrintWorkflowUICompletionStatus]: ...

class PrintWorkflowXpsDataAvailableEventArgs(_winrt.Object):
    operation: PrintWorkflowSubmittedOperation
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintWorkflowXpsDataAvailableEventArgs: ...
    @typing.overload
    def get_deferral(self) -> winsdk.windows.foundation.Deferral: ...

