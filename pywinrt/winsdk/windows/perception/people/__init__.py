# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Perception.People")

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.numerics
except Exception:
    pass

try:
    import winsdk.windows.perception
except Exception:
    pass

try:
    import winsdk.windows.perception.spatial
except Exception:
    pass

try:
    import winsdk.windows.ui.input
except Exception:
    pass

try:
    import winsdk.windows.ui.input.spatial
except Exception:
    pass

class HandJointKind(enum.IntEnum):
    PALM = 0
    WRIST = 1
    THUMB_METACARPAL = 2
    THUMB_PROXIMAL = 3
    THUMB_DISTAL = 4
    THUMB_TIP = 5
    INDEX_METACARPAL = 6
    INDEX_PROXIMAL = 7
    INDEX_INTERMEDIATE = 8
    INDEX_DISTAL = 9
    INDEX_TIP = 10
    MIDDLE_METACARPAL = 11
    MIDDLE_PROXIMAL = 12
    MIDDLE_INTERMEDIATE = 13
    MIDDLE_DISTAL = 14
    MIDDLE_TIP = 15
    RING_METACARPAL = 16
    RING_PROXIMAL = 17
    RING_INTERMEDIATE = 18
    RING_DISTAL = 19
    RING_TIP = 20
    LITTLE_METACARPAL = 21
    LITTLE_PROXIMAL = 22
    LITTLE_INTERMEDIATE = 23
    LITTLE_DISTAL = 24
    LITTLE_TIP = 25

class JointPoseAccuracy(enum.IntEnum):
    HIGH = 0
    APPROXIMATE = 1

HandMeshVertex = _ns_module.HandMeshVertex
JointPose = _ns_module.JointPose
EyesPose = _ns_module.EyesPose
HandMeshObserver = _ns_module.HandMeshObserver
HandMeshVertexState = _ns_module.HandMeshVertexState
HandPose = _ns_module.HandPose
HeadPose = _ns_module.HeadPose
