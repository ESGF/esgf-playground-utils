"""
Test various configurations of Items and their validation
"""

import unittest

from pydantic import ValidationError

from esgf_playground_utils.models.item import ESGFItemProperties


class TestESGFItemProperties(unittest.TestCase):
    """
    Test the validation of ESGFItemProperties
    """

    def test_with_valid_properties(self) -> None:
        """Should pass through"""

        stac_data = """{
            "title": "CMIP6.ScenarioMIP.CNRM-CERFACS.MPI-ESM1-2-HR.ssp126.r1i1000p1f2.3hr.pr.gr1.v20220101",
            "description": "fNpIMLPmUbhwjphcEytY",
            "datetime": null,
            "created": "1983-08-13T01:52:15.625356Z",
            "updated": null,
            "start_datetime": "2124-12-25T22:33:34.041698Z",
            "end_datetime": "2354-01-19T08:47:57.750624Z",
            "license": "DWmtkdGTcGXCnPxZjmld",
            "providers": [
              {
                "name": "5e",
                "description": "MxPawZErtBWWNtGlHwnI",
                "roles": null,
                "url": null
              }
            ],
            "platform": null,
            "instruments": [
              "HFyzkQHsVXuLftQMhhhu"
            ],
            "constellation": "UtpERJghEMBNgnhZtmjA",
            "mission": "eKsGjBvJdlSkcrBOuuHn",
            "gsd": null,
            "citation_url": "http://cera-www.dkrz.de/WDCC/meta/CMIP6/CMIP6.ScenarioMIP.CNRM-CERFACS.MPI-ESM1-2-HR.ssp126.r1i1000p1f2.3hr.pr.gr1.v20220101.json",
            "variable_long_name": "Snowfall Flux",
            "variable_units": "kg m-2 s-1",
            "cf_standard_name": "surface_upwelling_shortwave_flux_in_air",
            "activity_id": "ScenarioMIP",
            "data_specs_version": "01.00.27",
            "experiment_title": "update of RCP8.5 based on SSP5",
            "frequency": "3hrPt",
            "further_info_url": "https://furtherinfo.es-doc.org/CMIP6.ScenarioMIP.CNRM-CERFACS.MPI-ESM1-2-HR.ssp126.r1i1000p1f2.3hr.pr.gr1.v20220101",
            "grid": "T255L91",
            "grid_label": "gr1",
            "institution_id": "CNRM-CERFACS",
            "mip_era": "CMIP6",
            "source_id": "MPI-ESM1-2-HR",
            "source_type": "AOGCM BGC",
            "experiment_id": "ssp126",
            "sub_experiment_id": "none",
            "nominal_resolution": "250 km",
            "table_id": "3hr",
            "variable_id": "pr",
            "variant_label": "r1i1000p1f2",
            "instance_id": "CMIP6.ScenarioMIP.CNRM-CERFACS.MPI-ESM1-2-HR.ssp126.r1i1000p1f2.3hr.pr.gr1.v20220101"
          }
        """

        result = ESGFItemProperties.model_validate_json(stac_data)
        self.assertIsInstance(result, ESGFItemProperties)

    def test_with_invalid_cf_standard_name(self) -> None:
        """Should raise a ValueError"""

        stac_data = """{
    "title": "CMIP6.ScenarioMIP.CNRM-CERFACS.MPI-ESM1-2-HR.ssp126.r1i1000p1f2.3hr.pr.gr1.v20220101",
    "description": "fNpIMLPmUbhwjphcEytY",
    "datetime": null,
    "created": "1983-08-13T01:52:15.625356Z",
    "updated": null,
    "start_datetime": "2124-12-25T22:33:34.041698Z",
    "end_datetime": "2354-01-19T08:47:57.750624Z",
    "license": "DWmtkdGTcGXCnPxZjmld",
    "providers": [
      {
        "name": "5e",
        "description": "MxPawZErtBWWNtGlHwnI",
        "roles": null,
        "url": null
      }
    ],
    "platform": null,
    "instruments": [
      "HFyzkQHsVXuLftQMhhhu"
    ],
    "constellation": "UtpERJghEMBNgnhZtmjA",
    "mission": "eKsGjBvJdlSkcrBOuuHn",
    "gsd": null,
    "citation_url": "http://cera-www.dkrz.de/WDCC/meta/CMIP6/CMIP6.ScenarioMIP.CNRM-CERFACS.MPI-ESM1-2-HR.ssp126.r1i1000p1f2.3hr.pr.gr1.v20220101.json",
    "variable_long_name": "Snowfall Flux",
    "variable_units": "kg m-2 s-1",
    "cf_standard_name": "count_of_badgers_per_set",
    "activity_id": "ScenarioMIP",
    "data_specs_version": "01.00.27",
    "experiment_title": "update of RCP8.5 based on SSP5",
    "frequency": "3hrPt",
    "further_info_url": "https://furtherinfo.es-doc.org/CMIP6.ScenarioMIP.CNRM-CERFACS.MPI-ESM1-2-HR.ssp126.r1i1000p1f2.3hr.pr.gr1.v20220101",
    "grid": "T255L91",
    "grid_label": "gr1",
    "institution_id": "CNRM-CERFACS",
    "mip_era": "CMIP6",
    "source_id": "MPI-ESM1-2-HR",
    "source_type": "AOGCM BGC",
    "experiment_id": "ssp126",
    "sub_experiment_id": "none",
    "nominal_resolution": "250 km",
    "table_id": "3hr",
    "variable_id": "pr",
    "variant_label": "r1i1000p1f2",
    "instance_id": "CMIP6.ScenarioMIP.CNRM-CERFACS.MPI-ESM1-2-HR.ssp126.r1i1000p1f2.3hr.pr.gr1.v20220101"
  }
"""

        self.assertRaises(
            ValidationError, ESGFItemProperties.model_validate_json, stac_data
        )
