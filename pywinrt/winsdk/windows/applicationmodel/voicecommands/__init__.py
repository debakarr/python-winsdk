# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.ApplicationModel.VoiceCommands")

try:
    import winsdk.windows.applicationmodel.appservice
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
    import winsdk.windows.globalization
except Exception:
    pass

try:
    import winsdk.windows.media.speechrecognition
except Exception:
    pass

try:
    import winsdk.windows.storage
except Exception:
    pass

class VoiceCommandCompletionReason(enum.IntEnum):
    UNKNOWN = 0
    COMMUNICATION_FAILED = 1
    RESOURCE_LIMITS_EXCEEDED = 2
    CANCELED = 3
    TIMEOUT_EXCEEDED = 4
    APP_LAUNCHED = 5
    COMPLETED = 6

class VoiceCommandContentTileType(enum.IntEnum):
    TITLE_ONLY = 0
    TITLE_WITH_TEXT = 1
    TITLE_WITH68X68_ICON = 2
    TITLE_WITH68X68_ICON_AND_TEXT = 3
    TITLE_WITH68X92_ICON = 4
    TITLE_WITH68X92_ICON_AND_TEXT = 5
    TITLE_WITH280X140_ICON = 6
    TITLE_WITH280X140_ICON_AND_TEXT = 7

VoiceCommand = _ns_module.VoiceCommand
VoiceCommandCompletedEventArgs = _ns_module.VoiceCommandCompletedEventArgs
VoiceCommandConfirmationResult = _ns_module.VoiceCommandConfirmationResult
VoiceCommandContentTile = _ns_module.VoiceCommandContentTile
VoiceCommandDefinition = _ns_module.VoiceCommandDefinition
VoiceCommandDefinitionManager = _ns_module.VoiceCommandDefinitionManager
VoiceCommandDisambiguationResult = _ns_module.VoiceCommandDisambiguationResult
VoiceCommandResponse = _ns_module.VoiceCommandResponse
VoiceCommandServiceConnection = _ns_module.VoiceCommandServiceConnection
VoiceCommandUserMessage = _ns_module.VoiceCommandUserMessage
