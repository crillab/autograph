from collections import defaultdict

from plots.core.plot import Plot
import plotly.graph_objects as go


class Plotly(Plot):
    name = "plotly"

    def __init__(self):
        super().__init__()
        self._data_plotly = {}
        self._layout_plotly = defaultdict(dict)

    @Plot.title.setter
    def title(self, value):
        Plot.title.fset(self, value)

    @Plot.title_position.setter
    def title_position(self, value):
        Plot.title_position.fset(self, value)

    @Plot.title_style.setter
    def title_style(self, value):
        Plot.title_style.fset(self, value)

    @Plot.x_label.setter
    def x_label(self, value):
        Plot.x_label.fset(self, value)

    @Plot.y_label.setter
    def y_label(self, value):
        Plot.y_label.fset(self, value)

    @Plot.log_x.setter
    def log_x(self, value):
        Plot.log_x.fset(self, value)

    @Plot.log_y.setter
    def log_y(self, value):
        Plot.log_y.fset(self, value)

    def set_x_lim(self, left=None, right=None):
        super().set_x_lim(left, right)

    def set_y_lim(self, bottom=None, up=None):
        super().set_y_lim(bottom, up)

    def show(self):
        return go.Figure(data=self._data_plotly, layout=self._layout_plotly)

    def save(self, output):
        pass
