# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Web.UI.Interop")

try:
    import winsdk.windows.applicationmodel.datatransfer
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
    import winsdk.windows.storage.streams
except Exception:
    pass

try:
    import winsdk.windows.system
except Exception:
    pass

try:
    import winsdk.windows.ui
except Exception:
    pass

try:
    import winsdk.windows.ui.core
except Exception:
    pass

try:
    import winsdk.windows.web
except Exception:
    pass

try:
    import winsdk.windows.web.http
except Exception:
    pass

try:
    import winsdk.windows.web.ui
except Exception:
    pass

class WebViewControlAcceleratorKeyRoutingStage(enum.IntEnum):
    TUNNELING = 0
    BUBBLING = 1

class WebViewControlMoveFocusReason(enum.IntEnum):
    PROGRAMMATIC = 0
    NEXT = 1
    PREVIOUS = 2

class WebViewControlProcessCapabilityState(enum.IntEnum):
    DEFAULT = 0
    DISABLED = 1
    ENABLED = 2

WebViewControl = _ns_module.WebViewControl
WebViewControlAcceleratorKeyPressedEventArgs = _ns_module.WebViewControlAcceleratorKeyPressedEventArgs
WebViewControlMoveFocusRequestedEventArgs = _ns_module.WebViewControlMoveFocusRequestedEventArgs
WebViewControlProcess = _ns_module.WebViewControlProcess
WebViewControlProcessOptions = _ns_module.WebViewControlProcessOptions
