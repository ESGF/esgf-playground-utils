"""
Models relating to Authorisation for the ESGF Next Gen Core Architecture.
"""

from typing import Literal

from pydantic import BaseModel


class Node(BaseModel):
    """
    Model describing Node auth info of a ESGF publisher.
    """

    id: str
    role: Literal[
        "CREATE",
        "UPDATE",
        "DELETE",
        "REPLICATE",
        "REVOKE",
    ]


class Project(BaseModel):
    """
    Model describing Project auth info of a ESGF publisher.
    """

    id: str
    role: Literal[
        "CREATE",
        "UPDATE",
        "DELETE",
        "REPLICATE",
        "REVOKE",
    ]


class ESGFAuth(BaseModel):
    """
    Model describing Authentication information of a ESGF publisher.
    """

    sub: str
    iss: str
    nodes: list[Node]
    projects: list[Project]
