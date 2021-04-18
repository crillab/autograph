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

from autograph.core.enumstyle import MarkerShape, LineType, Position
from autograph.core.plot import Plot
import plotly.graph_objects as go
import plotly.io as pio

from autograph.core.style import TextPosition, TextStyle, LegendStyle, BoxStyle

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
        self._layout_plotly["xaxis"]["title"] = {"text": value}

    @Plot.y_label.setter
    def y_label(self, value):
        Plot.y_label.fset(self, value)
        self._layout_plotly["yaxis"]['title'] = {"text": value}

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

    def boxplot(self, x, labels=None, style: BoxStyle = BoxStyle()):
        if labels is not None:
            for s, name in zip(x, labels):
                self._data_plotly.append(go.Box({
                    'y': s,
                    'boxpoints': 'all',
                    'name': name,
                    'marker.size': 2,
                    'boxmean': style.show_mean,
                    'showlegend': False
                }))
        else:
            for s in x:
                self._data_plotly.append(go.Box({
                    'y': s,
                    'boxpoints': 'all',
                    'marker.size': 2,
                    'boxmean': style.show_mean,
                    'showlegend': False
                }))

    def save(self, output, **kwargs):
        pass

    def _line_type_as_string(self, line_type: LineType):
        return line_type.plotly_string

    def _marker_shape_as_string(self, shape: MarkerShape):
        return shape.plotly_string

    def _set_legend(self, value: LegendStyle):
        super()._set_legend(value)
        enabled = value is not None
        self._layout_plotly["showlegend"] = enabled
        if enabled:
            value.set_update_function(self._set_legend)
            if value.title is not None:
                self._layout_plotly["legend"]["title"] = {
                    "text": value.title
                }

    def _set_title_style(self, value: TextStyle):
        super()._set_title_style(value)
        value.set_update_function(self._set_title_style)
        self.__change_title()

    def _set_title_position(self, value: TextPosition):
        super()._set_title_position(value)
        value.set_update_function(self._set_title_position)
        self.__change_title()

    def _set_x_label_style(self, value: TextStyle):
        super()._set_x_label_style(value)
        value.set_update_function(self._set_x_label_style)
        self.__change_x_label()

    def _set_y_label_style(self, value: TextStyle):
        super()._set_y_label_style(value)
        value.set_update_function(self._set_y_label_style)
        self.__change_y_label()

    def _set_x_label_position(self, value: TextPosition):
        super()._set_x_label_position(value)
        value.set_update_function(self._set_x_label_position)
        self.__change_x_label()

    def _set_y_label_position(self, value: TextPosition):
        super()._set_y_label_position(value)
        value.set_update_function(self._set_y_label_position)
        self.__change_y_label()

    def __change_title(self):
        if self.title is None:
            return
        self._layout_plotly.update({
            "title_font_family": self.title_style.font_name,
            "title_font_color": self.title_style.color,
            "title_font_size": self.title_style.size
        })
        if self.title_style.weight is not None:
            self.title = self.title_style.weight.plotly_string.format(self.title)

    def __change_x_label(self):
        if self.x_label is None:
            return
        self.__change_style(self.x_label_style, "xaxis")

    def __change_y_label(self):
        if self.y_label is None:
            return
        self.__change_style(self.y_label_style, "yaxis")

    def __change_style(self, style, key):
        self._layout_plotly[key]["title"].update({
            "font": {
                "family": style.font_name,
                "size": style.size,
                "color": style.color,
            },
        })
        if style.weight is not None:
            self._layout_plotly[key]["title"]["text"] = style.weight.plotly_string \
                .format(self._layout_plotly[key]["title"]["text"])

    # def _legend_position_as_plotly(self, position: Position):
    #     if position == Position.TOP:
    #         return dict(xanchor="center", yanchor="top")
    #     if position == Position.RIGHT:
    #         return dict(xanchor="right", yanchor="middle")
    #     if position == Position.BOTTOM:
    #         return dict(xanchor="center", yanchor="bottom")
    #     if position == Position.LEFT:
    #         return dict(xanchor="left", yanchor="center")
