# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Devices.Midi")

try:
    import winsdk.windows.devices.enumeration
except ImportError:
    pass

try:
    import winsdk.windows.foundation
except ImportError:
    pass

try:
    import winsdk.windows.storage.streams
except ImportError:
    pass

class MidiMessageType(enum.IntEnum):
    NONE = 0
    NOTE_OFF = 128
    NOTE_ON = 144
    POLYPHONIC_KEY_PRESSURE = 160
    CONTROL_CHANGE = 176
    PROGRAM_CHANGE = 192
    CHANNEL_PRESSURE = 208
    PITCH_BEND_CHANGE = 224
    SYSTEM_EXCLUSIVE = 240
    MIDI_TIME_CODE = 241
    SONG_POSITION_POINTER = 242
    SONG_SELECT = 243
    TUNE_REQUEST = 246
    END_SYSTEM_EXCLUSIVE = 247
    TIMING_CLOCK = 248
    START = 250
    CONTINUE = 251
    STOP = 252
    ACTIVE_SENSING = 254
    SYSTEM_RESET = 255

_ns_module._register_MidiMessageType(MidiMessageType)

MidiActiveSensingMessage = _ns_module.MidiActiveSensingMessage
MidiChannelPressureMessage = _ns_module.MidiChannelPressureMessage
MidiContinueMessage = _ns_module.MidiContinueMessage
MidiControlChangeMessage = _ns_module.MidiControlChangeMessage
MidiInPort = _ns_module.MidiInPort
MidiMessageReceivedEventArgs = _ns_module.MidiMessageReceivedEventArgs
MidiNoteOffMessage = _ns_module.MidiNoteOffMessage
MidiNoteOnMessage = _ns_module.MidiNoteOnMessage
MidiOutPort = _ns_module.MidiOutPort
MidiPitchBendChangeMessage = _ns_module.MidiPitchBendChangeMessage
MidiPolyphonicKeyPressureMessage = _ns_module.MidiPolyphonicKeyPressureMessage
MidiProgramChangeMessage = _ns_module.MidiProgramChangeMessage
MidiSongPositionPointerMessage = _ns_module.MidiSongPositionPointerMessage
MidiSongSelectMessage = _ns_module.MidiSongSelectMessage
MidiStartMessage = _ns_module.MidiStartMessage
MidiStopMessage = _ns_module.MidiStopMessage
MidiSynthesizer = _ns_module.MidiSynthesizer
MidiSystemExclusiveMessage = _ns_module.MidiSystemExclusiveMessage
MidiSystemResetMessage = _ns_module.MidiSystemResetMessage
MidiTimeCodeMessage = _ns_module.MidiTimeCodeMessage
MidiTimingClockMessage = _ns_module.MidiTimingClockMessage
MidiTuneRequestMessage = _ns_module.MidiTuneRequestMessage
IMidiMessage = _ns_module.IMidiMessage
IMidiOutPort = _ns_module.IMidiOutPort
