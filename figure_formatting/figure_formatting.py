from matplotlib import rc
from matplotlib import rcParams
from matplotlib import cycler
from collections import OrderedDict

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
              'mathtext.rm': f'Helvetica',
              'mathtext.it': f'Helvetica:italic',
              'mathtext.bf': f'Helvetica',
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

def set_formatting(Dict: formatting=formatting) -> None:
    for k, v in formatting.items():
        rcParams[k] = v

def set_palette(palette: OrderedDict) -> None:
    color_cycle = palette.values()
    rcParams['axes.prop_cycle'] = cycler(color=color_cycle)

