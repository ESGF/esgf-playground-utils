"""
Models relating to STAC Items for the ESGF-Playground.
"""

import re

from pydantic import AnyUrl, ValidationInfo, model_validator
from stac_pydantic.item import Item, ItemProperties
from typing_extensions import Self

from esgf_playground_utils.models.validators import CFStandardNameStr, validate_any_url


class ESGFItem(Item):
    stac_version: str = "1.0.0"


class ESGFItemProperties(ItemProperties):
    citation_url: AnyUrl
    variable_long_name: str
    variable_units: str
    cf_standard_name: CFStandardNameStr
    activity_id: str
    data_specs_version: str
    experiment_title: str
    frequency: str
    further_info_url: AnyUrl
    grid: str
    grid_label: str
    institution_id: str
    mip_era: str
    source_id: str
    source_type: str
    experiment_id: str
    sub_experiment_id: str
    nominal_resolution: str
    table_id: str
    variable_id: str
    variant_label: str
    instance_id: str

    @model_validator(mode="after")
    def check_instance_id(self: Self) -> Self:
        """
        The instance_id value is a constructed value from other fields, validate that this is the case and
        raise a validation error if it is not.
        """

        predictable_instance_id = predictable_instance_id = (
            f"{self.mip_era}.{self.activity_id}.{self.institution_id}.{self.source_id}."
            f"{self.experiment_id}.{self.variant_label}.{self.table_id}.{self.variable_id}."
            f"{self.grid_label}"
        )

        expected_instance_id_pattern = rf"{predictable_instance_id}\..*"
        if re.match(expected_instance_id_pattern, self.instance_id):
            return self

        raise ValueError(
            f"The instance_id did not match other values provided. "
            f"It should have been in the form '{predictable_instance_id}.<some_version>' "
            f"however is was '{self.instance_id}'."
        )

    @model_validator(mode="after")
    def check_citation_url(self: Self, info: ValidationInfo) -> Self:
        """
        Validate `citation_url` by constructing it and optionally checking its existence.
        """
        expected_url = (
            f"http://cera-www.dkrz.de/WDCC/meta/{self.mip_era}/{self.instance_id}.json"
        )

        if str(self.citation_url) != expected_url:
            raise ValueError(
                f"citation_url should be '{expected_url}', but got '{self.citation_url}'"
            )

        context = info.context or {}
        if context.get("check_url", False):
            validate_any_url(str(self.citation_url), info)

        return self

    @model_validator(mode="after")
    def check_further_info_url(self: Self, info: ValidationInfo) -> Self:
        """
        Validate `further_info_url` by constructing it and optionally checking its existence.
        """

        expected_url = f"https://furtherinfo.es-doc.org/{self.instance_id}"

        if str(self.further_info_url) == expected_url:
            raise ValueError(
                f"further_info_url should be '{expected_url}', but got '{self.further_info_url}'"
            )

        context = info.context or {}
        if context.get("check_url", False):
            validate_any_url(str(self.further_info_url), info)

        return self
