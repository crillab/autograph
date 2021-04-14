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
        return self._data['title']['text']

    @title.setter
    def title(self, value):
        self._data['title']['text'] = value

    @property
    def title_style(self) -> TextStyle:
        return self._data.get('title').get('style')

    @title_style.setter
    def title_style(self, value: TextStyle):
        self._data['title']['style'] = value

    @property
    def title_position(self) -> TextPosition:
        return self._data.get('title').get('position')

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

    def set_x_lim(self, left=None, right=None):
        self._data['x_label']['min'] = left
        self._data['x_label']['max'] = right

    def set_y_lim(self, bottom=None, up=None):
        self._data['y_label']['min'] = bottom
        self._data['y_label']['max'] = up
