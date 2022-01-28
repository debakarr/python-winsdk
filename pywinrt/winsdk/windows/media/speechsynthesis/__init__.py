# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Media.SpeechSynthesis")

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.media
except Exception:
    pass

try:
    import winsdk.windows.media.core
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class SpeechAppendedSilence(enum.IntEnum):
    DEFAULT = 0
    MIN = 1

class SpeechPunctuationSilence(enum.IntEnum):
    DEFAULT = 0
    MIN = 1

class VoiceGender(enum.IntEnum):
    MALE = 0
    FEMALE = 1

SpeechSynthesisStream = _ns_module.SpeechSynthesisStream
SpeechSynthesizer = _ns_module.SpeechSynthesizer
SpeechSynthesizerOptions = _ns_module.SpeechSynthesizerOptions
VoiceInformation = _ns_module.VoiceInformation
