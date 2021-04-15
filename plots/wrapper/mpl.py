from matplotlib.axes import Axes
from matplotlib.figure import Figure

from plots.core.plot import Plot
import matplotlib.pyplot as plt

from plots.core.style import TextStyle, TextPosition, Legend


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

        self._ax.set_title(self.title, fontdict={
            'fontsize': self.title_style.size,
            'fontweight': self.title_style.weight,
            'color': self.title_style.color,
        }, loc=self.title_position.location, pad=self.title_position.pad, y=self.title_position.y)

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

    @Plot.legend.setter
    def legend(self, value: Legend):
        Plot.legend.fset(self, value)
        self._ax.legend(value.labels, **value.options)

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

    def show(self):
        return self._ax

    def save(self, output, **kwargs):
        self._figure.savefig(output, **kwargs)

    def plot(self, x, y, style=None, **kwargs):
        line_width = kwargs.get("line_width", 2)
        show_marker = kwargs.get("show_marker", False)
        label = kwargs.get("label", None)
        symbol = kwargs.get("symbol", None)

        d = {
            'linewidth': line_width,
            'marker': 'o' if show_marker else None,
        }

        if style is None:
            self._ax.plot(x, y, style, label=label, **d)
        else:
            self._ax.plot(x, y, label=label, **d)

    def scatter(self, x, y, **kwargs):
        self._ax.scatter(x, y, **kwargs)
