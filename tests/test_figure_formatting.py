from pathlib import Path

import pytest
from matplotlib import font_manager, rcParams
from matplotlib.font_manager import FontProperties

from figure_formatting.figure_formatting import HELVETICA_NEUE, set_formatting

needs_helvetica_neue = pytest.mark.skipif(not Path(HELVETICA_NEUE).exists(),
                                          reason='Helvetica Neue collection not installed')


def font_name(spec):
    """Full name of the font file matplotlib resolves a mathtext font spec ('family:style') to."""
    path = font_manager.findfont(FontProperties._from_any(spec), fallback_to_default=False)
    return font_manager.get_font(path).family_name + ' ' + font_manager.get_font(path).style_name


@needs_helvetica_neue
@pytest.mark.parametrize('key, expected', [('mathtext.rm', 'Helvetica Neue Regular'),
                                           ('mathtext.it', 'Helvetica Neue Italic'),
                                           ('mathtext.bf', 'Helvetica Neue Bold')])
def test_maths_fonts_resolve_to_helvetica_neue(key, expected):
    set_formatting()
    assert font_name(rcParams[key]) == expected


def test_set_formatting_applies_the_dictionary_it_is_given():
    set_formatting({'font.size': 13})
    assert rcParams['font.size'] == 13
