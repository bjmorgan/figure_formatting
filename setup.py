"""
Utilities for publication-quality figures.
"""

from setuptools import setup, find_packages
from figure_formatting.version import __version__ as VERSION

readme = 'README.md'
long_description = open(readme).read()

setup(
    name='figure-formatting',
    version=VERSION,
    description='Python utilities for generating publication-quality figures',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Benjamin J. Morgan',
    author_email='bjm42@bath.ac.uk',
    url='https://github.com/bjmorgan/figure_formatting', 
    download_url='https://github.com/bjmorgan/figure_formatting/archive/{}.tar.gz'.format(VERSION),
    license='MIT',
    install_requires=['matplotlib'],
    python_requires='>=3.7'
    )
