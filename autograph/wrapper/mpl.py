from typing import Optional

from matplotlib.axes import Axes
from matplotlib.figure import Figure

from autograph.core.enumstyle import MarkerShape, LineType, Position
from autograph.core.plot import Plot
import matplotlib.pyplot as plt

from autograph.core.style import TextStyle, TextPosition, PlotStyle, LegendStyle


class MPL(Plot):
    name = "matplotlib"

    def __init__(self):
        super().__init__()
        f, a = plt.subplots()
        self._figure: Figure = f
        self._ax: Axes = a

    def __change_title(self):
        if self.title is None:
            return
        kwargs = {'fontdict': {
            'fontsize': self.title_style.size,
            'fontweight': self.title_style.weight,
        }}

        if self.title_position.y is not None:
            kwargs["y"] = self.title_position.y
        if self.title_position.location is not None:
            kwargs["loc"] = self.title_position.location

        if self.title_position.pad is not None:
            kwargs["pad"] = self.title_position.pad
        self._ax.set_title(self.title, **kwargs)

    @Plot.title.setter
    def title(self, value):
        Plot.title.fset(self, value)
        self.__change_title()

    @Plot.title_position.setter
    def title_position(self, value):
        Plot.title_position.fset(self, value)
        self.__change_title()

    @Plot.title_style.setter
    def title_style(self, value):
        Plot.title_style.fset(self, value)
        self.__change_title()

    @Plot.x_label.setter
    def x_label(self, value):
        Plot.x_label.fset(self, value)
        self._ax.set_xlabel(value)

    @Plot.y_label.setter
    def y_label(self, value):
        Plot.y_label.fset(self, value)
        self._ax.set_ylabel(value)

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

    @Plot.legend.setter
    def legend(self, value: LegendStyle):
        Plot.legend.fset(self, value)
        kwargs = self._legend_position_as_mpl(value.position)
        kwargs['title'] = value.title
        kwargs['ncol'] = value.n_col
        self._ax.legend(**kwargs)

    def show(self):
        return self._ax

    def save(self, output, **kwargs):
        self._figure.savefig(output, **kwargs)

    def plot(self, x, y, label=None, style: Optional[PlotStyle] = None):
        self._internal_plot(x, y, label, style, self._ax.plot)

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
