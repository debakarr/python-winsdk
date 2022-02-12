# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.applicationmodel
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

class AddPackageByAppInstallerOptions(enum.IntFlag):
    NONE = 0
    INSTALL_ALL_RESOURCES = 0x20
    FORCE_TARGET_APP_SHUTDOWN = 0x40
    REQUIRED_CONTENT_GROUP_ONLY = 0x100
    LIMIT_TO_EXISTING_PACKAGES = 0x200

class DeploymentOptions(enum.IntFlag):
    NONE = 0
    FORCE_APPLICATION_SHUTDOWN = 0x1
    DEVELOPMENT_MODE = 0x2
    INSTALL_ALL_RESOURCES = 0x20
    FORCE_TARGET_APPLICATION_SHUTDOWN = 0x40
    REQUIRED_CONTENT_GROUP_ONLY = 0x100
    FORCE_UPDATE_FROM_ANY_VERSION = 0x40000
    RETAIN_FILES_ON_FAILURE = 0x200000
    STAGE_IN_PLACE = 0x400000

class DeploymentProgressState(enum.IntEnum):
    QUEUED = 0
    PROCESSING = 1

class PackageInstallState(enum.IntEnum):
    NOT_INSTALLED = 0
    STAGED = 1
    INSTALLED = 2
    PAUSED = 6

class PackageState(enum.IntEnum):
    NORMAL = 0
    LICENSE_INVALID = 1
    MODIFIED = 2
    TAMPERED = 3

class PackageStatus(enum.IntFlag):
    O_K = 0
    LICENSE_ISSUE = 0x1
    MODIFIED = 0x2
    TAMPERED = 0x4
    DISABLED = 0x8

class PackageStubPreference(enum.IntEnum):
    FULL = 0
    STUB = 1

class PackageTypes(enum.IntFlag):
    NONE = 0
    MAIN = 0x1
    FRAMEWORK = 0x2
    RESOURCE = 0x4
    BUNDLE = 0x8
    XAP = 0x10
    OPTIONAL = 0x20
    ALL = 0xffffffff

class RemovalOptions(enum.IntFlag):
    NONE = 0
    PRESERVE_APPLICATION_DATA = 0x1000
    PRESERVE_ROAMABLE_APPLICATION_DATA = 0x80
    REMOVE_FOR_ALL_USERS = 0x80000

class StubPackageOption(enum.IntEnum):
    DEFAULT = 0
    INSTALL_FULL = 1
    INSTALL_STUB = 2
    USE_PREFERENCE = 3

class DeploymentProgress:
    state: DeploymentProgressState
    percentage: _winrt.UInt32
    def __init__(self, state: DeploymentProgressState, percentage: _winrt.UInt32) -> None: ...

class AddPackageOptions(_winrt.Object):
    target_volume: PackageVolume
    stub_package_option: StubPackageOption
    stage_in_place: _winrt.Boolean
    retain_files_on_failure: _winrt.Boolean
    required_content_group_only: _winrt.Boolean
    install_all_resources: _winrt.Boolean
    force_update_from_any_version: _winrt.Boolean
    force_target_app_shutdown: _winrt.Boolean
    force_app_shutdown: _winrt.Boolean
    external_location_uri: winsdk.windows.foundation.Uri
    developer_mode: _winrt.Boolean
    defer_registration_when_packages_are_in_use: _winrt.Boolean
    allow_unsigned: _winrt.Boolean
    dependency_package_uris: winsdk.windows.foundation.collections.IVector[winsdk.windows.foundation.Uri]
    optional_package_family_names: winsdk.windows.foundation.collections.IVector[str]
    optional_package_uris: winsdk.windows.foundation.collections.IVector[winsdk.windows.foundation.Uri]
    related_package_uris: winsdk.windows.foundation.collections.IVector[winsdk.windows.foundation.Uri]
    @staticmethod
    def _from(obj: _winrt.Object) -> AddPackageOptions: ...
    @typing.overload
    def __init__(self) -> None: ...

class AppInstallerManager(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> AppInstallerManager: ...
    @typing.overload
    def clear_auto_update_settings(self, package_family_name: str) -> None: ...
    @typing.overload
    @staticmethod
    def get_default() -> AppInstallerManager: ...
    @typing.overload
    @staticmethod
    def get_for_system() -> AppInstallerManager: ...
    @typing.overload
    def pause_auto_updates_until(self, package_family_name: str, date_time: winsdk.windows.foundation.DateTime) -> None: ...
    @typing.overload
    def set_auto_update_settings(self, package_family_name: str, app_installer_info: AutoUpdateSettingsOptions) -> None: ...

class AutoUpdateSettingsOptions(_winrt.Object):
    version: winsdk.windows.applicationmodel.PackageVersion
    update_blocks_activation: _winrt.Boolean
    show_prompt: _winrt.Boolean
    on_launch: _winrt.Boolean
    is_auto_repair_enabled: _winrt.Boolean
    hours_between_update_checks: _winrt.UInt32
    force_update_from_any_version: _winrt.Boolean
    automatic_background_task: _winrt.Boolean
    app_installer_uri: winsdk.windows.foundation.Uri
    dependency_package_uris: winsdk.windows.foundation.collections.IVector[winsdk.windows.foundation.Uri]
    optional_package_uris: winsdk.windows.foundation.collections.IVector[winsdk.windows.foundation.Uri]
    repair_uris: winsdk.windows.foundation.collections.IVector[winsdk.windows.foundation.Uri]
    update_uris: winsdk.windows.foundation.collections.IVector[winsdk.windows.foundation.Uri]
    @staticmethod
    def _from(obj: _winrt.Object) -> AutoUpdateSettingsOptions: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    @staticmethod
    def create_from_app_installer_info(app_installer_info: winsdk.windows.applicationmodel.AppInstallerInfo) -> AutoUpdateSettingsOptions: ...

class DeploymentResult(_winrt.Object):
    activity_id: uuid.UUID
    error_text: str
    extended_error_code: winsdk.windows.foundation.HResult
    is_registered: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> DeploymentResult: ...

class PackageAllUserProvisioningOptions(_winrt.Object):
    optional_package_family_names: winsdk.windows.foundation.collections.IVector[str]
    projection_order_package_family_names: winsdk.windows.foundation.collections.IVector[str]
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageAllUserProvisioningOptions: ...
    @typing.overload
    def __init__(self) -> None: ...

class PackageManager(_winrt.Object):
    debug_settings: PackageManagerDebugSettings
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageManager: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def add_package_async(self, package_uri: winsdk.windows.foundation.Uri, dependency_package_uris: typing.Iterable[winsdk.windows.foundation.Uri], deployment_options: DeploymentOptions) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def add_package_async(self, package_uri: winsdk.windows.foundation.Uri, dependency_package_uris: typing.Iterable[winsdk.windows.foundation.Uri], deployment_options: DeploymentOptions, target_volume: PackageVolume) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def add_package_async(self, package_uri: winsdk.windows.foundation.Uri, dependency_package_uris: typing.Iterable[winsdk.windows.foundation.Uri], deployment_options: DeploymentOptions, target_volume: PackageVolume, optional_package_family_names: typing.Iterable[str], external_package_uris: typing.Iterable[winsdk.windows.foundation.Uri]) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def add_package_async(self, package_uri: winsdk.windows.foundation.Uri, dependency_package_uris: typing.Iterable[winsdk.windows.foundation.Uri], options: DeploymentOptions, target_volume: PackageVolume, optional_package_family_names: typing.Iterable[str], package_uris_to_install: typing.Iterable[winsdk.windows.foundation.Uri], related_package_uris: typing.Iterable[winsdk.windows.foundation.Uri]) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def add_package_by_app_installer_file_async(self, app_installer_file_uri: winsdk.windows.foundation.Uri, options: AddPackageByAppInstallerOptions, target_volume: PackageVolume) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def add_package_by_uri_async(self, package_uri: winsdk.windows.foundation.Uri, options: AddPackageOptions) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def add_package_volume_async(self, package_store_path: str) -> winsdk.windows.foundation.IAsyncOperation[PackageVolume]: ...
    @typing.overload
    def cleanup_package_for_user_async(self, package_name: str, user_security_id: str) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def clear_package_status(self, package_full_name: str, status: PackageStatus) -> None: ...
    @typing.overload
    def deprovision_package_for_all_users_async(self, package_family_name: str) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def find_package(self, package_full_name: str) -> winsdk.windows.applicationmodel.Package: ...
    @typing.overload
    def find_package_for_user(self, user_security_id: str, package_full_name: str) -> winsdk.windows.applicationmodel.Package: ...
    @typing.overload
    def find_package_volume(self, volume_name: str) -> PackageVolume: ...
    @typing.overload
    def find_package_volumes(self) -> winsdk.windows.foundation.collections.IIterable[PackageVolume]: ...
    @typing.overload
    def find_packages(self) -> winsdk.windows.foundation.collections.IIterable[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages(self, package_family_name: str) -> winsdk.windows.foundation.collections.IIterable[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages(self, package_name: str, package_publisher: str) -> winsdk.windows.foundation.collections.IIterable[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages_for_user(self, user_security_id: str) -> winsdk.windows.foundation.collections.IIterable[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages_for_user(self, user_security_id: str, package_family_name: str) -> winsdk.windows.foundation.collections.IIterable[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages_for_user(self, user_security_id: str, package_name: str, package_publisher: str) -> winsdk.windows.foundation.collections.IIterable[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages_for_user_with_package_types(self, user_security_id: str, package_types: PackageTypes) -> winsdk.windows.foundation.collections.IIterable[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages_for_user_with_package_types(self, user_security_id: str, package_family_name: str, package_types: PackageTypes) -> winsdk.windows.foundation.collections.IIterable[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages_for_user_with_package_types(self, user_security_id: str, package_name: str, package_publisher: str, package_types: PackageTypes) -> winsdk.windows.foundation.collections.IIterable[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages_with_package_types(self, package_types: PackageTypes) -> winsdk.windows.foundation.collections.IIterable[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages_with_package_types(self, package_family_name: str, package_types: PackageTypes) -> winsdk.windows.foundation.collections.IIterable[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages_with_package_types(self, package_name: str, package_publisher: str, package_types: PackageTypes) -> winsdk.windows.foundation.collections.IIterable[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_provisioned_packages(self) -> winsdk.windows.foundation.collections.IVector[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_users(self, package_full_name: str) -> winsdk.windows.foundation.collections.IIterable[PackageUserInformation]: ...
    @typing.overload
    def get_default_package_volume(self) -> PackageVolume: ...
    @typing.overload
    def get_package_stub_preference(self, package_family_name: str) -> PackageStubPreference: ...
    @typing.overload
    def get_package_volumes_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[PackageVolume]]: ...
    @typing.overload
    def move_package_to_volume_async(self, package_full_name: str, deployment_options: DeploymentOptions, target_volume: PackageVolume) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def provision_package_for_all_users_async(self, package_family_name: str) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def provision_package_for_all_users_async(self, main_package_family_name: str, options: PackageAllUserProvisioningOptions) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def register_package_async(self, manifest_uri: winsdk.windows.foundation.Uri, dependency_package_uris: typing.Iterable[winsdk.windows.foundation.Uri], deployment_options: DeploymentOptions) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def register_package_async(self, manifest_uri: winsdk.windows.foundation.Uri, dependency_package_uris: typing.Iterable[winsdk.windows.foundation.Uri], deployment_options: DeploymentOptions, app_data_volume: PackageVolume) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def register_package_by_family_name_async(self, main_package_family_name: str, dependency_package_family_names: typing.Iterable[str], deployment_options: DeploymentOptions, app_data_volume: PackageVolume, optional_package_family_names: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def register_package_by_full_name_async(self, main_package_full_name: str, dependency_package_full_names: typing.Iterable[str], deployment_options: DeploymentOptions) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def register_package_by_uri_async(self, manifest_uri: winsdk.windows.foundation.Uri, options: RegisterPackageOptions) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def register_packages_by_full_name_async(self, package_full_names: typing.Iterable[str], options: RegisterPackageOptions) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def remove_package_async(self, package_full_name: str) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def remove_package_async(self, package_full_name: str, removal_options: RemovalOptions) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def remove_package_volume_async(self, volume: PackageVolume) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def request_add_package_async(self, package_uri: winsdk.windows.foundation.Uri, dependency_package_uris: typing.Iterable[winsdk.windows.foundation.Uri], deployment_options: DeploymentOptions, target_volume: PackageVolume, optional_package_family_names: typing.Iterable[str], related_package_uris: typing.Iterable[winsdk.windows.foundation.Uri]) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def request_add_package_async(self, package_uri: winsdk.windows.foundation.Uri, dependency_package_uris: typing.Iterable[winsdk.windows.foundation.Uri], deployment_options: DeploymentOptions, target_volume: PackageVolume, optional_package_family_names: typing.Iterable[str], related_package_uris: typing.Iterable[winsdk.windows.foundation.Uri], package_uris_to_install: typing.Iterable[winsdk.windows.foundation.Uri]) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def request_add_package_by_app_installer_file_async(self, app_installer_file_uri: winsdk.windows.foundation.Uri, options: AddPackageByAppInstallerOptions, target_volume: PackageVolume) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def set_default_package_volume(self, volume: PackageVolume) -> None: ...
    @typing.overload
    def set_package_state(self, package_full_name: str, package_state: PackageState) -> None: ...
    @typing.overload
    def set_package_status(self, package_full_name: str, status: PackageStatus) -> None: ...
    @typing.overload
    def set_package_stub_preference(self, package_family_name: str, use_stub: PackageStubPreference) -> None: ...
    @typing.overload
    def set_package_volume_offline_async(self, package_volume: PackageVolume) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def set_package_volume_online_async(self, package_volume: PackageVolume) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def stage_package_async(self, package_uri: winsdk.windows.foundation.Uri, dependency_package_uris: typing.Iterable[winsdk.windows.foundation.Uri]) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def stage_package_async(self, package_uri: winsdk.windows.foundation.Uri, dependency_package_uris: typing.Iterable[winsdk.windows.foundation.Uri], deployment_options: DeploymentOptions) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def stage_package_async(self, package_uri: winsdk.windows.foundation.Uri, dependency_package_uris: typing.Iterable[winsdk.windows.foundation.Uri], deployment_options: DeploymentOptions, target_volume: PackageVolume) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def stage_package_async(self, package_uri: winsdk.windows.foundation.Uri, dependency_package_uris: typing.Iterable[winsdk.windows.foundation.Uri], deployment_options: DeploymentOptions, target_volume: PackageVolume, optional_package_family_names: typing.Iterable[str], external_package_uris: typing.Iterable[winsdk.windows.foundation.Uri]) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def stage_package_async(self, package_uri: winsdk.windows.foundation.Uri, dependency_package_uris: typing.Iterable[winsdk.windows.foundation.Uri], options: DeploymentOptions, target_volume: PackageVolume, optional_package_family_names: typing.Iterable[str], package_uris_to_install: typing.Iterable[winsdk.windows.foundation.Uri], related_package_uris: typing.Iterable[winsdk.windows.foundation.Uri]) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def stage_package_by_uri_async(self, package_uri: winsdk.windows.foundation.Uri, options: StagePackageOptions) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def stage_user_data_async(self, package_full_name: str) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def stage_user_data_async(self, package_full_name: str, deployment_options: DeploymentOptions) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...
    @typing.overload
    def update_package_async(self, package_uri: winsdk.windows.foundation.Uri, dependency_package_uris: typing.Iterable[winsdk.windows.foundation.Uri], deployment_options: DeploymentOptions) -> winsdk.windows.foundation.IAsyncOperationWithProgress[DeploymentResult, DeploymentProgress]: ...

class PackageManagerDebugSettings(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageManagerDebugSettings: ...
    @typing.overload
    def set_content_group_state_async(self, package: winsdk.windows.applicationmodel.Package, content_group_name: str, state: winsdk.windows.applicationmodel.PackageContentGroupState) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def set_content_group_state_async(self, package: winsdk.windows.applicationmodel.Package, content_group_name: str, state: winsdk.windows.applicationmodel.PackageContentGroupState, completion_percentage: _winrt.Double) -> winsdk.windows.foundation.IAsyncAction: ...

class PackageUserInformation(_winrt.Object):
    install_state: PackageInstallState
    user_security_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageUserInformation: ...

class PackageVolume(_winrt.Object):
    is_offline: _winrt.Boolean
    is_system_volume: _winrt.Boolean
    mount_point: str
    name: str
    package_store_path: str
    supports_hard_links: _winrt.Boolean
    is_appx_install_supported: _winrt.Boolean
    is_full_trust_package_supported: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageVolume: ...
    @typing.overload
    def find_package(self, package_full_name: str) -> winsdk.windows.foundation.collections.IVector[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_package_for_user(self, user_security_id: str, package_full_name: str) -> winsdk.windows.foundation.collections.IVector[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages(self) -> winsdk.windows.foundation.collections.IVector[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages(self, package_family_name: str) -> winsdk.windows.foundation.collections.IVector[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages(self, package_name: str, package_publisher: str) -> winsdk.windows.foundation.collections.IVector[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages_for_user(self, user_security_id: str) -> winsdk.windows.foundation.collections.IVector[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages_for_user(self, user_security_id: str, package_family_name: str) -> winsdk.windows.foundation.collections.IVector[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages_for_user(self, user_security_id: str, package_name: str, package_publisher: str) -> winsdk.windows.foundation.collections.IVector[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages_for_user_with_package_types(self, user_security_id: str, package_types: PackageTypes) -> winsdk.windows.foundation.collections.IVector[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages_for_user_with_package_types(self, user_security_id: str, package_types: PackageTypes, package_family_name: str) -> winsdk.windows.foundation.collections.IVector[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages_for_user_with_package_types(self, user_security_id: str, package_types: PackageTypes, package_name: str, package_publisher: str) -> winsdk.windows.foundation.collections.IVector[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages_with_package_types(self, package_types: PackageTypes) -> winsdk.windows.foundation.collections.IVector[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages_with_package_types(self, package_types: PackageTypes, package_family_name: str) -> winsdk.windows.foundation.collections.IVector[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def find_packages_with_package_types(self, package_types: PackageTypes, package_name: str, package_publisher: str) -> winsdk.windows.foundation.collections.IVector[winsdk.windows.applicationmodel.Package]: ...
    @typing.overload
    def get_available_space_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.UInt64]: ...

class RegisterPackageOptions(_winrt.Object):
    stage_in_place: _winrt.Boolean
    install_all_resources: _winrt.Boolean
    force_update_from_any_version: _winrt.Boolean
    force_target_app_shutdown: _winrt.Boolean
    force_app_shutdown: _winrt.Boolean
    external_location_uri: winsdk.windows.foundation.Uri
    developer_mode: _winrt.Boolean
    defer_registration_when_packages_are_in_use: _winrt.Boolean
    app_data_volume: PackageVolume
    allow_unsigned: _winrt.Boolean
    dependency_package_uris: winsdk.windows.foundation.collections.IVector[winsdk.windows.foundation.Uri]
    optional_package_family_names: winsdk.windows.foundation.collections.IVector[str]
    @staticmethod
    def _from(obj: _winrt.Object) -> RegisterPackageOptions: ...
    @typing.overload
    def __init__(self) -> None: ...

class StagePackageOptions(_winrt.Object):
    target_volume: PackageVolume
    stub_package_option: StubPackageOption
    stage_in_place: _winrt.Boolean
    required_content_group_only: _winrt.Boolean
    install_all_resources: _winrt.Boolean
    force_update_from_any_version: _winrt.Boolean
    external_location_uri: winsdk.windows.foundation.Uri
    developer_mode: _winrt.Boolean
    allow_unsigned: _winrt.Boolean
    dependency_package_uris: winsdk.windows.foundation.collections.IVector[winsdk.windows.foundation.Uri]
    optional_package_family_names: winsdk.windows.foundation.collections.IVector[str]
    optional_package_uris: winsdk.windows.foundation.collections.IVector[winsdk.windows.foundation.Uri]
    related_package_uris: winsdk.windows.foundation.collections.IVector[winsdk.windows.foundation.Uri]
    @staticmethod
    def _from(obj: _winrt.Object) -> StagePackageOptions: ...
    @typing.overload
    def __init__(self) -> None: ...

