"""
Models relating to STAC Items for the ESGF-Playground.
"""

from typing import List, Optional

from pydantic import ConfigDict, HttpUrl
from stac_pydantic.item import Item, ItemProperties


class ESGFItem(Item):
    stac_version: str = "1.0.0"


class ESGFItemProperties(ItemProperties):
    access: Optional[List[str]] = []
    activity_id: List[str]
    cf_standard_name: str
    citation_url: Optional[HttpUrl] = None
    data_spec_version: Optional[str] = None
    experiment_id: str
    experiment_title: str
    frequency: str
    further_info_url: HttpUrl
    grid: str
    grid_label: str
    institution_id: str
    mip_era: str
    model_cohort: Optional[str] = None
    nominal_resolution: str
    pid: Optional[str] = None
    product: Optional[str] = None
    project: Optional[str] = None
    realm: Optional[List[str]] = []
    retracted: Optional[bool] = False
    source_id: str
    source_type: List[str]
    sub_experiment_id: str
    table_id: str
    title: str
    variable: Optional[str] = None
    variable_id: str
    variable_long_name: str
    variable_units: Optional[str] = None
    variant_label: str
    version: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())


class CMIP6Item(Item):
    properties: ESGFItemProperties
