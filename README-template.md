# stactools-usfs-lcms

[![PyPI](https://img.shields.io/pypi/v/stactools-usfs-lcms?style=for-the-badge)](https://pypi.org/project/stactools-usfs-lcms/)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/stactools-packages/usfs-lcms/continuous-integration.yml?style=for-the-badge)

- Name: usfs-lcms
- Package: `stactools.usfs_lcms`
- [stactools-usfs-lcms on PyPI](https://pypi.org/project/stactools-usfs-lcms/)
- Owner: @githubusername
- [Dataset homepage](http://example.com)
- STAC extensions used:
  - [proj](https://github.com/stac-extensions/projection/)
- Extra fields:
  - `usfs-lcms:custom`: A custom attribute
- [Browse the example in human-readable form](https://radiantearth.github.io/stac-browser/#/external/raw.githubusercontent.com/stactools-packages/usfs-lcms/main/examples/collection.json)

A short description of the package and its usage.

## STAC examples

- [Collection](examples/collection.json)
- [Item](examples/item/item.json)

## Installation

```shell
pip install stactools-usfs-lcms
```

## Command-line usage

Description of the command line functions

```shell
stac usfs-lcms create-item source destination
```

Use `stac usfs-lcms --help` to see all subcommands and options.

## Contributing

We use [pre-commit](https://pre-commit.com/) to check any changes.
To set up your development environment:

```shell
pip install -e '.[dev]'
pre-commit install
```

To check all files:

```shell
pre-commit run --all-files
```

To run the tests:

```shell
pytest -vv
```

If you've updated the STAC metadata output, update the examples:

```shell
scripts/update-examples
```
