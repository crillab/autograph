from abc import abstractmethod
from collections import defaultdict
from warnings import warn

from plots.core.style import TextStyle, TextPosition


class Plot:
    name = 'plot'

    def __init__(self):
        self._data = defaultdict(dict)
        self._layout = defaultdict(dict)

    @property
    def title(self):
        return self._data.get('title', {}).get('text')

    @title.setter
    def title(self, value):
        self._data['title']['text'] = value

    @property
    def title_style(self) -> TextStyle:
        return self._data.get('title').get('style', TextStyle())

    @title_style.setter
    def title_style(self, value: TextStyle):
        self._data['title']['style'] = value

    @property
    def title_position(self) -> TextPosition:
        return self._data.get('title').get('position', TextPosition())

    @title_position.setter
    def title_position(self, value):
        self._data['title']['position'] = value

    @property
    def x_label(self):
        return self._data.get('x_axis').get('label')

    @x_label.setter
    def x_label(self, value):
        self._data['x_axis']['label'] = value

    @property
    def y_label(self):
        return self._data.get('y_axis').get('label')

    @y_label.setter
    def y_label(self, value):
        self._data['y_label']['label'] = value

    @property
    def log_x(self):
        return self._data.get('y_axis').get('log', False)

    @log_x.setter
    def log_x(self, value: bool):
        self._data['x_label']['log'] = value

    @property
    def log_y(self):
        return self._data.get('y_axis').get('log', False)

    @log_y.setter
    def log_y(self, value: bool):
        self._data['y_axis']['log'] = value

    @property
    def x_min(self):
        return self._data.get("x_label", {}).get("min", None)

    @x_min.setter
    def x_min(self, value):
        self.set_x_lim(left=value)

    @property
    def x_max(self):
        return self._data.get("x_label", {}).get("max", None)

    @x_max.setter
    def x_max(self, value):
        self.set_x_lim(right=value)

    @property
    def y_min(self):
        return self._data.get("y_label", {}).get("min", None)

    @y_min.setter
    def y_min(self, value):
        self.set_y_lim(bottom=value)

    @property
    def y_max(self):
        return self._data.get("y_label", {}).get("max", None)

    @y_max.setter
    def y_max(self, value):
        self.set_y_lim(up=value)

    @property
    def x_lim(self):
        return self.x_min, self.x_max

    @x_lim.setter
    def x_lim(self, value):
        self.set_x_lim(left=value[0], right=value[1])

    @property
    def y_lim(self):
        return self.y_min, self.y_max

    @y_lim.setter
    def y_lim(self, value):
        self.set_y_lim(bottom=value[0], up=value[1])

    def set_x_lim(self, left=None, right=None):
        self._data['x_label']['min'] = left
        self._data['x_label']['max'] = right

    def set_y_lim(self, bottom=None, up=None):
        self._data['y_label']['min'] = bottom
        self._data['y_label']['max'] = up

    @property
    def legend(self):
        return self._data.get('legend')

    @legend.setter
    def legend(self, value):
        self._data['legend'] = value

    @abstractmethod
    def plot(self, x, y, style=None, **kwargs):
        warn('abstract plot')

    @abstractmethod
    def scatter(self, x, y, **kwargs):
        warn('abstract plot')

    @abstractmethod
    def show(self):
        warn('abstract show')

    @abstractmethod
    def save(self, output, **kwargs):
        warn('abstract save')
