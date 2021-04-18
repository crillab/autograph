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

from abc import abstractmethod
from collections import defaultdict
from typing import Optional

from autograph.core.enumstyle import LineType, MarkerShape
from autograph.core.style import TextStyle, TextPosition, PlotStyle, LegendStyle


class Plot:
    name = 'plot'

    def __init__(self):
        self._data = defaultdict(dict)

    @property
    def figure_size(self):
        return self._data.get('figure_size')

    @figure_size.setter
    def figure_size(self, value):
        self._data['figure_size'] = value

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
        self._set_title_style(value)

    @property
    def title_position(self) -> TextPosition:
        return self._data.get('title').get('position', TextPosition())

    @title_position.setter
    def title_position(self, value):
        self._data['title']['position'] = value
        self._set_title_position(value)

    @property
    def x_label(self):
        return self._data.get('x_axis').get('label')

    @x_label.setter
    def x_label(self, value):
        self._data['x_axis']['label'] = value

    @property
    def x_label_style(self):
        return self._data.get('x_axis').get('style')

    @x_label_style.setter
    def x_label_style(self, value):
        self._data['x_axis']['style'] = value
        self._set_x_label_style(value)

    @property
    def y_label_style(self):
        return self._data.get('y_axis').get('style')

    @y_label_style.setter
    def y_label_style(self, value):
        self._data['y_axis']['style'] = value
        self._set_y_label_style(value)

    @property
    def x_label_position(self):
        return self._data.get('x_axis').get('position')

    @x_label_position.setter
    def x_label_position(self, value):
        self._data['x_axis']['position'] = value
        self._set_x_label_position(value)

    @property
    def y_label_position(self):
        return self._data.get('y_axis').get('position')

    @y_label_position.setter
    def y_label_position(self, value):
        self._data['y_axis']['position'] = value
        self._set_y_label_position(value)

    @property
    def y_label(self):
        return self._data.get('y_axis').get('label')

    @y_label.setter
    def y_label(self, value):
        self._data['y_axis']['label'] = value

    @property
    def log_x(self):
        return self._data.get('x_axis', {}).get('log', False)

    @log_x.setter
    def log_x(self, value: bool):
        self._data['x_axis']['log'] = value

    @property
    def log_y(self):
        return self._data.get('y_axis', {}).get('log', False)

    @log_y.setter
    def log_y(self, value: bool):
        self._data['y_axis']['log'] = value

    @property
    def x_min(self):
        return self._data.get("x_axis", {}).get("min")

    @x_min.setter
    def x_min(self, value):
        self.set_x_lim(left=value)

    @property
    def x_max(self):
        return self._data.get("x_axis", {}).get("max")

    @x_max.setter
    def x_max(self, value):
        self.set_x_lim(right=value)

    @property
    def y_min(self):
        return self._data.get("y_axis", {}).get("min")

    @y_min.setter
    def y_min(self, value):
        self.set_y_lim(bottom=value)

    @property
    def y_max(self):
        return self._data.get("y_axis", {}).get("max")

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

    @property
    def legend(self):
        return self._data.get('legend')

    @legend.setter
    def legend(self, value: LegendStyle):
        self._data['legend'] = value
        self._set_legend(value)

    def set_x_lim(self, left=None, right=None):
        self._data['x_axis']['min'] = left
        self._data['x_axis']['max'] = right

    def set_y_lim(self, bottom=None, up=None):
        self._data['y_axis']['min'] = bottom
        self._data['y_axis']['max'] = up

    def _set_legend(self, value: LegendStyle):
        value.set_plot(self)

    def _set_title_style(self, value: TextStyle):
        value.set_plot(value)

    def _set_x_label_style(self, value: TextStyle):
        value.set_plot(value)

    def _set_y_label_style(self, value: TextStyle):
        value.set_plot(value)

    def _set_title_position(self, value: TextPosition):
        value.set_plot(value)

    def _set_x_label_position(self, value):
        value.set_plot(value)

    def _set_y_label_position(self, value):
        value.set_plot(value)

    @abstractmethod
    def plot(self, x, y, label=None, style: Optional[PlotStyle] = None):
        raise NotImplementedError

    @abstractmethod
    def scatter(self, x, y, label=None, style: Optional[PlotStyle] = None):
        raise NotImplementedError

    def boxplot(self, x):
        raise NotImplementedError

    @abstractmethod
    def show(self):
        raise NotImplementedError

    @abstractmethod
    def save(self, output, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def _line_type_as_string(self, line_type: LineType):
        raise NotImplementedError

    @abstractmethod
    def _marker_shape_as_string(self, shape: MarkerShape):
        raise NotImplementedError
