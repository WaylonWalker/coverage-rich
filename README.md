# coverage-rich

[![PyPI - Version](https://img.shields.io/pypi/v/coverage-rich.svg)](https://pypi.org/project/coverage-rich)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/coverage-rich.svg)](https://pypi.org/project/coverage-rich)

-----


## Installation

```console
pip install coverage-rich
```
## Usage

``` bash
coverage run -m pytest
coverage-rich report
```

## configuration

`coverage-rich` will send a failure code if there is insufficient total coverage, this is configurable by setting the `fail-under` value.

**pyproject.toml**

``` toml
[tool.coverage_rich]
fail-under=0 # default 80
```
**.coverage_rich**, **coverage_rich.ini**
``` ini
[coverage_rich]
fail-under = 1
```

**setup.cfg**
``` cfg
[tool.coverage_rich]
fail-under = 22
```


## Examples

`coverage-rich` (left) compared to `coverage report -m` (right)

<img src='https://user-images.githubusercontent.com/22648375/218324200-d6b8078b-8f24-4163-9c02-8f6d695d4d4a.png' align='left' width='45%'>
<img src='https://user-images.githubusercontent.com/22648375/218324226-ece0b3d6-e1a9-4644-b8d1-d3adf4568cf0.png' align='right' width='45%'>
<br clear="both"/>

<img src='https://user-images.githubusercontent.com/22648375/218325189-daf0381b-8ddc-482e-8bb4-7642cade9a52.png' align='left' width='45%'>
<img src='https://user-images.githubusercontent.com/22648375/218325218-3ba5c899-f2d8-4b2d-9cb5-93fabe7511cd.png' align='right' width='45%'>
<br clear="both"/>

## License

`coverage-rich` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
