# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.applicationmodel.appointments
import winsdk.windows.foundation
import winsdk.windows.foundation.collections

Self = typing.TypeVar('Self')

class AppointmentCalendarCancelMeetingRequest(_winrt.Object):
    appointment_calendar_local_id: str
    appointment_local_id: str
    appointment_original_start_time: typing.Optional[typing.Optional[winsdk.windows.foundation.DateTime]]
    comment: str
    notify_invitees: _winrt.Boolean
    subject: str
    @staticmethod
    def _from(obj: _winrt.Object) -> AppointmentCalendarCancelMeetingRequest: ...
    def report_completed_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def report_failed_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...

class AppointmentCalendarCancelMeetingRequestEventArgs(_winrt.Object):
    request: typing.Optional[AppointmentCalendarCancelMeetingRequest]
    @staticmethod
    def _from(obj: _winrt.Object) -> AppointmentCalendarCancelMeetingRequestEventArgs: ...
    def get_deferral(self) -> typing.Optional[winsdk.windows.foundation.Deferral]: ...

class AppointmentCalendarCreateOrUpdateAppointmentRequest(_winrt.Object):
    appointment: typing.Optional[winsdk.windows.applicationmodel.appointments.Appointment]
    appointment_calendar_local_id: str
    changed_properties: typing.Optional[winsdk.windows.foundation.collections.IVectorView[str]]
    notify_invitees: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> AppointmentCalendarCreateOrUpdateAppointmentRequest: ...
    def report_completed_async(self, created_or_updated_appointment: typing.Optional[winsdk.windows.applicationmodel.appointments.Appointment]) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def report_failed_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...

class AppointmentCalendarCreateOrUpdateAppointmentRequestEventArgs(_winrt.Object):
    request: typing.Optional[AppointmentCalendarCreateOrUpdateAppointmentRequest]
    @staticmethod
    def _from(obj: _winrt.Object) -> AppointmentCalendarCreateOrUpdateAppointmentRequestEventArgs: ...
    def get_deferral(self) -> typing.Optional[winsdk.windows.foundation.Deferral]: ...

class AppointmentCalendarForwardMeetingRequest(_winrt.Object):
    appointment_calendar_local_id: str
    appointment_local_id: str
    appointment_original_start_time: typing.Optional[typing.Optional[winsdk.windows.foundation.DateTime]]
    comment: str
    forward_header: str
    invitees: typing.Optional[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.applicationmodel.appointments.AppointmentInvitee]]
    subject: str
    @staticmethod
    def _from(obj: _winrt.Object) -> AppointmentCalendarForwardMeetingRequest: ...
    def report_completed_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def report_failed_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...

class AppointmentCalendarForwardMeetingRequestEventArgs(_winrt.Object):
    request: typing.Optional[AppointmentCalendarForwardMeetingRequest]
    @staticmethod
    def _from(obj: _winrt.Object) -> AppointmentCalendarForwardMeetingRequestEventArgs: ...
    def get_deferral(self) -> typing.Optional[winsdk.windows.foundation.Deferral]: ...

class AppointmentCalendarProposeNewTimeForMeetingRequest(_winrt.Object):
    appointment_calendar_local_id: str
    appointment_local_id: str
    appointment_original_start_time: typing.Optional[typing.Optional[winsdk.windows.foundation.DateTime]]
    comment: str
    new_duration: winsdk.windows.foundation.TimeSpan
    new_start_time: winsdk.windows.foundation.DateTime
    subject: str
    @staticmethod
    def _from(obj: _winrt.Object) -> AppointmentCalendarProposeNewTimeForMeetingRequest: ...
    def report_completed_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def report_failed_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...

class AppointmentCalendarProposeNewTimeForMeetingRequestEventArgs(_winrt.Object):
    request: typing.Optional[AppointmentCalendarProposeNewTimeForMeetingRequest]
    @staticmethod
    def _from(obj: _winrt.Object) -> AppointmentCalendarProposeNewTimeForMeetingRequestEventArgs: ...
    def get_deferral(self) -> typing.Optional[winsdk.windows.foundation.Deferral]: ...

class AppointmentCalendarSyncManagerSyncRequest(_winrt.Object):
    appointment_calendar_local_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> AppointmentCalendarSyncManagerSyncRequest: ...
    def report_completed_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def report_failed_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...

class AppointmentCalendarSyncManagerSyncRequestEventArgs(_winrt.Object):
    request: typing.Optional[AppointmentCalendarSyncManagerSyncRequest]
    @staticmethod
    def _from(obj: _winrt.Object) -> AppointmentCalendarSyncManagerSyncRequestEventArgs: ...
    def get_deferral(self) -> typing.Optional[winsdk.windows.foundation.Deferral]: ...

class AppointmentCalendarUpdateMeetingResponseRequest(_winrt.Object):
    appointment_calendar_local_id: str
    appointment_local_id: str
    appointment_original_start_time: typing.Optional[typing.Optional[winsdk.windows.foundation.DateTime]]
    comment: str
    response: winsdk.windows.applicationmodel.appointments.AppointmentParticipantResponse
    send_update: _winrt.Boolean
    subject: str
    @staticmethod
    def _from(obj: _winrt.Object) -> AppointmentCalendarUpdateMeetingResponseRequest: ...
    def report_completed_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def report_failed_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...

class AppointmentCalendarUpdateMeetingResponseRequestEventArgs(_winrt.Object):
    request: typing.Optional[AppointmentCalendarUpdateMeetingResponseRequest]
    @staticmethod
    def _from(obj: _winrt.Object) -> AppointmentCalendarUpdateMeetingResponseRequestEventArgs: ...
    def get_deferral(self) -> typing.Optional[winsdk.windows.foundation.Deferral]: ...

class AppointmentDataProviderConnection(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> AppointmentDataProviderConnection: ...
    def start(self) -> None: ...
    def add_cancel_meeting_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[AppointmentDataProviderConnection, AppointmentCalendarCancelMeetingRequestEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_cancel_meeting_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_create_or_update_appointment_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[AppointmentDataProviderConnection, AppointmentCalendarCreateOrUpdateAppointmentRequestEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_create_or_update_appointment_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_forward_meeting_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[AppointmentDataProviderConnection, AppointmentCalendarForwardMeetingRequestEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_forward_meeting_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_propose_new_time_for_meeting_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[AppointmentDataProviderConnection, AppointmentCalendarProposeNewTimeForMeetingRequestEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_propose_new_time_for_meeting_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_sync_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[AppointmentDataProviderConnection, AppointmentCalendarSyncManagerSyncRequestEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_sync_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_update_meeting_response_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[AppointmentDataProviderConnection, AppointmentCalendarUpdateMeetingResponseRequestEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_update_meeting_response_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class AppointmentDataProviderTriggerDetails(_winrt.Object):
    connection: typing.Optional[AppointmentDataProviderConnection]
    @staticmethod
    def _from(obj: _winrt.Object) -> AppointmentDataProviderTriggerDetails: ...

