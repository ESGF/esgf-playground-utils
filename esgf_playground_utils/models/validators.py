"""Validated Types for ESGF data values"""

from pydantic import BeforeValidator
from typing_extensions import Annotated
from utils.cf import get_standard_names


def validate_cf_standard_name(value: str) -> str:
    """Ensure that the `cf_standard_name` value is a CF value name"""

    standard_names = get_standard_names()

    if value in standard_names:
        return value

    raise ValueError(
        "given cf_standard_name is not a valid CF standard name - see https://cfconventions.org/Data/cf-standard-names/86/build/cf-standard-name-table.html "
    )


CFStandardNameStr = Annotated[str, BeforeValidator(validate_cf_standard_name)]
