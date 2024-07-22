"""
Models relating to Kakfa payloads for the ESGF-Playground.
"""

from datetime import datetime
from enum import Enum
from typing import Literal, Union

from pydantic import BaseModel
from stac_pydantic.item import Item


class _Payload(BaseModel):
    collection_id: str


class CreatePayload(_Payload):
    method: Literal["POST"]
    item: Item


class RevokePayload(_Payload):
    method: Literal["PATCH", "DELETE"]
    item_id: str


class UpdatePayload(_Payload):
    method: Literal["PUT", "PATCH"]
    item: Item


class Data(BaseModel):
    type: Literal["STAC"]
    version: Literal["1.0.0"]
    payload: Union[CreatePayload, RevokePayload, UpdatePayload]


class Auth(BaseModel):
    client_id: str
    server: str


class Publisher(BaseModel):
    package: str
    version: str


class Metadata(BaseModel):
    auth: Auth
    publisher: Publisher
    time: datetime
    schema_version: str


class KafkaEvent(BaseModel):
    metadata: Metadata
    data: Data


class ErrorType(str, Enum):
    payload = "payload"
    stac_server = "stac_server"
    kafka = "kafka"
    unknown = "unknown"


class Error(BaseModel):
    original_payload: str
    node: str
    traceback: str
    error_type: ErrorType
