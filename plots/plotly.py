from collections import defaultdict

from plots.plot import Plot
import plotly.graph_objects as go


class Plotly(Plot):
    def __init__(self):
        self._data = {}
        self._layout = defaultdict(dict)

    def set_tile(self, label, fontdict=None, loc=None, pas=None, *, y=None, **kwargs):
        self._layout['title.text'] = label

    def set_xlabel(self, xlabel, fontdict=None, labelpad=None, loc=None, **kwargs):
        self._layout['xaxis']['title'] = xlabel

    def set_ylabel(self, ylabel, fontdict=None, labelpad=None, loc=None, **kwargs):
        self._layout['yaxis']['title'] = ylabel

    def set_xscale(self, values, **kwargs):
        self._layout['xaxis']['type'] = values

    def set_yscale(self, values, **kwargs):
        self._layout['yaxis']['type'] = values



    def get_figure(self):
        return go.Figure({'data': self._data, 'layout': self._layout})
