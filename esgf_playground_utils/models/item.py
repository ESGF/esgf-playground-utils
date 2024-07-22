"""
Models relating to STAC Items for the ESGF-Playground.
"""

from pydantic import AnyUrl
from stac_pydantic.item import Item, ItemProperties


class ESGFItem(Item):
    stac_version: str = "1.0.0"


class ESGFItemProperties(ItemProperties):
    citation_url: AnyUrl
    variable_long_name: str
    variable_units: str
    cf_standard_name: str
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
