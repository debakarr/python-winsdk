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
    import winsdk.windows.applicationmodel.core
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

class AddResourcePackageOptions(enum.IntFlag):
    NONE = 0
    FORCE_TARGET_APP_SHUTDOWN = 0x1
    APPLY_UPDATE_IF_AVAILABLE = 0x2

class AppExecutionContext(enum.IntEnum):
    UNKNOWN = 0
    HOST = 1
    GUEST = 2

class AppInstallerPolicySource(enum.IntEnum):
    DEFAULT = 0
    SYSTEM = 1

class LimitedAccessFeatureStatus(enum.IntEnum):
    UNAVAILABLE = 0
    AVAILABLE = 1
    AVAILABLE_WITHOUT_TOKEN = 2
    UNKNOWN = 3

class PackageContentGroupState(enum.IntEnum):
    NOT_STAGED = 0
    QUEUED = 1
    STAGING = 2
    STAGED = 3

class PackageSignatureKind(enum.IntEnum):
    NONE = 0
    DEVELOPER = 1
    ENTERPRISE = 2
    STORE = 3
    SYSTEM = 4

class PackageUpdateAvailability(enum.IntEnum):
    UNKNOWN = 0
    NO_UPDATES = 1
    AVAILABLE = 2
    REQUIRED = 3
    ERROR = 4

class StartupTaskState(enum.IntEnum):
    DISABLED = 0
    DISABLED_BY_USER = 1
    ENABLED = 2
    DISABLED_BY_POLICY = 3
    ENABLED_BY_POLICY = 4

class PackageInstallProgress:
    percent_complete: _winrt.UInt32
    def __init__(self, percent_complete: _winrt.UInt32) -> None: ...

class PackageVersion:
    major: _winrt.UInt16
    minor: _winrt.UInt16
    build: _winrt.UInt16
    revision: _winrt.UInt16
    def __init__(self, major: _winrt.UInt16, minor: _winrt.UInt16, build: _winrt.UInt16, revision: _winrt.UInt16) -> None: ...

class AppDisplayInfo(_winrt.Object):
    description: str
    display_name: str
    @staticmethod
    def _from(obj: _winrt.Object) -> AppDisplayInfo: ...
    @typing.overload
    def get_logo(self, size: winsdk.windows.foundation.Size) -> winsdk.windows.storage.streams.RandomAccessStreamReference: ...

class AppInfo(_winrt.Object):
    app_user_model_id: str
    display_info: AppDisplayInfo
    id: str
    package_family_name: str
    package: Package
    execution_context: AppExecutionContext
    supported_file_extensions: str
    current: AppInfo
    @staticmethod
    def _from(obj: _winrt.Object) -> AppInfo: ...
    @typing.overload
    @staticmethod
    def get_from_app_user_model_id(app_user_model_id: str) -> AppInfo: ...
    @typing.overload
    @staticmethod
    def get_from_app_user_model_id_for_user(user: winsdk.windows.system.User, app_user_model_id: str) -> AppInfo: ...

class AppInstallerInfo(_winrt.Object):
    uri: winsdk.windows.foundation.Uri
    automatic_background_task: _winrt.Boolean
    dependency_package_uris: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.foundation.Uri]
    force_update_from_any_version: _winrt.Boolean
    hours_between_update_checks: _winrt.UInt32
    is_auto_repair_enabled: _winrt.Boolean
    last_checked: winsdk.windows.foundation.DateTime
    on_launch: _winrt.Boolean
    optional_package_uris: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.foundation.Uri]
    paused_until: typing.Optional[winsdk.windows.foundation.DateTime]
    policy_source: AppInstallerPolicySource
    repair_uris: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.foundation.Uri]
    show_prompt: _winrt.Boolean
    update_blocks_activation: _winrt.Boolean
    update_uris: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.foundation.Uri]
    version: PackageVersion
    @staticmethod
    def _from(obj: _winrt.Object) -> AppInstallerInfo: ...

class AppInstance(_winrt.Object):
    is_current_instance: _winrt.Boolean
    key: str
    recommended_instance: AppInstance
    @staticmethod
    def _from(obj: _winrt.Object) -> AppInstance: ...
    @typing.overload
    @staticmethod
    def find_or_register_instance_for_key(key: str) -> AppInstance: ...
    @typing.overload
    @staticmethod
    def get_activated_event_args() -> winsdk.windows.applicationmodel.activation.IActivatedEventArgs: ...
    @typing.overload
    @staticmethod
    def get_instances() -> winsdk.windows.foundation.collections.IVector[AppInstance]: ...
    @typing.overload
    def redirect_activation_to(self) -> None: ...
    @typing.overload
    @staticmethod
    def unregister() -> None: ...

class DesignMode(_winrt.Object):
    design_mode_enabled: _winrt.Boolean
    design_mode2_enabled: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> DesignMode: ...

class EnteredBackgroundEventArgs(IEnteredBackgroundEventArgs, _winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> EnteredBackgroundEventArgs: ...
    @typing.overload
    def get_deferral(self) -> winsdk.windows.foundation.Deferral: ...

class LeavingBackgroundEventArgs(ILeavingBackgroundEventArgs, _winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> LeavingBackgroundEventArgs: ...
    @typing.overload
    def get_deferral(self) -> winsdk.windows.foundation.Deferral: ...

class LimitedAccessFeatureRequestResult(_winrt.Object):
    estimated_removal_date: typing.Optional[winsdk.windows.foundation.DateTime]
    feature_id: str
    status: LimitedAccessFeatureStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> LimitedAccessFeatureRequestResult: ...

class LimitedAccessFeatures(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> LimitedAccessFeatures: ...
    @typing.overload
    @staticmethod
    def try_unlock_feature(feature_id: str, token: str, attestation: str) -> LimitedAccessFeatureRequestResult: ...

class Package(_winrt.Object):
    dependencies: winsdk.windows.foundation.collections.IVectorView[Package]
    id: PackageId
    installed_location: winsdk.windows.storage.StorageFolder
    is_framework: _winrt.Boolean
    description: str
    display_name: str
    is_bundle: _winrt.Boolean
    is_development_mode: _winrt.Boolean
    is_resource_package: _winrt.Boolean
    logo: winsdk.windows.foundation.Uri
    publisher_display_name: str
    installed_date: winsdk.windows.foundation.DateTime
    status: PackageStatus
    is_optional: _winrt.Boolean
    signature_kind: PackageSignatureKind
    effective_location: winsdk.windows.storage.StorageFolder
    mutable_location: winsdk.windows.storage.StorageFolder
    effective_external_location: winsdk.windows.storage.StorageFolder
    effective_external_path: str
    effective_path: str
    installed_path: str
    is_stub: _winrt.Boolean
    machine_external_location: winsdk.windows.storage.StorageFolder
    machine_external_path: str
    mutable_path: str
    user_external_location: winsdk.windows.storage.StorageFolder
    user_external_path: str
    install_date: winsdk.windows.foundation.DateTime
    current: Package
    @staticmethod
    def _from(obj: _winrt.Object) -> Package: ...
    @typing.overload
    def check_update_availability_async(self) -> winsdk.windows.foundation.IAsyncOperation[PackageUpdateAvailabilityResult]: ...
    @typing.overload
    def get_app_installer_info(self) -> AppInstallerInfo: ...
    @typing.overload
    def get_app_list_entries(self) -> winsdk.windows.foundation.collections.IVectorView[winsdk.windows.applicationmodel.core.AppListEntry]: ...
    @typing.overload
    def get_app_list_entries_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.applicationmodel.core.AppListEntry]]: ...
    @typing.overload
    def get_content_group_async(self, name: str) -> winsdk.windows.foundation.IAsyncOperation[PackageContentGroup]: ...
    @typing.overload
    def get_content_groups_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVector[PackageContentGroup]]: ...
    @typing.overload
    def get_logo_as_random_access_stream_reference(self, size: winsdk.windows.foundation.Size) -> winsdk.windows.storage.streams.RandomAccessStreamReference: ...
    @typing.overload
    def get_thumbnail_token(self) -> str: ...
    @typing.overload
    def launch(self, parameters: str) -> None: ...
    @typing.overload
    def set_in_use_async(self, in_use: _winrt.Boolean) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def stage_content_groups_async(self, names: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVector[PackageContentGroup]]: ...
    @typing.overload
    def stage_content_groups_async(self, names: typing.Iterable[str], move_to_head_of_queue: _winrt.Boolean) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVector[PackageContentGroup]]: ...
    @typing.overload
    def verify_content_integrity_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...

class PackageCatalog(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageCatalog: ...
    @typing.overload
    def add_optional_package_async(self, optional_package_family_name: str) -> winsdk.windows.foundation.IAsyncOperation[PackageCatalogAddOptionalPackageResult]: ...
    @typing.overload
    def add_resource_package_async(self, resource_package_family_name: str, resource_i_d: str, options: AddResourcePackageOptions) -> winsdk.windows.foundation.IAsyncOperationWithProgress[PackageCatalogAddResourcePackageResult, PackageInstallProgress]: ...
    @typing.overload
    @staticmethod
    def open_for_current_package() -> PackageCatalog: ...
    @typing.overload
    @staticmethod
    def open_for_current_user() -> PackageCatalog: ...
    @typing.overload
    def remove_optional_packages_async(self, optional_package_family_names: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperation[PackageCatalogRemoveOptionalPackagesResult]: ...
    @typing.overload
    def remove_resource_packages_async(self, resource_packages: typing.Iterable[Package]) -> winsdk.windows.foundation.IAsyncOperation[PackageCatalogRemoveResourcePackagesResult]: ...
    @typing.overload
    def add_package_installing(self, handler: winsdk.windows.foundation.TypedEventHandler[PackageCatalog, PackageInstallingEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_package_installing(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_package_staging(self, handler: winsdk.windows.foundation.TypedEventHandler[PackageCatalog, PackageStagingEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_package_staging(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_package_status_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[PackageCatalog, PackageStatusChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_package_status_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_package_uninstalling(self, handler: winsdk.windows.foundation.TypedEventHandler[PackageCatalog, PackageUninstallingEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_package_uninstalling(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_package_updating(self, handler: winsdk.windows.foundation.TypedEventHandler[PackageCatalog, PackageUpdatingEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_package_updating(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_package_content_group_staging(self, handler: winsdk.windows.foundation.TypedEventHandler[PackageCatalog, PackageContentGroupStagingEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_package_content_group_staging(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class PackageCatalogAddOptionalPackageResult(_winrt.Object):
    extended_error: winsdk.windows.foundation.HResult
    package: Package
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageCatalogAddOptionalPackageResult: ...

class PackageCatalogAddResourcePackageResult(_winrt.Object):
    extended_error: winsdk.windows.foundation.HResult
    is_complete: _winrt.Boolean
    package: Package
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageCatalogAddResourcePackageResult: ...

class PackageCatalogRemoveOptionalPackagesResult(_winrt.Object):
    extended_error: winsdk.windows.foundation.HResult
    packages_removed: winsdk.windows.foundation.collections.IVectorView[Package]
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageCatalogRemoveOptionalPackagesResult: ...

class PackageCatalogRemoveResourcePackagesResult(_winrt.Object):
    extended_error: winsdk.windows.foundation.HResult
    packages_removed: winsdk.windows.foundation.collections.IVectorView[Package]
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageCatalogRemoveResourcePackagesResult: ...

class PackageContentGroup(_winrt.Object):
    is_required: _winrt.Boolean
    name: str
    package: Package
    state: PackageContentGroupState
    required_group_name: str
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageContentGroup: ...

class PackageContentGroupStagingEventArgs(_winrt.Object):
    activity_id: uuid.UUID
    content_group_name: str
    error_code: winsdk.windows.foundation.HResult
    is_complete: _winrt.Boolean
    is_content_group_required: _winrt.Boolean
    package: Package
    progress: _winrt.Double
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageContentGroupStagingEventArgs: ...

class PackageId(_winrt.Object):
    architecture: winsdk.windows.system.ProcessorArchitecture
    family_name: str
    full_name: str
    name: str
    publisher: str
    publisher_id: str
    resource_id: str
    version: PackageVersion
    author: str
    product_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageId: ...

class PackageInstallingEventArgs(_winrt.Object):
    activity_id: uuid.UUID
    error_code: winsdk.windows.foundation.HResult
    is_complete: _winrt.Boolean
    package: Package
    progress: _winrt.Double
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageInstallingEventArgs: ...

class PackageStagingEventArgs(_winrt.Object):
    activity_id: uuid.UUID
    error_code: winsdk.windows.foundation.HResult
    is_complete: _winrt.Boolean
    package: Package
    progress: _winrt.Double
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageStagingEventArgs: ...

class PackageStatus(_winrt.Object):
    data_offline: _winrt.Boolean
    dependency_issue: _winrt.Boolean
    deployment_in_progress: _winrt.Boolean
    disabled: _winrt.Boolean
    license_issue: _winrt.Boolean
    modified: _winrt.Boolean
    needs_remediation: _winrt.Boolean
    not_available: _winrt.Boolean
    package_offline: _winrt.Boolean
    servicing: _winrt.Boolean
    tampered: _winrt.Boolean
    is_partially_staged: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageStatus: ...
    @typing.overload
    def verify_is_o_k(self) -> _winrt.Boolean: ...

class PackageStatusChangedEventArgs(_winrt.Object):
    package: Package
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageStatusChangedEventArgs: ...

class PackageUninstallingEventArgs(_winrt.Object):
    activity_id: uuid.UUID
    error_code: winsdk.windows.foundation.HResult
    is_complete: _winrt.Boolean
    package: Package
    progress: _winrt.Double
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageUninstallingEventArgs: ...

class PackageUpdateAvailabilityResult(_winrt.Object):
    availability: PackageUpdateAvailability
    extended_error: winsdk.windows.foundation.HResult
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageUpdateAvailabilityResult: ...

class PackageUpdatingEventArgs(_winrt.Object):
    activity_id: uuid.UUID
    error_code: winsdk.windows.foundation.HResult
    is_complete: _winrt.Boolean
    progress: _winrt.Double
    source_package: Package
    target_package: Package
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageUpdatingEventArgs: ...

class StartupTask(_winrt.Object):
    state: StartupTaskState
    task_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> StartupTask: ...
    @typing.overload
    def disable(self) -> None: ...
    @typing.overload
    @staticmethod
    def get_async(task_id: str) -> winsdk.windows.foundation.IAsyncOperation[StartupTask]: ...
    @typing.overload
    @staticmethod
    def get_for_current_package_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[StartupTask]]: ...
    @typing.overload
    def request_enable_async(self) -> winsdk.windows.foundation.IAsyncOperation[StartupTaskState]: ...

class SuspendingDeferral(ISuspendingDeferral, _winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> SuspendingDeferral: ...
    @typing.overload
    def complete(self) -> None: ...

class SuspendingEventArgs(ISuspendingEventArgs, _winrt.Object):
    suspending_operation: SuspendingOperation
    @staticmethod
    def _from(obj: _winrt.Object) -> SuspendingEventArgs: ...

class SuspendingOperation(ISuspendingOperation, _winrt.Object):
    deadline: winsdk.windows.foundation.DateTime
    @staticmethod
    def _from(obj: _winrt.Object) -> SuspendingOperation: ...
    @typing.overload
    def get_deferral(self) -> SuspendingDeferral: ...

class IEnteredBackgroundEventArgs(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> IEnteredBackgroundEventArgs: ...
    @typing.overload
    def get_deferral(self) -> winsdk.windows.foundation.Deferral: ...

class ILeavingBackgroundEventArgs(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> ILeavingBackgroundEventArgs: ...
    @typing.overload
    def get_deferral(self) -> winsdk.windows.foundation.Deferral: ...

class ISuspendingDeferral(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> ISuspendingDeferral: ...
    @typing.overload
    def complete(self) -> None: ...

class ISuspendingEventArgs(_winrt.Object):
    suspending_operation: SuspendingOperation
    @staticmethod
    def _from(obj: _winrt.Object) -> ISuspendingEventArgs: ...

class ISuspendingOperation(_winrt.Object):
    deadline: winsdk.windows.foundation.DateTime
    @staticmethod
    def _from(obj: _winrt.Object) -> ISuspendingOperation: ...
    @typing.overload
    def get_deferral(self) -> SuspendingDeferral: ...

