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

from typing import Optional

from matplotlib.axes import Axes
from matplotlib.figure import Figure

from autograph.core.enumstyle import MarkerShape, LineType, Position
from autograph.core.plot import Plot
import matplotlib.pyplot as plt

from autograph.core.style import TextStyle, TextPosition, PlotStyle, LegendStyle, BoxStyle


class MPL(Plot):
    name = "matplotlib"

    def __init__(self):
        super().__init__()
        f, a = plt.subplots()
        self._figure: Figure = f
        self._ax: Axes = a

    @Plot.figure_size.setter
    def figure_size(self, value: tuple):
        Plot.figure_size.fset(self, value)
        self._figure.set_size_inches(value[0], value[1])

    @Plot.title.setter
    def title(self, value):
        Plot.title.fset(self, value)
        self.__change_title()

    @Plot.x_label.setter
    def x_label(self, value):
        Plot.x_label.fset(self, value)
        self.__change_x_label()

    @Plot.y_label.setter
    def y_label(self, value):
        Plot.y_label.fset(self, value)
        self.__change_y_label()

    @Plot.log_x.setter
    def log_x(self, value):
        Plot.log_x.fset(self, value)
        self._ax.set_xscale('log' if self.log_x else 'linear')

    @Plot.log_y.setter
    def log_y(self, value):
        Plot.log_y.fset(self, value)
        self._ax.set_yscale('log' if self.log_y else 'linear')

    def set_x_lim(self, left=None, right=None):
        super().set_x_lim(left, right)
        left = left if left is not None else self._ax.get_xlim()[0]
        right = right if right is not None else self._ax.get_xlim()[1]
        self._ax.set_xlim([left, right])

    def set_y_lim(self, bottom=None, up=None):
        super().set_y_lim(bottom, up)
        bottom = bottom if bottom is not None else self._ax.get_ylim()[0]
        up = up if up is not None else self._ax.get_ylim()[1]
        self._ax.set_ylim([bottom, up])

    def _set_legend(self, value: LegendStyle):
        super()._set_legend(value)
        value.set_update_function(self._set_legend)
        kwargs = self._legend_position_as_mpl(value.position)
        kwargs['title'] = value.title
        kwargs['ncol'] = value.n_col
        self._ax.legend(**kwargs)

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

    def show(self):
        return self._figure, self._ax

    def save(self, output, **kwargs):
        self._figure.savefig(output, **kwargs)

    def plot(self, x, y, label=None, style: Optional[PlotStyle] = None):
        self._internal_plot(x, y, label, style, self._ax.plot)

    def boxplot(self, x, labels=None, style: BoxStyle = BoxStyle()):
        self._ax.boxplot(x, labels=labels, meanline=style.mean_line, showmeans=style.show_mean,
                         vert=style.vert)

    def _style_as_kwargs(self, style):
        kwargs = {}
        if style.line_weight is not None:
            kwargs['linewidth'] = style.line_weight
        if style.line_type is not None:
            kwargs['linestyle'] = self._line_type_as_string(style.line_type)
        if style.marker_weight is not None:
            kwargs['markersize'] = style.marker_weight
        if style.marker_shape is not None:
            kwargs['marker'] = self._marker_shape_as_string(style.marker_shape)
        if style.color is not None:
            kwargs['color'] = style.color
        return kwargs

    def scatter(self, x, y, label=None, style: Optional[PlotStyle] = None):
        self._internal_plot(x, y, label, style, self._ax.scatter)

    def _internal_plot(self, x, y, label, style: Optional[PlotStyle], plot_function):
        if style is None:
            plot_function(x, y, label=label)
            return
        kwargs = self._style_as_kwargs(style)
        plot_function(x, y, label=label, **kwargs)

    def _line_type_as_string(self, line_type: LineType):
        return line_type.mpl_string

    def _marker_shape_as_string(self, shape: MarkerShape):
        return shape.mpl_string

    def _legend_position_as_mpl(self, position: Position):
        if position == Position.TOP:
            return dict(loc="lower center", bbox_to_anchor=(.5, 1.1))
        if position == Position.RIGHT:
            return dict(loc="center left", bbox_to_anchor=(1.1, .5))
        if position == Position.BOTTOM:
            return dict(loc="upper center", bbox_to_anchor=(.5, -.1))
        if position == Position.LEFT:
            return dict(loc="center right", bbox_to_anchor=(-.1, .5))

    def __change_title(self):
        if self.title is None:
            return
        kwargs = self.__text_style_and_position_as_kwargs(self.title_style, self.title_position)
        self._ax.set_title(self.title, **kwargs)

    def __change_x_label(self):
        if self.x_label is None:
            return
        kwargs = self.__text_style_and_position_as_kwargs(self.x_label_style, self.x_label_position)
        self._ax.set_xlabel(self.x_label, **kwargs)

    def __change_y_label(self):
        if self.y_label is None:
            return
        kwargs = self.__text_style_and_position_as_kwargs(self.y_label_style, self.y_label_position)
        self._ax.set_ylabel(self.y_label, **kwargs)

    def __text_style_and_position_as_kwargs(self, text_style, text_position):
        kwargs = {'fontdict': {

        }}

        if text_style is not None and text_style.size is not None:
            kwargs['fontdict']['fontsize'] = text_style.size
        if text_style is not None and text_style.weight is not None:
            kwargs['fontdict']['fontweight'] = text_style.weight.mpl_string
        if text_style is not None and text_style.color is not None:
            kwargs['fontdict']['color'] = text_style.color
        if text_style is not None and text_style.font_name is not None:
            kwargs['fontdict']['fontname'] = text_style.font_name

        if text_position is not None and text_position.y is not None:
            kwargs["y"] = text_position.y
        if text_position is not None and text_position.location is not None:
            kwargs["loc"] = text_position.location
        if text_position is not None and text_position.pad is not None:
            kwargs["pad"] = text_position.pad
        return kwargs
