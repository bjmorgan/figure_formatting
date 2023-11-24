# figure_formatting

An installable Python package intended to make it easier to produce near-publication-quality figures that are broadly consitent with the Morgan group style guide.

## Installation

Clone the repo and install:
```
git clone git@github.com:bjmorgan/figure_formatting.git
cd figure_formatting
pip install .
```

## Example usage:
See the [examples](./examples) directory.

### Using the defaults:
After installing the package, you can include the following in any plotting scripts:
```python
from figure_formatting import figure_formatting as ff

ff.set_formatting()
```
