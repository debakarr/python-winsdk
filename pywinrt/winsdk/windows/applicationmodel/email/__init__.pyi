# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.applicationmodel.appointments
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
    import winsdk.windows.security.cryptography.certificates
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

class EmailAttachmentDownloadState(enum.IntEnum):
    NOT_DOWNLOADED = 0
    DOWNLOADING = 1
    DOWNLOADED = 2
    FAILED = 3

class EmailBatchStatus(enum.IntEnum):
    SUCCESS = 0
    SERVER_SEARCH_SYNC_MANAGER_ERROR = 1
    SERVER_SEARCH_UNKNOWN_ERROR = 2

class EmailCertificateValidationStatus(enum.IntEnum):
    SUCCESS = 0
    NO_MATCH = 1
    INVALID_USAGE = 2
    INVALID_CERTIFICATE = 3
    REVOKED = 4
    CHAIN_REVOKED = 5
    REVOCATION_SERVER_FAILURE = 6
    EXPIRED = 7
    UNTRUSTED = 8
    SERVER_ERROR = 9
    UNKNOWN_FAILURE = 10

class EmailFlagState(enum.IntEnum):
    UNFLAGGED = 0
    FLAGGED = 1
    COMPLETED = 2
    CLEARED = 3

class EmailImportance(enum.IntEnum):
    NORMAL = 0
    HIGH = 1
    LOW = 2

class EmailMailboxActionKind(enum.IntEnum):
    MARK_MESSAGE_AS_SEEN = 0
    MARK_MESSAGE_READ = 1
    CHANGE_MESSAGE_FLAG_STATE = 2
    MOVE_MESSAGE = 3
    SAVE_DRAFT = 4
    SEND_MESSAGE = 5
    CREATE_RESPONSE_REPLY_MESSAGE = 6
    CREATE_RESPONSE_REPLY_ALL_MESSAGE = 7
    CREATE_RESPONSE_FORWARD_MESSAGE = 8
    MOVE_FOLDER = 9
    MARK_FOLDER_FOR_SYNC_ENABLED = 10

class EmailMailboxAllowedSmimeEncryptionAlgorithmNegotiation(enum.IntEnum):
    NONE = 0
    STRONG_ALGORITHM = 1
    ANY_ALGORITHM = 2

class EmailMailboxAutoReplyMessageResponseKind(enum.IntEnum):
    HTML = 0
    PLAIN_TEXT = 1

class EmailMailboxChangeType(enum.IntEnum):
    MESSAGE_CREATED = 0
    MESSAGE_MODIFIED = 1
    MESSAGE_DELETED = 2
    FOLDER_CREATED = 3
    FOLDER_MODIFIED = 4
    FOLDER_DELETED = 5
    CHANGE_TRACKING_LOST = 6

class EmailMailboxCreateFolderStatus(enum.IntEnum):
    SUCCESS = 0
    NETWORK_ERROR = 1
    PERMISSIONS_ERROR = 2
    SERVER_ERROR = 3
    UNKNOWN_FAILURE = 4
    NAME_COLLISION = 5
    SERVER_REJECTED = 6

class EmailMailboxDeleteFolderStatus(enum.IntEnum):
    SUCCESS = 0
    NETWORK_ERROR = 1
    PERMISSIONS_ERROR = 2
    SERVER_ERROR = 3
    UNKNOWN_FAILURE = 4
    COULD_NOT_DELETE_EVERYTHING = 5

class EmailMailboxEmptyFolderStatus(enum.IntEnum):
    SUCCESS = 0
    NETWORK_ERROR = 1
    PERMISSIONS_ERROR = 2
    SERVER_ERROR = 3
    UNKNOWN_FAILURE = 4
    COULD_NOT_DELETE_EVERYTHING = 5

class EmailMailboxOtherAppReadAccess(enum.IntEnum):
    SYSTEM_ONLY = 0
    FULL = 1
    NONE = 2

class EmailMailboxOtherAppWriteAccess(enum.IntEnum):
    NONE = 0
    LIMITED = 1

class EmailMailboxSmimeEncryptionAlgorithm(enum.IntEnum):
    ANY = 0
    TRIPLE_DES = 1
    DES = 2
    R_C2128_BIT = 3
    R_C264_BIT = 4
    R_C240_BIT = 5

class EmailMailboxSmimeSigningAlgorithm(enum.IntEnum):
    ANY = 0
    SHA1 = 1
    M_D5 = 2

class EmailMailboxSyncStatus(enum.IntEnum):
    IDLE = 0
    SYNCING = 1
    UP_TO_DATE = 2
    AUTHENTICATION_ERROR = 3
    POLICY_ERROR = 4
    UNKNOWN_ERROR = 5
    MANUAL_ACCOUNT_REMOVAL_REQUIRED = 6

class EmailMeetingResponseType(enum.IntEnum):
    ACCEPT = 0
    DECLINE = 1
    TENTATIVE = 2

class EmailMessageBodyKind(enum.IntEnum):
    HTML = 0
    PLAIN_TEXT = 1

class EmailMessageDownloadState(enum.IntEnum):
    PARTIALLY_DOWNLOADED = 0
    DOWNLOADING = 1
    DOWNLOADED = 2
    FAILED = 3

class EmailMessageResponseKind(enum.IntEnum):
    NONE = 0
    REPLY = 1
    REPLY_ALL = 2
    FORWARD = 3

class EmailMessageSmimeKind(enum.IntEnum):
    NONE = 0
    CLEAR_SIGNED = 1
    OPAQUE_SIGNED = 2
    ENCRYPTED = 3

class EmailQueryKind(enum.IntEnum):
    ALL = 0
    IMPORTANT = 1
    FLAGGED = 2
    UNREAD = 3
    READ = 4
    UNSEEN = 5

class EmailQuerySearchFields(enum.IntFlag):
    NONE = 0
    SUBJECT = 0x1
    SENDER = 0x2
    PREVIEW = 0x4
    RECIPIENTS = 0x8
    ALL = 0xffffffff

class EmailQuerySearchScope(enum.IntEnum):
    LOCAL = 0
    SERVER = 1

class EmailQuerySortDirection(enum.IntEnum):
    DESCENDING = 0
    ASCENDING = 1

class EmailQuerySortProperty(enum.IntEnum):
    DATE = 0

class EmailRecipientResolutionStatus(enum.IntEnum):
    SUCCESS = 0
    RECIPIENT_NOT_FOUND = 1
    AMBIGUOUS_RECIPIENT = 2
    NO_CERTIFICATE = 3
    CERTIFICATE_REQUEST_LIMIT_REACHED = 4
    CANNOT_RESOLVE_DISTRIBUTION_LIST = 5
    SERVER_ERROR = 6
    UNKNOWN_FAILURE = 7

class EmailSpecialFolderKind(enum.IntEnum):
    NONE = 0
    ROOT = 1
    INBOX = 2
    OUTBOX = 3
    DRAFTS = 4
    DELETED_ITEMS = 5
    SENT = 6

class EmailStoreAccessType(enum.IntEnum):
    APP_MAILBOXES_READ_WRITE = 0
    ALL_MAILBOXES_LIMITED_READ_WRITE = 1

class EmailAttachment(_winrt.Object):
    file_name: str
    data: winsdk.windows.storage.streams.IRandomAccessStreamReference
    mime_type: str
    is_inline: _winrt.Boolean
    estimated_download_size_in_bytes: _winrt.UInt64
    download_state: EmailAttachmentDownloadState
    content_location: str
    content_id: str
    id: str
    is_from_base_message: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailAttachment: ...
    @typing.overload
    def __init__(self, file_name: str, data: winsdk.windows.storage.streams.IRandomAccessStreamReference, mime_type: str) -> None: ...
    @typing.overload
    def __init__(self, file_name: str, data: winsdk.windows.storage.streams.IRandomAccessStreamReference) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...

class EmailConversation(_winrt.Object):
    flag_state: EmailFlagState
    has_attachment: _winrt.Boolean
    id: str
    importance: EmailImportance
    last_email_response_kind: EmailMessageResponseKind
    latest_sender: EmailRecipient
    mailbox_id: str
    message_count: _winrt.UInt32
    most_recent_message_id: str
    most_recent_message_time: winsdk.windows.foundation.DateTime
    preview: str
    subject: str
    unread_message_count: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailConversation: ...
    @typing.overload
    def find_messages_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[EmailMessage]]: ...
    @typing.overload
    def find_messages_async(self, count: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[EmailMessage]]: ...

class EmailConversationBatch(_winrt.Object):
    conversations: winsdk.windows.foundation.collections.IVectorView[EmailConversation]
    status: EmailBatchStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailConversationBatch: ...

class EmailConversationReader(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailConversationReader: ...
    @typing.overload
    def read_batch_async(self) -> winsdk.windows.foundation.IAsyncOperation[EmailConversationBatch]: ...

class EmailFolder(_winrt.Object):
    remote_id: str
    last_successful_sync_time: winsdk.windows.foundation.DateTime
    is_sync_enabled: _winrt.Boolean
    display_name: str
    id: str
    kind: EmailSpecialFolderKind
    mailbox_id: str
    parent_folder_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailFolder: ...
    @typing.overload
    def create_folder_async(self, name: str) -> winsdk.windows.foundation.IAsyncOperation[EmailFolder]: ...
    @typing.overload
    def delete_async(self) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def find_child_folders_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[EmailFolder]]: ...
    @typing.overload
    def get_conversation_reader(self) -> EmailConversationReader: ...
    @typing.overload
    def get_conversation_reader(self, options: EmailQueryOptions) -> EmailConversationReader: ...
    @typing.overload
    def get_message_async(self, id: str) -> winsdk.windows.foundation.IAsyncOperation[EmailMessage]: ...
    @typing.overload
    def get_message_counts_async(self) -> winsdk.windows.foundation.IAsyncOperation[EmailItemCounts]: ...
    @typing.overload
    def get_message_reader(self) -> EmailMessageReader: ...
    @typing.overload
    def get_message_reader(self, options: EmailQueryOptions) -> EmailMessageReader: ...
    @typing.overload
    def save_message_async(self, message: EmailMessage) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def try_move_async(self, new_parent_folder: EmailFolder) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_move_async(self, new_parent_folder: EmailFolder, new_folder_name: str) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_save_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...

class EmailIrmInfo(_winrt.Object):
    can_remove_irm_on_response: _winrt.Boolean
    can_print_data: _winrt.Boolean
    can_modify_recipients_on_response: _winrt.Boolean
    can_forward: _winrt.Boolean
    can_extract_data: _winrt.Boolean
    can_reply: _winrt.Boolean
    can_edit: _winrt.Boolean
    template: EmailIrmTemplate
    is_programatic_access_allowed: _winrt.Boolean
    is_irm_originator: _winrt.Boolean
    expiration_date: winsdk.windows.foundation.DateTime
    can_reply_all: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailIrmInfo: ...
    @typing.overload
    def __init__(self, expiration: winsdk.windows.foundation.DateTime, irm_template: EmailIrmTemplate) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...

class EmailIrmTemplate(_winrt.Object):
    name: str
    id: str
    description: str
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailIrmTemplate: ...
    @typing.overload
    def __init__(self, id: str, name: str, description: str) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...

class EmailItemCounts(_winrt.Object):
    flagged: _winrt.UInt32
    important: _winrt.UInt32
    total: _winrt.UInt32
    unread: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailItemCounts: ...

class EmailMailbox(_winrt.Object):
    other_app_write_access: EmailMailboxOtherAppWriteAccess
    mail_address: str
    other_app_read_access: EmailMailboxOtherAppReadAccess
    display_name: str
    id: str
    is_data_encrypted_under_lock: _winrt.Boolean
    is_owned_by_current_app: _winrt.Boolean
    mail_address_aliases: winsdk.windows.foundation.collections.IVector[str]
    capabilities: EmailMailboxCapabilities
    change_tracker: EmailMailboxChangeTracker
    policies: EmailMailboxPolicies
    source_display_name: str
    sync_manager: EmailMailboxSyncManager
    user_data_account_id: str
    linked_mailbox_id: str
    network_account_id: str
    network_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailMailbox: ...
    @typing.overload
    def change_message_flag_state_async(self, message_id: str, flag_state: EmailFlagState) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def create_response_message_async(self, message_id: str, response_type: EmailMessageResponseKind, subject: str, response_header_type: EmailMessageBodyKind, response_header: str) -> winsdk.windows.foundation.IAsyncOperation[EmailMessage]: ...
    @typing.overload
    def delete_async(self) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def delete_message_async(self, message_id: str) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def download_attachment_async(self, attachment_id: str) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def download_message_async(self, message_id: str) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def get_change_tracker(self, identity: str) -> EmailMailboxChangeTracker: ...
    @typing.overload
    def get_conversation_async(self, id: str) -> winsdk.windows.foundation.IAsyncOperation[EmailConversation]: ...
    @typing.overload
    def get_conversation_reader(self) -> EmailConversationReader: ...
    @typing.overload
    def get_conversation_reader(self, options: EmailQueryOptions) -> EmailConversationReader: ...
    @typing.overload
    def get_folder_async(self, id: str) -> winsdk.windows.foundation.IAsyncOperation[EmailFolder]: ...
    @typing.overload
    def get_message_async(self, id: str) -> winsdk.windows.foundation.IAsyncOperation[EmailMessage]: ...
    @typing.overload
    def get_message_reader(self) -> EmailMessageReader: ...
    @typing.overload
    def get_message_reader(self, options: EmailQueryOptions) -> EmailMessageReader: ...
    @typing.overload
    def get_special_folder_async(self, folder_type: EmailSpecialFolderKind) -> winsdk.windows.foundation.IAsyncOperation[EmailFolder]: ...
    @typing.overload
    def mark_folder_as_seen_async(self, folder_id: str) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def mark_folder_sync_enabled_async(self, folder_id: str, is_sync_enabled: _winrt.Boolean) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def mark_message_as_seen_async(self, message_id: str) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def mark_message_read_async(self, message_id: str, is_read: _winrt.Boolean) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def register_sync_manager_async(self) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def resolve_recipients_async(self, recipients: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[EmailRecipientResolutionResult]]: ...
    @typing.overload
    def save_async(self) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def save_draft_async(self, message: EmailMessage) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def send_message_async(self, message: EmailMessage) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def send_message_async(self, message: EmailMessage, smart_send: _winrt.Boolean) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def try_create_folder_async(self, parent_folder_id: str, name: str) -> winsdk.windows.foundation.IAsyncOperation[EmailMailboxCreateFolderResult]: ...
    @typing.overload
    def try_delete_folder_async(self, folder_id: str) -> winsdk.windows.foundation.IAsyncOperation[EmailMailboxDeleteFolderStatus]: ...
    @typing.overload
    def try_empty_folder_async(self, folder_id: str) -> winsdk.windows.foundation.IAsyncOperation[EmailMailboxEmptyFolderStatus]: ...
    @typing.overload
    def try_forward_meeting_async(self, meeting: EmailMessage, recipients: typing.Iterable[EmailRecipient], subject: str, forward_header_type: EmailMessageBodyKind, forward_header: str, comment: str) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_get_auto_reply_settings_async(self, requested_format: EmailMailboxAutoReplyMessageResponseKind) -> winsdk.windows.foundation.IAsyncOperation[EmailMailboxAutoReplySettings]: ...
    @typing.overload
    def try_move_folder_async(self, folder_id: str, new_parent_folder_id: str) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_move_folder_async(self, folder_id: str, new_parent_folder_id: str, new_folder_name: str) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_move_message_async(self, message_id: str, new_parent_folder_id: str) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_propose_new_time_for_meeting_async(self, meeting: EmailMessage, new_start_time: winsdk.windows.foundation.DateTime, new_duration: winsdk.windows.foundation.TimeSpan, subject: str, comment: str) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_set_auto_reply_settings_async(self, auto_reply_settings: EmailMailboxAutoReplySettings) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_update_meeting_response_async(self, meeting: EmailMessage, response: EmailMeetingResponseType, subject: str, comment: str, send_update: _winrt.Boolean) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def validate_certificates_async(self, certificates: typing.Iterable[winsdk.windows.security.cryptography.certificates.Certificate]) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[EmailCertificateValidationStatus]]: ...
    @typing.overload
    def add_mailbox_changed(self, p_handler: winsdk.windows.foundation.TypedEventHandler[EmailMailbox, EmailMailboxChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_mailbox_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class EmailMailboxAction(_winrt.Object):
    change_number: _winrt.UInt64
    kind: EmailMailboxActionKind
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailMailboxAction: ...

class EmailMailboxAutoReply(_winrt.Object):
    response: str
    is_enabled: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailMailboxAutoReply: ...

class EmailMailboxAutoReplySettings(_winrt.Object):
    start_time: typing.Optional[winsdk.windows.foundation.DateTime]
    response_kind: EmailMailboxAutoReplyMessageResponseKind
    is_enabled: _winrt.Boolean
    end_time: typing.Optional[winsdk.windows.foundation.DateTime]
    internal_reply: EmailMailboxAutoReply
    known_external_reply: EmailMailboxAutoReply
    unknown_external_reply: EmailMailboxAutoReply
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailMailboxAutoReplySettings: ...
    @typing.overload
    def __init__(self) -> None: ...

class EmailMailboxCapabilities(_winrt.Object):
    can_smart_send: _winrt.Boolean
    can_update_meeting_responses: _winrt.Boolean
    can_server_search_mailbox: _winrt.Boolean
    can_server_search_folders: _winrt.Boolean
    can_forward_meetings: _winrt.Boolean
    can_propose_new_time_for_meetings: _winrt.Boolean
    can_get_and_set_internal_auto_replies: _winrt.Boolean
    can_get_and_set_external_auto_replies: _winrt.Boolean
    can_validate_certificates: _winrt.Boolean
    can_resolve_recipients: _winrt.Boolean
    can_move_folder: _winrt.Boolean
    can_empty_folder: _winrt.Boolean
    can_delete_folder: _winrt.Boolean
    can_create_folder: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailMailboxCapabilities: ...

class EmailMailboxChange(_winrt.Object):
    change_type: EmailMailboxChangeType
    folder: EmailFolder
    mailbox_actions: winsdk.windows.foundation.collections.IVector[EmailMailboxAction]
    message: EmailMessage
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailMailboxChange: ...

class EmailMailboxChangeReader(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailMailboxChangeReader: ...
    @typing.overload
    def accept_changes(self) -> None: ...
    @typing.overload
    def accept_changes_through(self, last_change_to_acknowledge: EmailMailboxChange) -> None: ...
    @typing.overload
    def read_batch_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[EmailMailboxChange]]: ...

class EmailMailboxChangeTracker(_winrt.Object):
    is_tracking: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailMailboxChangeTracker: ...
    @typing.overload
    def enable(self) -> None: ...
    @typing.overload
    def get_change_reader(self) -> EmailMailboxChangeReader: ...
    @typing.overload
    def reset(self) -> None: ...

class EmailMailboxChangedDeferral(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailMailboxChangedDeferral: ...
    @typing.overload
    def complete(self) -> None: ...

class EmailMailboxChangedEventArgs(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailMailboxChangedEventArgs: ...
    @typing.overload
    def get_deferral(self) -> EmailMailboxChangedDeferral: ...

class EmailMailboxCreateFolderResult(_winrt.Object):
    folder: EmailFolder
    status: EmailMailboxCreateFolderStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailMailboxCreateFolderResult: ...

class EmailMailboxPolicies(_winrt.Object):
    required_smime_signing_algorithm: typing.Optional[EmailMailboxSmimeSigningAlgorithm]
    required_smime_encryption_algorithm: typing.Optional[EmailMailboxSmimeEncryptionAlgorithm]
    allowed_smime_encryption_algorithm_negotiation: EmailMailboxAllowedSmimeEncryptionAlgorithmNegotiation
    allow_smime_soft_certificates: _winrt.Boolean
    must_sign_smime_messages: _winrt.Boolean
    must_encrypt_smime_messages: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailMailboxPolicies: ...

class EmailMailboxSyncManager(_winrt.Object):
    status: EmailMailboxSyncStatus
    last_successful_sync_time: winsdk.windows.foundation.DateTime
    last_attempted_sync_time: winsdk.windows.foundation.DateTime
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailMailboxSyncManager: ...
    @typing.overload
    def sync_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def add_sync_status_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[EmailMailboxSyncManager, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_sync_status_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class EmailManager(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailManager: ...
    @typing.overload
    @staticmethod
    def get_for_user(user: winsdk.windows.system.User) -> EmailManagerForUser: ...
    @typing.overload
    @staticmethod
    def request_store_async(access_type: EmailStoreAccessType) -> winsdk.windows.foundation.IAsyncOperation[EmailStore]: ...
    @typing.overload
    @staticmethod
    def show_compose_new_email_async(message: EmailMessage) -> winsdk.windows.foundation.IAsyncAction: ...

class EmailManagerForUser(_winrt.Object):
    user: winsdk.windows.system.User
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailManagerForUser: ...
    @typing.overload
    def request_store_async(self, access_type: EmailStoreAccessType) -> winsdk.windows.foundation.IAsyncOperation[EmailStore]: ...
    @typing.overload
    def show_compose_new_email_async(self, message: EmailMessage) -> winsdk.windows.foundation.IAsyncAction: ...

class EmailMeetingInfo(_winrt.Object):
    location: str
    is_response_requested: _winrt.Boolean
    is_all_day: _winrt.Boolean
    allow_new_time_proposal: _winrt.Boolean
    duration: winsdk.windows.foundation.TimeSpan
    appointment_roaming_id: str
    appointment_original_start_time: typing.Optional[winsdk.windows.foundation.DateTime]
    proposed_duration: typing.Optional[winsdk.windows.foundation.TimeSpan]
    remote_change_number: _winrt.UInt64
    start_time: winsdk.windows.foundation.DateTime
    recurrence_start_time: typing.Optional[winsdk.windows.foundation.DateTime]
    recurrence: winsdk.windows.applicationmodel.appointments.AppointmentRecurrence
    proposed_start_time: typing.Optional[winsdk.windows.foundation.DateTime]
    is_reported_out_of_date_by_server: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailMeetingInfo: ...
    @typing.overload
    def __init__(self) -> None: ...

class EmailMessage(_winrt.Object):
    subject: str
    body: str
    bcc: winsdk.windows.foundation.collections.IVector[EmailRecipient]
    c_c: winsdk.windows.foundation.collections.IVector[EmailRecipient]
    attachments: winsdk.windows.foundation.collections.IVector[EmailAttachment]
    to: winsdk.windows.foundation.collections.IVector[EmailRecipient]
    allow_internet_images: _winrt.Boolean
    flag_state: EmailFlagState
    estimated_download_size_in_bytes: _winrt.UInt32
    download_state: EmailMessageDownloadState
    importance: EmailImportance
    irm_info: EmailIrmInfo
    original_code_page: _winrt.Int32
    sent_time: typing.Optional[winsdk.windows.foundation.DateTime]
    sender: EmailRecipient
    remote_id: str
    preview: str
    message_class: str
    meeting_info: EmailMeetingInfo
    last_response_kind: EmailMessageResponseKind
    is_seen: _winrt.Boolean
    is_read: _winrt.Boolean
    is_server_search_message: _winrt.Boolean
    is_smart_sendable: _winrt.Boolean
    mailbox_id: str
    change_number: _winrt.UInt64
    conversation_id: str
    normalized_subject: str
    folder_id: str
    has_partial_bodies: _winrt.Boolean
    id: str
    in_response_to_message_id: str
    is_draft_message: _winrt.Boolean
    smime_kind: EmailMessageSmimeKind
    smime_data: winsdk.windows.storage.streams.IRandomAccessStreamReference
    sent_representing: EmailRecipient
    reply_to: winsdk.windows.foundation.collections.IVector[EmailRecipient]
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailMessage: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def get_body_stream(self, type: EmailMessageBodyKind) -> winsdk.windows.storage.streams.IRandomAccessStreamReference: ...
    @typing.overload
    def set_body_stream(self, type: EmailMessageBodyKind, stream: winsdk.windows.storage.streams.IRandomAccessStreamReference) -> None: ...

class EmailMessageBatch(_winrt.Object):
    messages: winsdk.windows.foundation.collections.IVectorView[EmailMessage]
    status: EmailBatchStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailMessageBatch: ...

class EmailMessageReader(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailMessageReader: ...
    @typing.overload
    def read_batch_async(self) -> winsdk.windows.foundation.IAsyncOperation[EmailMessageBatch]: ...

class EmailQueryOptions(_winrt.Object):
    sort_property: EmailQuerySortProperty
    sort_direction: EmailQuerySortDirection
    kind: EmailQueryKind
    folder_ids: winsdk.windows.foundation.collections.IVector[str]
    text_search: EmailQueryTextSearch
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailQueryOptions: ...
    @typing.overload
    def __init__(self, text: str) -> None: ...
    @typing.overload
    def __init__(self, text: str, fields: EmailQuerySearchFields) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...

class EmailQueryTextSearch(_winrt.Object):
    text: str
    search_scope: EmailQuerySearchScope
    fields: EmailQuerySearchFields
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailQueryTextSearch: ...

class EmailRecipient(_winrt.Object):
    name: str
    address: str
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailRecipient: ...
    @typing.overload
    def __init__(self, address: str) -> None: ...
    @typing.overload
    def __init__(self, address: str, name: str) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...

class EmailRecipientResolutionResult(_winrt.Object):
    status: EmailRecipientResolutionStatus
    public_keys: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.security.cryptography.certificates.Certificate]
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailRecipientResolutionResult: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def set_public_keys(self, value: typing.Iterable[winsdk.windows.security.cryptography.certificates.Certificate]) -> None: ...

class EmailStore(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailStore: ...
    @typing.overload
    def create_mailbox_async(self, account_name: str, account_address: str) -> winsdk.windows.foundation.IAsyncOperation[EmailMailbox]: ...
    @typing.overload
    def create_mailbox_async(self, account_name: str, account_address: str, user_data_account_id: str) -> winsdk.windows.foundation.IAsyncOperation[EmailMailbox]: ...
    @typing.overload
    def find_mailboxes_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[EmailMailbox]]: ...
    @typing.overload
    def get_conversation_async(self, id: str) -> winsdk.windows.foundation.IAsyncOperation[EmailConversation]: ...
    @typing.overload
    def get_conversation_reader(self) -> EmailConversationReader: ...
    @typing.overload
    def get_conversation_reader(self, options: EmailQueryOptions) -> EmailConversationReader: ...
    @typing.overload
    def get_folder_async(self, id: str) -> winsdk.windows.foundation.IAsyncOperation[EmailFolder]: ...
    @typing.overload
    def get_mailbox_async(self, id: str) -> winsdk.windows.foundation.IAsyncOperation[EmailMailbox]: ...
    @typing.overload
    def get_message_async(self, id: str) -> winsdk.windows.foundation.IAsyncOperation[EmailMessage]: ...
    @typing.overload
    def get_message_reader(self) -> EmailMessageReader: ...
    @typing.overload
    def get_message_reader(self, options: EmailQueryOptions) -> EmailMessageReader: ...

class EmailStoreNotificationTriggerDetails(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> EmailStoreNotificationTriggerDetails: ...

