# How to contribute?

## Branch structure

Please create new features in `feature/<name_of_feature>` branch, when you are ready please create a pull request to 
merge your feature into a `release/<version_of_release>` branch. If there is no applicable release feel free to create 
one.

## Development environment

Begin by collecting the repo from github.

To contribute, you should be using `poetry` as your python package manager, see https://python-poetry.org for
installation instructions. Please wnsure that when you add or update dependencies, you use the `poetry add` or 
`poetry add --group <group_name>` command to do so. If you do not, it is likely that the CI will reject your change.

Once you have poetry installed, you should install the library with all it's dependencies:

```shell
foo@bar:~$ poetry install 
```

Then, activate the `pre-commit hooks` run:

```shell
foo@bar:~$ poetry run install pre-commit
```

When you commit, the following checks will be run:

- black[^1] (python style formatter)
- isort[^1] (python import order checker)
- ruff[^1]  (python linter)
- mypy      (python static type analysis)
- bandit    (pythin SAST analyis)
- xenon     (McCabe cyclomatc complexity analysis)

You can disable the `pre-commit hooks` per commit with the flag `--no-verify` however all checks will be preformed in the CI.

You can also (and are encouraged to) run the `pre-commit hooks` manually as often as you like with:

```shell
foo@bar:~$ poetry run pre-commit run -a
```

## CI Environment

The CI Enviroment runs the same checks as the `pre-commit hooks` on push[^2] plus the following additional checks:

- audit  (checks all dependencies for vulnerabilities) 

[^1]: These pre-commit hooks will attempt to fix the issue in place
[^2]: On CI, no checks perform code changes in place
  
