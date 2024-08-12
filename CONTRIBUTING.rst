Contributing
============

Branch structure
----------------

Please create new features in ``feature/<name_of_feature>`` branch, when
you are ready please create a pull request to merge your feature into a
``release/<version_of_release>`` branch. If there is no applicable
release feel free to create one.

Development environment
-----------------------

Begin by collecting the repo from github.

To contribute, you should be using ``poetry`` as your python package
manager, see https://python-poetry.org for installation instructions.
Please wnsure that when you add or update dependencies, you use the
``poetry add`` or ``poetry add --group <group_name>`` command to do so.
If you do not, it is likely that the CI will reject your change.

Once you have poetry installed, you should install the library with all
it’s dependencies:

.. code:: shell

   foo@bar:~$ poetry install

Then, activate the ``pre-commit hooks`` run:

.. code:: shell

   foo@bar:~$ poetry run install pre-commit

When you commit, the following checks will be run:

-  poetry-check (checks the conformity of the pyproject.toml and
   poetry.lock file)
-  poetry-lock [1]_ (ensures an up-to-date lock file)
-  black [1]_ (python style formatter)
-  isort [1]_ (python import order checker)
-  ruff linter [1]_ (python linter)
-  mypy (python static type analysis)
-  bandit (python SAST analyis)
-  xenon (McCabe cyclomatc complexity analysis)
-  sphinx (dry-run documentation build)

You can disable the ``pre-commit hooks`` per commit with the flag
``--no-verify`` however all checks will be preformed in the CI.

You can also (and are encouraged to) run the ``pre-commit hooks``
manually as often as you like with:

.. code:: shell

   foo@bar:~$ poetry run pre-commit run -a

CI Environment
--------------

The CI Environment runs the same checks as the ``pre-commit hooks`` on
push [2]_ plus the following additional checks:

-  audit (checks all dependencies for vulnerabilities)

.. [1]
   These pre-commit hooks will attempt to fix the issue in place

.. [2]
   On CI, no checks perform code changes in place