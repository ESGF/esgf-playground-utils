"""
Test the functionality of the :py:mod:`models.item` module.

.. note:

  These tests call wrapped methods which quality control tools may not recognise as callable. Some quality
  measures are suppressed for this test case.

"""

from unittest import TestCase
from unittest.mock import Mock

from esgf_playground_utils.models.item import ESGFItemProperties


class TestESGFItemPropertiesCheckInstanceId(TestCase):
    """
    Test the functionality of the :py:ref:`models.item.ESGFItemProperties.check_instance_id` method.
    """

    def test_with_valid_input(self) -> None:
        """Should validate the instance_id value"""

        mock_instance = Mock(spec=ESGFItemProperties)
        mock_instance.mip_era = "a"
        mock_instance.activity_id = "b"
        mock_instance.institution_id = "c"
        mock_instance.source_id = "d"
        mock_instance.experiment_id = "e"
        mock_instance.variant_label = "f"
        mock_instance.table_id = "g"
        mock_instance.variable_id = "h"
        mock_instance.grid_label = "i"
        mock_instance.instance_id = "a.b.c.d.e.f.g.h.i.v200202"

        ESGFItemProperties.check_instance_id(mock_instance)  # type: ignore

    def test_with_invalid_input(self) -> None:
        """Should raise a :py:exc:`ValueError`"""

        mock_instance = Mock(spec=ESGFItemProperties)
        mock_instance.mip_era = "z"
        mock_instance.activity_id = "b"
        mock_instance.institution_id = "c"
        mock_instance.source_id = "d"
        mock_instance.experiment_id = "e"
        mock_instance.variant_label = "f"
        mock_instance.table_id = "g"
        mock_instance.variable_id = "h"
        mock_instance.grid_label = "i"
        mock_instance.instance_id = "a.b.c.d.e.f.g.h.i.v200202"

        with self.assertRaises(ValueError):
            ESGFItemProperties.check_instance_id(mock_instance)  # type: ignore


class TestESGFItemPropertiesCheckCitationURL(TestCase):
    """
    Test the functionality of the :py:ref:`models.item.ESGFItemProperties.check_citation_url` method.
    """

    def test_with_valid_input(self) -> None:
        """Should validate the citation_url value"""

        mock_instance = Mock(spec=ESGFItemProperties)
        mock_instance.mip_era = "z"
        mock_instance.instance_id = "a.b.c.d.e.f.g.h.i.v200202"
        mock_instance.citation_url = (
            "http://cera-www.dkrz.de/WDCC/meta/z/a.b.c.d.e.f.g.h.i.v200202.json"
        )

        ESGFItemProperties.check_citation_url(mock_instance)  # type: ignore

    def test_with_invalid_input(self) -> None:
        """Should raise a :py:exc:`ValueError`"""

        mock_instance = Mock(spec=ESGFItemProperties)
        mock_instance.mip_era = "z"
        mock_instance.instance_id = "a.b.c.d.e.f.g.h.i.v200202"
        mock_instance.citation_url = (
            "http://cera-www.dkrz.de/WDCC/meta/a/a.b.c.d.e.f.g.h.i.v200202.json"
        )

        with self.assertRaises(ValueError):
            ESGFItemProperties.check_citation_url(mock_instance)  # type: ignore


class TestTestESGFItemPropertiesCheckFurtherInfoURL(TestCase):
    """
    Test the functionality of the :py:ref:`models.item.ESGFItemProperties.check_further_info_url` method.
    """

    def test_with_valid_input(self) -> None:
        """Should validate the further_info_url value"""

        mock_instance = Mock(spec=ESGFItemProperties)
        mock_instance.instance_id = "a.b.c.d.e.f.g.h.i.v200202"
        mock_instance.further_info_url = (
            "https://furtherinfo.es-doc.org/a.b.c.d.e.f.g.h.i.v200202"
        )

        ESGFItemProperties.check_further_info_url(mock_instance)  # type: ignore

    def test_with_invalid_input(self) -> None:
        """Should raise a :py:exc:`ValueError`"""

        mock_instance = Mock(spec=ESGFItemProperties)
        mock_instance.instance_id = "a.b.c.d.e.f.g.h.i.v200202"
        mock_instance.further_info_url = (
            "https://furtherinfo.es-doc.org/z.b.c.d.e.f.g.h.i.v200202"
        )

        with self.assertRaises(ValueError):
            ESGFItemProperties.check_further_info_url(mock_instance)  # type: ignore
