"""
Models relating to Kakfa payloads for the ESGF-Playground.
"""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, Literal, Union

from pydantic import BaseModel
from stac_pydantic.item import Item


class _Payload(BaseModel):
    """
    Base model for payloads in a Kafka message, provides the required ``collection_id`` attribute.

    .. warning::

      This model should not be used directly.

    """

    collection_id: str


class CreatePayload(_Payload):
    """
    Model describing a ``CREATE`` payload. This must be sent as a ``POST`` request.
    """

    method: Literal["POST"]
    item: Item


class RevokePayload(_Payload):
    """
    Model describing a ``REVOKE`` payload. This must be sent as a ``PATCH`` or ``DELETE`` request.

    .. note::

      It is intended that the ``PATCH`` request is interpreted as a "soft" delete, simply updating the item to
      signify that it is revoked.

      The ``DELETE`` request will operate as a "hard" delete strictly removing the item from the STAC index.

    .. danger::

      The behaviour of either of these actions is not yet fully defined.
    """

    method: Literal["PATCH", "DELETE"]
    item_id: str


class PartialUpdatePayload(_Payload):
    """
    Model describing a ``PARTIAL_UPDATE`` payload. This must be sent as a ``PATCH`` request.
    """

    method: Literal["PATCH"]
    item: Dict[str, Any]
    item_id: str


class UpdatePayload(_Payload):
    """
    Model describing a ``UPDATE`` payload. This must be sent as a ``PATCH`` or ``PUT`` request.
    """

    method: Literal["PUT", "PATCH"]
    item: Item
    item_id: str


class Data(BaseModel):
    """
    Model describing the ``DATA`` component of a Kafka message. This contains the payload itself.

    .. note::

      Whilst the ``type`` and ``version`` attributes are available, it is not expected that these will change for
      a significant length of time.
    """

    type: Literal["STAC"]
    version: Literal["1.0.0"]
    payload: Union[CreatePayload, RevokePayload, UpdatePayload, PartialUpdatePayload]


class Auth(BaseModel):
    """
    Model describing the ``AUTH`` component of a Kafka message.

    .. note::

      This is not an authorisation token or other verified identity. It is the simply an indication of the institute
      providing the message.
    """

    client_id: str
    server: str


class AuthData(BaseModel):
    """
    Model describing ``Auth`` component of a Kafka message in more detail.
    """

    auth_policy_id: str
    client_id: str
    requester_data: Dict[str, str]


class Publisher(BaseModel):
    """
    Model describing the ``PUBLISHER`` component of a Kafka message. This is the name and version of the software used
    to publish the Kafka message.
    """

    package: str
    version: str


class Metadata(BaseModel):
    """
    Multiple metadata attributes required for ESGF but not part of the STAC payload.
    """

    auth: Union[Auth, AuthData]
    publisher: Publisher
    time: datetime
    schema_version: str


class KafkaEvent(BaseModel):
    """
    The full content of a Kafka message, containing both the STAC payload, the request description and the ESGF
    mandated metadata.
    """

    metadata: Metadata
    data: Data


class ErrorType(str, Enum):
    """
    Enum describing the source of the error that occurred.
    """

    payload = "payload"
    stac_server = "stac_server"
    kafka = "kafka"
    unknown = "unknown"


class Error(BaseModel):
    """
    Error event published to the Kafka error queue.
    """

    original_payload: str
    node: str
    traceback: str
    error_type: ErrorType
