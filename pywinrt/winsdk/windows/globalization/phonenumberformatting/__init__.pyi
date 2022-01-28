# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

class PhoneNumberFormat(enum.IntEnum):
    E164 = 0
    INTERNATIONAL = 1
    NATIONAL = 2
    RFC3966 = 3

class PhoneNumberMatchResult(enum.IntEnum):
    NO_MATCH = 0
    SHORT_NATIONAL_SIGNIFICANT_NUMBER_MATCH = 1
    NATIONAL_SIGNIFICANT_NUMBER_MATCH = 2
    EXACT_MATCH = 3

class PhoneNumberParseResult(enum.IntEnum):
    VALID = 0
    NOT_A_NUMBER = 1
    INVALID_COUNTRY_CODE = 2
    TOO_SHORT = 3
    TOO_LONG = 4

class PredictedPhoneNumberKind(enum.IntEnum):
    FIXED_LINE = 0
    MOBILE = 1
    FIXED_LINE_OR_MOBILE = 2
    TOLL_FREE = 3
    PREMIUM_RATE = 4
    SHARED_COST = 5
    VOIP = 6
    PERSONAL_NUMBER = 7
    PAGER = 8
    UNIVERSAL_ACCOUNT_NUMBER = 9
    VOICEMAIL = 10
    UNKNOWN = 11

class PhoneNumberFormatter(_winrt.Object):
    ...
    def __init__(self, ) -> None:
        ...
    def format(number: PhoneNumberInfo) -> str:
        ...
    def format(number: PhoneNumberInfo, number_format: PhoneNumberFormat) -> str:
        ...
    def format_partial_string(number: str) -> str:
        ...
    def format_string(number: str) -> str:
        ...
    def format_string_with_left_to_right_markers(number: str) -> str:
        ...
    def get_country_code_for_region(region_code: str) -> _winrt.Int32:
        ...
    def get_national_direct_dialing_prefix_for_region(region_code: str, strip_non_digit: _winrt.Boolean) -> str:
        ...
    def try_create(region_code: str) -> PhoneNumberFormatter:
        ...
    def wrap_with_left_to_right_markers(number: str) -> str:
        ...

class PhoneNumberInfo(winsdk.windows.foundation.IStringable, _winrt.Object):
    ...
    country_code: _winrt.Int32
    phone_number: str
    def __init__(self, number: str) -> None:
        ...
    def check_number_match(other_number: PhoneNumberInfo) -> PhoneNumberMatchResult:
        ...
    def get_geographic_region_code() -> str:
        ...
    def get_length_of_geographical_area_code() -> _winrt.Int32:
        ...
    def get_length_of_national_destination_code() -> _winrt.Int32:
        ...
    def get_national_significant_number() -> str:
        ...
    def predict_number_kind() -> PredictedPhoneNumberKind:
        ...
    def to_string() -> str:
        ...
    def try_parse(input: str) -> typing.Tuple[PhoneNumberParseResult, PhoneNumberInfo]:
        ...
    def try_parse(input: str, region_code: str) -> typing.Tuple[PhoneNumberParseResult, PhoneNumberInfo]:
        ...

