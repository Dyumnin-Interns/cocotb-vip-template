# Cocotb VIP templates

[![ci](https://github.com/dyumnin-interns/cocotb-vip-templates/workflows/ci/badge.svg)](https://github.com/dyumnin-interns/cocotb-vip-templates/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://dyumnin-interns.github.io/cocotb-vip-templates/)
[![pypi version](https://img.shields.io/pypi/v/cocotb-vip-templates.svg)](https://pypi.org/project/cocotb-vip-templates/)
[![gitpod](https://img.shields.io/badge/gitpod-workspace-blue.svg?style=flat)](https://gitpod.io/#https://github.com/dyumnin-interns/cocotb-vip-templates)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://app.gitter.im/#/room/#cocotb-vip-templates:gitter.im)

   Template file for creation of cocotb VIP

## Development

```bash
python3 -m pip install --user pipx
pipx install pdm
pdm install
pdm install -G ci-quality
pdm run pre-commit install
```

or simply run make install which will execute the above commands.
```bash
make install
```
Install pdm

## Package Installation

With `pip`:

```bash
pip install cocotb-vip-templates
```

## Package Documents
* Overview of what the package does.
* Example of how to use the package in your code.
