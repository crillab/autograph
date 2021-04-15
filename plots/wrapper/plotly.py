from collections import defaultdict
from math import log10

from plots.core.plot import Plot
import plotly.graph_objects as go


class Plotly(Plot):
    name = "plotly"

    def __init__(self):
        super().__init__()
        self._data_plotly = []
        self._layout_plotly = defaultdict(dict)

    @Plot.title.setter
    def title(self, value):
        Plot.title.fset(self, value)
        self._layout_plotly["title.text"] = value

    @Plot.x_label.setter
    def x_label(self, value):
        Plot.x_label.fset(self, value)
        self._layout_plotly["xaxis.title.text"] = value

    @Plot.y_label.setter
    def y_label(self, value):
        Plot.y_label.fset(self, value)
        self._layout_plotly["yaxis.title.text"] = value

    @Plot.log_x.setter
    def log_x(self, value):
        Plot.log_x.fset(self, value)
        self._layout_plotly["xaxis"] = {"type": 'log' if value else 'linear'}

    @Plot.log_y.setter
    def log_y(self, value):
        Plot.log_y.fset(self, value)
        self._layout_plotly["yaxis"] = {"type": 'log' if value else 'linear'}

    def set_x_lim(self, left=None, right=None):
        super().set_x_lim(left, right)
        self._layout_plotly['xaxis'] = {
            'range': [log10(self.x_min) if self.log_x else self.x_min, log10(self.x_max) if self.log_x else self.x_max]
        }

    def set_y_lim(self, bottom=None, up=None):
        super().set_y_lim(bottom, up)
        self._layout_plotly['yaxis'] = {
            'range': [log10(self.y_min) if self.log_y else self.y_min, log10(self.y_max) if self.log_y else self.y_max]
        }

    def show(self):
        return go.Figure(data=self._data_plotly, layout=self._layout_plotly)

    def plot(self, x, y, style=None, **kwargs):
        line_width = kwargs.get("line_width", 2)
        show_marker = kwargs.get("show_marker", False)
        label = kwargs.get("label", None)
        symbol = kwargs.get("symbol", None)

        self._data_plotly.append(
            {
                'name': label,
                'mode': 'lines+markers' if show_marker else 'lines',
                'marker.symbol': symbol,
                'line.width': line_width,
                'x': x,
                'y': y,
            }
        )

    def scatter(self, x, y, **kwargs):
        col = kwargs.get("col", None)
        label = kwargs.get("label", None)
        d = {
            'x': x,
            'y': y,
            'mode': 'markers',
            'name': label

        }
        if col is not None:
            d['text'] = col
        self._data_plotly.append(d)
