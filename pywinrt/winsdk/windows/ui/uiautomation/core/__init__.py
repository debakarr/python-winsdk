# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.UI.UIAutomation.Core")

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.ui.uiautomation
except Exception:
    pass

class AutomationRemoteOperationStatus(enum.IntEnum):
    SUCCESS = 0
    MALFORMED_BYTECODE = 1
    INSTRUCTION_LIMIT_EXCEEDED = 2
    UNHANDLED_EXCEPTION = 3
    EXECUTION_FAILURE = 4

AutomationAnnotationTypeRegistration = _ns_module.AutomationAnnotationTypeRegistration
AutomationRemoteOperationOperandId = _ns_module.AutomationRemoteOperationOperandId
AutomationRemoteOperationResult = _ns_module.AutomationRemoteOperationResult
CoreAutomationRegistrar = _ns_module.CoreAutomationRegistrar
CoreAutomationRemoteOperation = _ns_module.CoreAutomationRemoteOperation
CoreAutomationRemoteOperationContext = _ns_module.CoreAutomationRemoteOperationContext
RemoteAutomationClientSession = _ns_module.RemoteAutomationClientSession
RemoteAutomationConnectionRequestedEventArgs = _ns_module.RemoteAutomationConnectionRequestedEventArgs
RemoteAutomationDisconnectedEventArgs = _ns_module.RemoteAutomationDisconnectedEventArgs
RemoteAutomationServer = _ns_module.RemoteAutomationServer
RemoteAutomationWindow = _ns_module.RemoteAutomationWindow
ICoreAutomationConnectionBoundObjectProvider = _ns_module.ICoreAutomationConnectionBoundObjectProvider
ICoreAutomationRemoteOperationExtensionProvider = _ns_module.ICoreAutomationRemoteOperationExtensionProvider
