# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Devices.Perception.Provider")

try:
    import winsdk.windows.devices.perception
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
    import winsdk.windows.foundation.numerics
except Exception:
    pass

try:
    import winsdk.windows.graphics.imaging
except Exception:
    pass

try:
    import winsdk.windows.media
except Exception:
    pass

KnownPerceptionFrameKind = _ns_module.KnownPerceptionFrameKind
PerceptionControlGroup = _ns_module.PerceptionControlGroup
PerceptionCorrelation = _ns_module.PerceptionCorrelation
PerceptionCorrelationGroup = _ns_module.PerceptionCorrelationGroup
PerceptionFaceAuthenticationGroup = _ns_module.PerceptionFaceAuthenticationGroup
PerceptionFrame = _ns_module.PerceptionFrame
PerceptionFrameProviderInfo = _ns_module.PerceptionFrameProviderInfo
PerceptionFrameProviderManagerService = _ns_module.PerceptionFrameProviderManagerService
PerceptionPropertyChangeRequest = _ns_module.PerceptionPropertyChangeRequest
PerceptionVideoFrameAllocator = _ns_module.PerceptionVideoFrameAllocator
IPerceptionFrameProvider = _ns_module.IPerceptionFrameProvider
IPerceptionFrameProviderManager = _ns_module.IPerceptionFrameProviderManager
