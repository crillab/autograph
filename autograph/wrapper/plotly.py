# ##############################################################################
#  Copyright © 2021 Univ Artois & CNRS, Exakis Nelite                          #
#                                                                              #
#  Permission is hereby granted, free of charge, to any person                 #
#  obtaining a copy of this software and associated documentation              #
#  files (the “Software”), to deal in the Software without                     #
#  restriction, including without limitation the rights to use,                #
#  copy, modify, merge, publish, distribute, sublicense, and/or sell           #
#  copies of the Software, and to permit persons to whom the                   #
#  Software is furnished to do so, subject to the following                    #
#  conditions:                                                                 #
#                                                                              #
#  The above copyright notice and this permission notice shall be              #
#  included in all copies or substantial portions of the Software.             #
#                                                                              #
#  THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,             #
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES             #
#  OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                    #
#  NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT                 #
#  HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,                #
#  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING                #
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR               #
#  OTHER DEALINGS IN THE SOFTWARE.                                             #
# ##############################################################################

from collections import defaultdict
from math import log10

from autograph.core.plot import Plot
import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = 'none'


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
        self._layout_plotly["xaxis"]["title"] = value

    @Plot.y_label.setter
    def y_label(self, value):
        Plot.y_label.fset(self, value)
        self._layout_plotly["yaxis"]['title'] = value

    @Plot.log_x.setter
    def log_x(self, value):
        Plot.log_x.fset(self, value)
        self._layout_plotly["xaxis"]["type"] = 'log' if value else 'linear'
        self._update_x_lim()

    @Plot.log_y.setter
    def log_y(self, value):
        Plot.log_y.fset(self, value)
        self._layout_plotly["yaxis"]["type"] = 'log' if value else 'linear'
        self._update_y_lim()

    def set_x_lim(self, left=None, right=None):
        super().set_x_lim(left, right)
        self._update_x_lim(left, right)

    def _update_x_lim(self, left=None, right=None):
        x_min = left if left is not None else self.x_min
        x_max = right if right is not None else self.x_max

        if self.log_x:
            x_min = log10(x_min) if x_min else None
            x_max = log10(x_max) if x_max else None

        self._layout_plotly['xaxis']['range'] = [x_min, x_max]

    def set_y_lim(self, bottom=None, up=None):
        super().set_y_lim(bottom, up)
        self._update_y_lim(bottom, up)

    def _update_y_lim(self, bottom=None, up=None):
        y_min = bottom if bottom is not None else self.y_min
        y_max = up if up is not None else self.y_max

        if self.log_y:
            y_min = log10(y_min) if y_min else None
            y_max = log10(y_max) if y_max else None

        self._layout_plotly['yaxis']['range'] = [y_min, y_max]

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

    def save(self, output, **kwargs):
        pass
