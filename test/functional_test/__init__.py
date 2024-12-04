"""
Test the polymorphic interpretation of a KafkaEvent
"""

import unittest

from pydantic import ValidationError

from esgf_playground_utils.models.kafka import (
    CreatePayload,
    KafkaEvent,
    RevokePayload,
    UpdatePayload,
)


class TestKafkaEvent(unittest.TestCase):
    """Test that events with different methods are correctly resovled"""

    def test_create_payload_valid(self) -> None:
        """Test that a creation payload can be interpreted from a valid payload"""

        payload = """
{
  "data": {
    "type": "STAC",
    "version": "1.0.0",
    "payload": {
      "collection_id": "cmip6",
      "method": "POST",
      "item": {
        "bbox": [
          -71.04548482586011,
          -40.70724540817599,
          70.95154804339046,
          18.041543625553206
        ],
        "type": "Feature",
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                -71.04548482586011,
                -40.70724540817599
              ],
              [
                70.95154804339046,
                -40.70724540817599
              ],
              [
                70.95154804339046,
                18.041543625553206
              ],
              [
                -71.04548482586011,
                18.041543625553206
              ],
              [
                -71.04548482586011,
                -40.70724540817599
              ]
            ]
          ]
        },
        "properties": {
          "title": "CMIP6.CMIP.IPSL.CMCC-ESM2.ssp585.r1i1000p1f2.3hr.vas.gr.v20220101",
          "description": null,
          "datetime": "2720-11-02T18:18:05.322660Z",
          "created": "1980-07-05T06:25:41.304211Z",
          "updated": "2020-06-02T12:29:58.311307Z",
          "start_datetime": null,
          "end_datetime": null,
          "license": "GqmvOMeWcuNhryVbwniL",
          "providers": [
            {
              "name": "21",
              "description": null,
              "roles": [
                "JiKhIJraixVQrDjSOdrf"
              ],
              "url": "EtVBRiTpUeXBoGBlLRsx"
            }
          ],
          "platform": null,
          "instruments": null,
          "constellation": "yaTflgiUXEwqXFUgjmer",
          "mission": null,
          "gsd": null,
          "citation_url": "http://cera-www.dkrz.de/WDCC/meta/CMIP6/CMIP6.CMIP.IPSL.CMCC-ESM2.ssp585.r1i1000p1f2.3hr.vas.gr.v20220101.json",
          "variable_long_name": "Precipitation",
          "variable_units": "m s-1",
          "cf_standard_name": "air_temperature",
          "activity_id": "CMIP",
          "data_specs_version": "01.00.21",
          "experiment_title": "Simulation of recent past (1850 to 2014). Impose changing conditions (consistent with observations). Should be initialised from a point early enough in the pre-industrial control run to ensure that the end of all the perturbed runs branching from the end of this historical run end before the end of the control. Only one ensemble member is requested but modelling groups are strongly encouraged to submit at least three ensemble members of their CMIP historical simulation.",
          "frequency": "3hrPt",
          "further_info_url": "https://furtherinfo.es-doc.org/CMIP6.CMIP.IPSL.CMCC-ESM2.ssp585.r1i1000p1f2.3hr.vas.gr.v20220101",
          "grid": "gs1x1",
          "grid_label": "gr",
          "institution_id": "IPSL",
          "mip_era": "CMIP6",
          "source_id": "CMCC-ESM2",
          "source_type": "AOGCM BGC AER CHEM",
          "experiment_id": "ssp585",
          "sub_experiment_id": "none",
          "nominal_resolution": "10 km",
          "table_id": "3hr",
          "variable_id": "vas",
          "variant_label": "r1i1000p1f2",
          "instance_id": "CMIP6.CMIP.IPSL.CMCC-ESM2.ssp585.r1i1000p1f2.3hr.vas.gr.v20220101"
        },
        "id": "CMIP6.CMIP.IPSL.CMCC-ESM2.ssp585.r1i1000p1f2.3hr.vas.gr.v20220101",
        "stac_version": "1.0.0",
        "assets": {
          "cudrjPnkDBusxfZNPXib": {
            "href": "252",
            "type": "uLBhENjsjwedAAYcAlZp",
            "title": "UwlqbQPrzhfkvbIDxYSI",
            "description": "CMwrUkEnGNshrhDiwsHk",
            "roles": null
          }
        },
        "links": [
          {
            "href": "http://ceda.stac.ac.uk/collections/cmip6/items/CMIP6.CMIP.IPSL.CMCC-ESM2.ssp585.r1i1000p1f2.3hr.vas.gr.v20220101",
            "rel": "self",
            "type": "application/geo+json"
          },
          {
            "href": "http://ceda.stac.ac.uk/collections/cmip6",
            "rel": "parent",
            "type": "application/json"
          },
          {
            "href": "http://ceda.stac.ac.uk/collections/cmip6",
            "rel": "collection",
            "type": "application/json"
          },
          {
            "href": "http://ceda.stac.ac.uk",
            "rel": "root",
            "type": "application/json"
          }
        ],
        "stac_extensions": [],
        "collection": "cmip6"
      }
    }
  },
  "metadata": {
    "event_id": "3a8a2536-323b-4259-a218-6002a3491d25",
    "request_id": "dee8c54c-e815-4863-87fb-7b606efd2501",
    "auth": {
        "auth_policy_id": "ESGF-Publish-00012",   # We need registered auth policies?
        "client_id": "CEDA-transaction-client",
        "requester_data": {
          "auth_service": "auth.globus.org",
          "sub": "b16b12b6-d274-11e5-8e41-5fea585a1aa2",
          "user_id": "7fd9ab20-f6c5-4902-a7ac-b40bc4d8ad7b",
          "identity_provider": "0dcf5063-bffd-40f7-b403-24f97e32fa47",
          "identity_provider_display_name": "University of Chicago"
        }
    },
    "publisher": {
        "package": "some_python_package",
        "version": "0.3.0"
    },
    "time": "2024-07-04T14:17:35Z",
    "schema_version": "1.0.0"
  }
}
"""

        kafka_event = KafkaEvent.model_validate_json(payload)

        self.assertIsInstance(kafka_event.data.payload, CreatePayload)

    def test_create_payload_invalid(self) -> None:
        """Test that a creation payload with the wrong verb is not validated"""

        payload = """
{
  "data": {
    "type": "STAC",
    "version": "1.0.0",
    "payload": {
      "collection_id": "cmip6",
      "method": "DELETE",
      "item": {
        "bbox": [
          -71.04548482586011,
          -40.70724540817599,
          70.95154804339046,
          18.041543625553206
        ],
        "type": "Feature",
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                -71.04548482586011,
                -40.70724540817599
              ],
              [
                70.95154804339046,
                -40.70724540817599
              ],
              [
                70.95154804339046,
                18.041543625553206
              ],
              [
                -71.04548482586011,
                18.041543625553206
              ],
              [
                -71.04548482586011,
                -40.70724540817599
              ]
            ]
          ]
        },
        "properties": {
          "title": "CMIP6.CMIP.IPSL.CMCC-ESM2.ssp585.r1i1000p1f2.3hr.vas.gr.v20220101",
          "description": null,
          "datetime": "2720-11-02T18:18:05.322660Z",
          "created": "1980-07-05T06:25:41.304211Z",
          "updated": "2020-06-02T12:29:58.311307Z",
          "start_datetime": null,
          "end_datetime": null,
          "license": "GqmvOMeWcuNhryVbwniL",
          "providers": [
            {
              "name": "21",
              "description": null,
              "roles": [
                "JiKhIJraixVQrDjSOdrf"
              ],
              "url": "EtVBRiTpUeXBoGBlLRsx"
            }
          ],
          "platform": null,
          "instruments": null,
          "constellation": "yaTflgiUXEwqXFUgjmer",
          "mission": null,
          "gsd": null,
          "citation_url": "http://cera-www.dkrz.de/WDCC/meta/CMIP6/CMIP6.CMIP.IPSL.CMCC-ESM2.ssp585.r1i1000p1f2.3hr.vas.gr.v20220101.json",
          "variable_long_name": "Precipitation",
          "variable_units": "m s-1",
          "cf_standard_name": "air_temperature",
          "activity_id": "CMIP",
          "data_specs_version": "01.00.21",
          "experiment_title": "Simulation of recent past (1850 to 2014). Impose changing conditions (consistent with observations). Should be initialised from a point early enough in the pre-industrial control run to ensure that the end of all the perturbed runs branching from the end of this historical run end before the end of the control. Only one ensemble member is requested but modelling groups are strongly encouraged to submit at least three ensemble members of their CMIP historical simulation.",
          "frequency": "3hrPt",
          "further_info_url": "https://furtherinfo.es-doc.org/CMIP6.CMIP.IPSL.CMCC-ESM2.ssp585.r1i1000p1f2.3hr.vas.gr.v20220101",
          "grid": "gs1x1",
          "grid_label": "gr",
          "institution_id": "IPSL",
          "mip_era": "CMIP6",
          "source_id": "CMCC-ESM2",
          "source_type": "AOGCM BGC AER CHEM",
          "experiment_id": "ssp585",
          "sub_experiment_id": "none",
          "nominal_resolution": "10 km",
          "table_id": "3hr",
          "variable_id": "vas",
          "variant_label": "r1i1000p1f2",
          "instance_id": "CMIP6.CMIP.IPSL.CMCC-ESM2.ssp585.r1i1000p1f2.3hr.vas.gr.v20220101"
        },
        "id": "CMIP6.CMIP.IPSL.CMCC-ESM2.ssp585.r1i1000p1f2.3hr.vas.gr.v20220101",
        "stac_version": "1.0.0",
        "assets": {
          "cudrjPnkDBusxfZNPXib": {
            "href": "252",
            "type": "uLBhENjsjwedAAYcAlZp",
            "title": "UwlqbQPrzhfkvbIDxYSI",
            "description": "CMwrUkEnGNshrhDiwsHk",
            "roles": null
          }
        },
        "links": [
          {
            "href": "http://ceda.stac.ac.uk/collections/cmip6/items/CMIP6.CMIP.IPSL.CMCC-ESM2.ssp585.r1i1000p1f2.3hr.vas.gr.v20220101",
            "rel": "self",
            "type": "application/geo+json"
          },
          {
            "href": "http://ceda.stac.ac.uk/collections/cmip6",
            "rel": "parent",
            "type": "application/json"
          },
          {
            "href": "http://ceda.stac.ac.uk/collections/cmip6",
            "rel": "collection",
            "type": "application/json"
          },
          {
            "href": "http://ceda.stac.ac.uk",
            "rel": "root",
            "type": "application/json"
          }
        ],
        "stac_extensions": [],
        "collection": "cmip6"
      }
    }
  },
  "metadata": {
    "event_id": "3a8a2536-323b-4259-a218-6002a3491d25",
    "request_id": "dee8c54c-e815-4863-87fb-7b606efd2501",
    "auth": {
        "auth_policy_id": "ESGF-Publish-00012",   # We need registered auth policies?
        "client_id": "CEDA-transaction-client",
        "requester_data": {
          "auth_service": "auth.globus.org",
          "sub": "b16b12b6-d274-11e5-8e41-5fea585a1aa2",
          "user_id": "7fd9ab20-f6c5-4902-a7ac-b40bc4d8ad7b",
          "identity_provider": "0dcf5063-bffd-40f7-b403-24f97e32fa47",
          "identity_provider_display_name": "University of Chicago"
        }
    },
    "publisher": {
        "package": "some_python_package",
        "version": "0.3.0"
    },
    "time": "2024-07-04T14:17:35Z",
    "schema_version": "1.0.0"
  }
}
"""

        with self.assertRaises(ValidationError):
            KafkaEvent.model_validate_json(payload)

    def test_revoke_payload_soft(self) -> None:
        payload = """
{
          "data": {
            "type": "STAC",
            "version": "1.0.0",
            "payload": {
              "collection_id": "cmip6",
              "method": "PATCH",
              "item_id": "an_item" 
            }
          },
          "metadata": {
            "event_id": "3a8a2536-323b-4259-a218-6002a3491d25",
            "request_id": "dee8c54c-e815-4863-87fb-7b606efd2501",
            "auth": {
                "auth_policy_id": "ESGF-Publish-00012",   # We need registered auth policies?
                "client_id": "CEDA-transaction-client",
                "requester_data": {
                  "auth_service": "auth.globus.org",
                  "sub": "b16b12b6-d274-11e5-8e41-5fea585a1aa2",
                  "user_id": "7fd9ab20-f6c5-4902-a7ac-b40bc4d8ad7b",
                  "identity_provider": "0dcf5063-bffd-40f7-b403-24f97e32fa47",
                  "identity_provider_display_name": "University of Chicago"
                }
            },
            "publisher": {
                "package": "some_python_package",
                "version": "0.3.0"
            },
            "time": "2024-07-04T14:17:35Z",
            "schema_version": "1.0.0"
          }
        }
"""

        kafka_event = KafkaEvent.model_validate_json(payload)

        self.assertIsInstance(kafka_event.data.payload, RevokePayload)

    def test_revoke_payload_hard(self) -> None:
        payload = """
{
  "data": {
    "type": "STAC",
    "version": "1.0.0",
    "payload": {
      "collection_id": "cmip6",
      "method": "DELETE",
      "item_id": "an_item" 
    }
  },
  "metadata": {
    "event_id": "3a8a2536-323b-4259-a218-6002a3491d25",
    "request_id": "dee8c54c-e815-4863-87fb-7b606efd2501",
    "auth": {
        "auth_policy_id": "ESGF-Publish-00012",   # We need registered auth policies?
        "client_id": "CEDA-transaction-client",
        "requester_data": {
          "auth_service": "auth.globus.org",
          "sub": "b16b12b6-d274-11e5-8e41-5fea585a1aa2",
          "user_id": "7fd9ab20-f6c5-4902-a7ac-b40bc4d8ad7b",
          "identity_provider": "0dcf5063-bffd-40f7-b403-24f97e32fa47",
          "identity_provider_display_name": "University of Chicago"
        }
    },
    "publisher": {
        "package": "some_python_package",
        "version": "0.3.0"
    },
    "time": "2024-07-04T14:17:35Z",
    "schema_version": "1.0.0"
  }
}
"""

        kafka_event = KafkaEvent.model_validate_json(payload)

        self.assertIsInstance(kafka_event.data.payload, RevokePayload)

    def test_update_payload_full(self) -> None:
        """Test that a creation payload can be interpreted from a valid payload"""

        payload = """
{
  "data": {
    "type": "STAC",
    "version": "1.0.0",
    "payload": {
      "collection_id": "cmip6",
      "method": "PUT",
      "item_id": "an_item",
      "item": {
        "bbox": [
          -71.04548482586011,
          -40.70724540817599,
          70.95154804339046,
          18.041543625553206
        ],
        "type": "Feature",
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                -71.04548482586011,
                -40.70724540817599
              ],
              [
                70.95154804339046,
                -40.70724540817599
              ],
              [
                70.95154804339046,
                18.041543625553206
              ],
              [
                -71.04548482586011,
                18.041543625553206
              ],
              [
                -71.04548482586011,
                -40.70724540817599
              ]
            ]
          ]
        },
        "properties": {
          "title": "CMIP6.CMIP.IPSL.CMCC-ESM2.ssp585.r1i1000p1f2.3hr.vas.gr.v20220101",
          "description": null,
          "datetime": "2720-11-02T18:18:05.322660Z",
          "created": "1980-07-05T06:25:41.304211Z",
          "updated": "2020-06-02T12:29:58.311307Z",
          "start_datetime": null,
          "end_datetime": null,
          "license": "GqmvOMeWcuNhryVbwniL",
          "providers": [
            {
              "name": "21",
              "description": null,
              "roles": [
                "JiKhIJraixVQrDjSOdrf"
              ],
              "url": "EtVBRiTpUeXBoGBlLRsx"
            }
          ],
          "platform": null,
          "instruments": null,
          "constellation": "yaTflgiUXEwqXFUgjmer",
          "mission": null,
          "gsd": null,
          "citation_url": "http://cera-www.dkrz.de/WDCC/meta/CMIP6/CMIP6.CMIP.IPSL.CMCC-ESM2.ssp585.r1i1000p1f2.3hr.vas.gr.v20220101.json",
          "variable_long_name": "Precipitation",
          "variable_units": "m s-1",
          "cf_standard_name": "air_temperature",
          "activity_id": "CMIP",
          "data_specs_version": "01.00.21",
          "experiment_title": "Simulation of recent past (1850 to 2014). Impose changing conditions (consistent with observations). Should be initialised from a point early enough in the pre-industrial control run to ensure that the end of all the perturbed runs branching from the end of this historical run end before the end of the control. Only one ensemble member is requested but modelling groups are strongly encouraged to submit at least three ensemble members of their CMIP historical simulation.",
          "frequency": "3hrPt",
          "further_info_url": "https://furtherinfo.es-doc.org/CMIP6.CMIP.IPSL.CMCC-ESM2.ssp585.r1i1000p1f2.3hr.vas.gr.v20220101",
          "grid": "gs1x1",
          "grid_label": "gr",
          "institution_id": "IPSL",
          "mip_era": "CMIP6",
          "source_id": "CMCC-ESM2",
          "source_type": "AOGCM BGC AER CHEM",
          "experiment_id": "ssp585",
          "sub_experiment_id": "none",
          "nominal_resolution": "10 km",
          "table_id": "3hr",
          "variable_id": "vas",
          "variant_label": "r1i1000p1f2",
          "instance_id": "CMIP6.CMIP.IPSL.CMCC-ESM2.ssp585.r1i1000p1f2.3hr.vas.gr.v20220101"
        },
        "id": "CMIP6.CMIP.IPSL.CMCC-ESM2.ssp585.r1i1000p1f2.3hr.vas.gr.v20220101",
        "stac_version": "1.0.0",
        "assets": {
          "cudrjPnkDBusxfZNPXib": {
            "href": "252",
            "type": "uLBhENjsjwedAAYcAlZp",
            "title": "UwlqbQPrzhfkvbIDxYSI",
            "description": "CMwrUkEnGNshrhDiwsHk",
            "roles": null
          }
        },
        "links": [
          {
            "href": "http://ceda.stac.ac.uk/collections/cmip6/items/CMIP6.CMIP.IPSL.CMCC-ESM2.ssp585.r1i1000p1f2.3hr.vas.gr.v20220101",
            "rel": "self",
            "type": "application/geo+json"
          },
          {
            "href": "http://ceda.stac.ac.uk/collections/cmip6",
            "rel": "parent",
            "type": "application/json"
          },
          {
            "href": "http://ceda.stac.ac.uk/collections/cmip6",
            "rel": "collection",
            "type": "application/json"
          },
          {
            "href": "http://ceda.stac.ac.uk",
            "rel": "root",
            "type": "application/json"
          }
        ],
        "stac_extensions": [],
        "collection": "cmip6"
      }
    }
  },
  "metadata": {
    "event_id": "3a8a2536-323b-4259-a218-6002a3491d25",
    "request_id": "dee8c54c-e815-4863-87fb-7b606efd2501",
    "auth": {
        "auth_policy_id": "ESGF-Publish-00012",   # We need registered auth policies?
        "client_id": "CEDA-transaction-client",
        "requester_data": {
          "auth_service": "auth.globus.org",
          "sub": "b16b12b6-d274-11e5-8e41-5fea585a1aa2",
          "user_id": "7fd9ab20-f6c5-4902-a7ac-b40bc4d8ad7b",
          "identity_provider": "0dcf5063-bffd-40f7-b403-24f97e32fa47",
          "identity_provider_display_name": "University of Chicago"
        }
    },
    "publisher": {
        "package": "some_python_package",
        "version": "0.3.0"
    },
    "time": "2024-07-04T14:17:35Z",
    "schema_version": "1.0.0"
  }
}
        """

        kafka_event = KafkaEvent.model_validate_json(payload)

        self.assertIsInstance(kafka_event.data.payload, UpdatePayload)
