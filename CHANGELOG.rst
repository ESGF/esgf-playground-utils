Changelog
=========

All notable changes to this package are recorded in this document.

This format is based on `Keep a ChangeLog <https://keepachangelog.com/>`_ and this project
adheres to `Semantic Versioning <https://semver.org>`_.

[Unreleased] - 2024-09-04
-------------------------

`0.3.3 <https://github.com/ESGF/esgf-playground-utils/releases/tag/0.3.3>`_  - 2024-09-04
-----------------------------------------------------------------------------------------

Added
^^^^^
- Added new kafka PartialUpdatePayload to Data class

Changed
^^^^^^^

-Updated poetry (1.82 -> 1.83)

Removed
^^^^^^^

Fixed
^^^^^


`0.3.2 <https://github.com/ESGF/esgf-playground-utils/releases/tag/0.3.2>`_  - 2024-09-04
-----------------------------------------------------------------------------------------

Added
^^^^^

- Payload model (:py:class:`esgf_playground_utils.models.kafka.PartialUpdatePayload`) for "soft delete` of an
  :py:class:`stac_pydantic.item.Item`.

Changed
^^^^^^^

- Updated certifi (2024.7.4 -> 2024.8.30)
- Updated idna (3.7 -> 3.8)
- Updated pbr (6.0.0 -> 6.1.0)
- Updated geojson-pydantic (1.1.0 -> 1.1.1)
- Updated rich (13.7.1 -> 13.8.0)
- Updated stevedore (5.2.0 -> 5.3.0)
- Updated mypy (1.11.1 -> 1.11.2)
- Updated sphinx-autoapi (3.2.1 -> 3.3.1)
- Updated stac-pydantic (3.1.1 -> 3.1.2)

Removed
^^^^^^^

Fixed
^^^^^

`0.3.1 <https://github.com/ESGF/esgf-playground-utils/releases/tag/0.3.1>`_ - 2024-08-13
----------------------------------------------------------------------------------------

Added
^^^^^

- Community documentation
- Pre-commit hooks for quality
- Documentation published to GitHub Pages

Changed
^^^^^^^

- :py:attr:`esgf_playground_utils.models.kafka.UpdatePayload.item_id` added to enable canonical id of resource
  to be changed.

Removed
^^^^^^^

Fixed
^^^^^

`0.3.0 <https://github.com/ESGF/esgf-playground-utils/releases/tag/0.3.0>`_ - 2024-07-22
------------------------------------------------------------------------------------------

Initial working release.

Added
^^^^^

Changed
^^^^^^^

Removed
^^^^^^^

Fixed
^^^^^

