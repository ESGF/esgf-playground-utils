"""
Configuration module for the ESGF-Playground.
"""

from __future__ import annotations

from re import compile
from typing import List, Optional, Pattern

from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Container for configuration of the ESGF-Playground.

    By default, this configuration is valid for running the consumer on localhost, with a Kafka broker on localhost,
    provided it is given a `consumer_group` value. It will subscribe the consumer to all topics.
    """

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    bootstrap_servers: List[str] = ["localhost"]
    consumer_group: Optional[str] = None
    kafka_topics: Pattern[str] = compile(r".*\..*\..*")
    error_topic: str = "esgf_consumer_error"
    stac_server: HttpUrl = HttpUrl("http://localhost:9010")
