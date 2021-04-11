from abc import abstractmethod
from warnings import warn

from plots.style import TextStyle, TextPosition


class Plot:
    def __init__(self):
        self._title = None
        self._x_label = None
        self._y_label = None
        self._log_x = False
        self._log_y = False
        self._style = {}
        self._position = {}

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def title_style(self):
        return self._style.get('title')

    @title_style.setter
    def title_style(self, value: TextStyle):
        self.__apply_style_for('title', value)

    @property
    def title_position(self):
        return self._position.get('title')

    @title_position.setter
    def title_position(self, value: TextPosition):
        self.__apply_position_for('title', value)

    def __apply_style_for(self, key, text_style: TextStyle):
        """
        :param key: possible values: {'title','xlabel','ylabel'}
        :param text_style: A text style object
        :return:
        """
        self._style[key] = text_style

    def __apply_position_for(self, key, text_position: TextPosition):
        """

        :param key: possible values: {'title','xlabel','ylabel'}
        :param text_postion: A text postion object
        :return:
        """
        self._position[key] = text_position

    @property
    def x_label(self):
        return self._x_label

    @x_label.setter
    def x_label(self, value):
        self._x_label = value

    @property
    def y_label(self):
        return self._y_label

    @y_label.setter
    def y_label(self, value):
        self._y_label = value

    def set_x_lim(self, left=None, right=None):
        warn('function set_x_limn() not supported')

    def set_y_lim(self, bottom=None, up=None):
        warn('function set_y_lim() not supported')

    @property
    def log_x(self):
        return self._log_x

    @log_x.setter
    def log_x(self, value):
        self._log_x = value

    @property
    def log_y(self):
        return self._log_y

    @log_y.setter
    def log_y(self, value):
        self._log_y = value
