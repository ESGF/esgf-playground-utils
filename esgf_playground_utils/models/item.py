"""
Models relating to STAC Items for the ESGF-Playground.
"""

from pydantic import AnyUrl, ConfigDict, HttpUrl
from stac_pydantic.item import Item, ItemProperties
from typing import List, Optional

import datetime as datetimevalidate


class ESGFItem(Item):
    stac_version: str = "1.0.0"


class ESGFItemProperties(ItemProperties):
    access: List[str]
    activity_id: List[str]
    cf_standard_name: str
    citation_url: HttpUrl
    data_spec_version: Optional[str] = None
    experiment_id: str
    experiment_title: str
    frequency: str
    further_info_url: HttpUrl
    grid: str
    grid_label: str
    institution_id: str
    mip_era: str
    model_cohort: str
    nominal_resolution: str
    pid: str
    product: str
    project: str
    realm: List[str]
    retracted: Optional[str] = None
    source_id: str
    source_type: List[str]
    sub_experiment_id: str
    table_id: str
    title: str
    variable: str
    variable_id: str
    variable_long_name: str
    variable_units: str
    variant_label: str
    version: str

    model_config = ConfigDict(
        protected_namespaces=()
    )


class CMIP6Item(Item):
    properties: ESGFItemProperties
