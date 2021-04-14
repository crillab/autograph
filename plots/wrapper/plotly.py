from collections import defaultdict

from plots.core.plot import Plot
import plotly.graph_objects as go


class Plotly(Plot):
    name = "plotly"

    def __init__(self):
        super().__init__()
        self._data_plotly = {}
        self._layout_plotly = defaultdict(dict)

    @property
    def title(self):
        return self._data['']
