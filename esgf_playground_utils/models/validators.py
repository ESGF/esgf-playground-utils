"""Validated Types for ESGF data values"""

import httpx
from pydantic import AnyUrl, BeforeValidator, ValidationInfo
from typing_extensions import Annotated

from esgf_playground_utils.utils.cf import get_standard_names


def validate_cf_standard_name(value: str) -> str:
    """Ensure that the `cf_standard_name` value is a CF value name"""

    standard_names = get_standard_names()

    if value in standard_names:
        return value

    raise ValueError(
        "given cf_standard_name is not a valid CF standard name - see https://cfconventions.org/Data/cf-standard-names/86/build/cf-standard-name-table.html "
    )


CFStandardNameStr = Annotated[str, BeforeValidator(validate_cf_standard_name)]


def validate_any_url(value: AnyUrl, info: ValidationInfo) -> AnyUrl:
    """Ensure that the `AnyUrl` value is a valid URL"""

    context = info.context or {}
    check = context.get("check_url")
    if check:
        try:
            response = httpx.head(value, timeout=5)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404 or e.response.status_code >= 500:
                raise ValueError(f"URL {value} does not exist")
        except httpx.RequestError:
            raise ValueError(f"URL {value} is not reachable")

    return value
