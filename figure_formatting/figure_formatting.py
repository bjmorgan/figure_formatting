from collections import OrderedDict
from pathlib import Path

from fontTools.ttLib import TTCollection
from matplotlib import cycler, font_manager, get_cachedir, rcParams

# Helvetica Neue ships on macOS as a font collection. matplotlib reads only the
# first face of a collection, so the italic and bold faces used for maths are
# extracted and registered separately (see register_helvetica_neue).
HELVETICA_NEUE = '/System/Library/Fonts/HelveticaNeue.ttc'
HELVETICA_NEUE_FACES = {'Bold': 1, 'Italic': 2}   # face indices in the collection

# ---------------------------------------------------
# Color sets
# ---------------------------------------------------
# Standard tableau 20 set
tableau = OrderedDict([
    ('blue',        '#1F77B4'),
    ('orange',      '#FF7F0E'),
    ('green',       '#2CA02C'),
    ('red',         '#D62728'),
    ('purple',      '#9467BD'),
    ('brown',       '#8C564B'),
    ('pink',        '#E377C2'),
    ('grey',        '#7F7F7F'),
    ('yellow',      '#BCBD22'),
    ('turquoise',   '#17BECF'),
    ('lightblue',   '#AEC7E8'),
    ('lightorange', '#FFBB78'),
    ('lightgreen',  '#98DF8A'),
    ('lightred',    '#FF9896'),
    ('lightpurple', '#C5B0D5'),
    ('lightbrown',  '#C49C94'),
    ('lightpink',   '#F7B6D2'),
    ('lightgrey',   '#C7C7C7'),
    ('lightyellow', '#DBDB8D'),
    ('lightturquoise', '#9EDAE5')
])

# Slightly pastel versions of the tableu colours
tableauP = OrderedDict([
    ('blue',        '#5c95c3'),
    ('orange',      '#fd9b50'),
    ('green',       '#65b762'),
    ('red',         '#de5b62'),
    ('purple',      '#a762b7'),
    ('brown',       '#bf6f2e')
])

fontsize = 8
linewidth = 0.7

nearly_black = '#161616'
light_grey = '#EEEEEE'
lighter_grey = '#F5F5F5'
white = '#FFFFFF'

formatting = {'font.family': 'sans-serif',
              'font.sans-serif': ['Helvetica Neue',
                                  'Helvetica',
                                  'DejaVu Sans'],
              'mathtext.fontset': 'custom',
              'mathtext.rm': 'Helvetica Neue',
              'mathtext.it': 'Helvetica Neue:italic',
              'mathtext.bf': 'Helvetica Neue:bold',
              'font.size': fontsize,
              'axes.formatter.limits': (-3,3),
              'xtick.major.pad': 3,
              'ytick.major.pad': 3,
              'ytick.color': nearly_black,
              'xtick.color': nearly_black,
              'xtick.labelsize': fontsize,
              'ytick.labelsize': fontsize,
              'ytick.major.size': 3,
              'ytick.minor.size': 1.5,
              'xtick.major.size': 3,
              'xtick.minor.size': 1.5,
              'xtick.major.width': linewidth,
              'xtick.minor.width': linewidth,
              'ytick.major.width': linewidth,
              'ytick.minor.width': linewidth,
              'axes.labelcolor': nearly_black,
              'legend.facecolor': white,
              'legend.fancybox': False,
              'legend.frameon': False,
              'savefig.bbox':'tight',
              'axes.facecolor': white,
              'axes.labelpad': 2,
              'axes.labelsize': fontsize,
              'axes.titlesize': fontsize,
              'axes.titlepad': 7,
              'axes.titlelocation': 'left',
              'lines.markersize': 5.0,
              'lines.scale_dashes': False,
              'axes.linewidth': linewidth,
              'lines.linewidth': linewidth,
              'figure.dpi': 127,
              'figure.figsize': (3.15, 1.95)} # Default size = landscape (8 cm width + golden ratio)

def register_helvetica_neue() -> None:
    """Register the Helvetica Neue italic and bold faces with matplotlib.

    Each face is extracted once to matplotlib's cache directory. Does nothing
    if the collection is not installed, in which case matplotlib falls back to
    its default fonts.
    """
    if not Path(HELVETICA_NEUE).exists():
        return
    cache = Path(get_cachedir()) / 'figure_formatting'
    cache.mkdir(exist_ok=True)
    for style, index in HELVETICA_NEUE_FACES.items():
        path = cache / f'HelveticaNeue-{style}.ttf'
        if not path.exists():
            TTCollection(HELVETICA_NEUE).fonts[index].save(path)
        font_manager.fontManager.addfont(path)

def set_formatting(formatting: dict = formatting) -> None:
    register_helvetica_neue()
    rcParams.update(formatting)

def set_palette(palette: OrderedDict) -> None:
    color_cycle = palette.values()
    rcParams['axes.prop_cycle'] = cycler(color=color_cycle)

