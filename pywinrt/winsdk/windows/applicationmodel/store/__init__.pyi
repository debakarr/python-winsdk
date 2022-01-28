# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

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

class FulfillmentResult(enum.IntEnum):
    SUCCEEDED = 0
    NOTHING_TO_FULFILL = 1
    PURCHASE_PENDING = 2
    PURCHASE_REVERTED = 3
    SERVER_ERROR = 4

class ProductPurchaseStatus(enum.IntEnum):
    SUCCEEDED = 0
    ALREADY_PURCHASED = 1
    NOT_FULFILLED = 2
    NOT_PURCHASED = 3

class ProductType(enum.IntEnum):
    UNKNOWN = 0
    DURABLE = 1
    CONSUMABLE = 2

class CurrentApp(_winrt.Object):
    ...
    app_id: uuid.UUID
    license_information: LicenseInformation
    link_uri: winsdk.windows.foundation.Uri
    def get_app_purchase_campaign_id_async() -> winsdk.windows.foundation.IAsyncOperation[str]:
        ...
    def get_app_receipt_async() -> winsdk.windows.foundation.IAsyncOperation[str]:
        ...
    def get_customer_collections_id_async(service_ticket: str, publisher_user_id: str) -> winsdk.windows.foundation.IAsyncOperation[str]:
        ...
    def get_customer_purchase_id_async(service_ticket: str, publisher_user_id: str) -> winsdk.windows.foundation.IAsyncOperation[str]:
        ...
    def get_product_receipt_async(product_id: str) -> winsdk.windows.foundation.IAsyncOperation[str]:
        ...
    def get_unfulfilled_consumables_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[UnfulfilledConsumable]]:
        ...
    def load_listing_information_async() -> winsdk.windows.foundation.IAsyncOperation[ListingInformation]:
        ...
    def load_listing_information_by_keywords_async(keywords: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperation[ListingInformation]:
        ...
    def load_listing_information_by_product_ids_async(product_ids: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperation[ListingInformation]:
        ...
    def report_consumable_fulfillment_async(product_id: str, transaction_id: uuid.UUID) -> winsdk.windows.foundation.IAsyncOperation[FulfillmentResult]:
        ...
    def report_product_fulfillment(product_id: str) -> None:
        ...
    def request_app_purchase_async(include_receipt: _winrt.Boolean) -> winsdk.windows.foundation.IAsyncOperation[str]:
        ...
    def request_product_purchase_async(product_id: str) -> winsdk.windows.foundation.IAsyncOperation[PurchaseResults]:
        ...
    def request_product_purchase_async(product_id: str, include_receipt: _winrt.Boolean) -> winsdk.windows.foundation.IAsyncOperation[str]:
        ...
    def request_product_purchase_async(product_id: str, offer_id: str, display_properties: ProductPurchaseDisplayProperties) -> winsdk.windows.foundation.IAsyncOperation[PurchaseResults]:
        ...

class CurrentAppSimulator(_winrt.Object):
    ...
    app_id: uuid.UUID
    license_information: LicenseInformation
    link_uri: winsdk.windows.foundation.Uri
    def get_app_purchase_campaign_id_async() -> winsdk.windows.foundation.IAsyncOperation[str]:
        ...
    def get_app_receipt_async() -> winsdk.windows.foundation.IAsyncOperation[str]:
        ...
    def get_product_receipt_async(product_id: str) -> winsdk.windows.foundation.IAsyncOperation[str]:
        ...
    def get_unfulfilled_consumables_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[UnfulfilledConsumable]]:
        ...
    def load_listing_information_async() -> winsdk.windows.foundation.IAsyncOperation[ListingInformation]:
        ...
    def load_listing_information_by_keywords_async(keywords: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperation[ListingInformation]:
        ...
    def load_listing_information_by_product_ids_async(product_ids: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperation[ListingInformation]:
        ...
    def reload_simulator_async(simulator_settings_file: winsdk.windows.storage.StorageFile) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def report_consumable_fulfillment_async(product_id: str, transaction_id: uuid.UUID) -> winsdk.windows.foundation.IAsyncOperation[FulfillmentResult]:
        ...
    def request_app_purchase_async(include_receipt: _winrt.Boolean) -> winsdk.windows.foundation.IAsyncOperation[str]:
        ...
    def request_product_purchase_async(product_id: str) -> winsdk.windows.foundation.IAsyncOperation[PurchaseResults]:
        ...
    def request_product_purchase_async(product_id: str, include_receipt: _winrt.Boolean) -> winsdk.windows.foundation.IAsyncOperation[str]:
        ...
    def request_product_purchase_async(product_id: str, offer_id: str, display_properties: ProductPurchaseDisplayProperties) -> winsdk.windows.foundation.IAsyncOperation[PurchaseResults]:
        ...

class LicenseInformation(_winrt.Object):
    ...
    expiration_date: winsdk.windows.foundation.DateTime
    is_active: _winrt.Boolean
    is_trial: _winrt.Boolean
    product_licenses: winsdk.windows.foundation.collections.IMapView[str, ProductLicense]
    def add_license_changed(handler: LicenseChangedEventHandler) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_license_changed(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class ListingInformation(_winrt.Object):
    ...
    age_rating: _winrt.UInt32
    current_market: str
    description: str
    formatted_price: str
    name: str
    product_listings: winsdk.windows.foundation.collections.IMapView[str, ProductListing]
    currency_code: str
    formatted_base_price: str
    is_on_sale: _winrt.Boolean
    sale_end_date: winsdk.windows.foundation.DateTime

class ProductLicense(_winrt.Object):
    ...
    expiration_date: winsdk.windows.foundation.DateTime
    is_active: _winrt.Boolean
    product_id: str
    is_consumable: _winrt.Boolean

class ProductListing(_winrt.Object):
    ...
    formatted_price: str
    name: str
    product_id: str
    formatted_base_price: str
    is_on_sale: _winrt.Boolean
    sale_end_date: winsdk.windows.foundation.DateTime
    currency_code: str
    description: str
    image_uri: winsdk.windows.foundation.Uri
    keywords: winsdk.windows.foundation.collections.IIterable[str]
    tag: str
    product_type: ProductType

class ProductPurchaseDisplayProperties(_winrt.Object):
    ...
    name: str
    image: winsdk.windows.foundation.Uri
    description: str
    def __init__(self, name: str) -> None:
        ...
    def __init__(self, ) -> None:
        ...

class PurchaseResults(_winrt.Object):
    ...
    offer_id: str
    receipt_xml: str
    status: ProductPurchaseStatus
    transaction_id: uuid.UUID

class UnfulfilledConsumable(_winrt.Object):
    ...
    offer_id: str
    product_id: str
    transaction_id: uuid.UUID

LicenseChangedEventHandler = typing.Callable[[], None]

