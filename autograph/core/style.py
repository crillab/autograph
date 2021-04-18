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

from matplotlib import rcParams

from autograph.core.enumstyle import LineType, MarkerShape, Position, FontWeight


class AbstractStyle:
    def __init__(self):
        self._data = {}
        self._plot = None
        self._update_function = None

    def set_plot(self, plot):
        self._plot = plot

    def set_update_function(self, call):
        self._update_function = call


class LegendStyle(AbstractStyle):
    def __init__(self):
        super().__init__()

    @property
    def position(self):
        return self._data.get('position', Position.BOTTOM)

    @position.setter
    def position(self, value):
        self._data['position'] = value
        self._update_function(self)

    @property
    def n_col(self):
        return self._data.get('n_col', 1)

    @n_col.setter
    def n_col(self, value):
        self._data['n_col'] = value
        self._update_function(self)

    @property
    def title(self):
        return self._data.get('title', None)

    @title.setter
    def title(self, value):
        self._data['title'] = value
        self._update_function(self)


class TextStyle(AbstractStyle):
    def __init__(self):
        super().__init__()

    @property
    def size(self):
        return self._data.get("size")

    @size.setter
    def size(self, value):
        self._data["size"] = value
        self._update_function(self)

    @property
    def weight(self) -> FontWeight:
        return self._data.get("weight")

    @weight.setter
    def weight(self, value: FontWeight):
        self._data["weight"] = value
        self._update_function(self)

    @property
    def color(self):
        return self._data.get("color")

    @color.setter
    def color(self, value):
        self._data["color"] = value
        self._update_function(self)

    @property
    def font_name(self):
        return self._data.get("font_name")

    @font_name.setter
    def font_name(self, value):
        self._data["font_name"] = value
        self._update_function(self)


class TextPosition(AbstractStyle):
    def __init__(self):
        super().__init__()

    @property
    def pad(self):
        return self._data.get("pad")

    @pad.setter
    def pad(self, value):
        self._data['pad'] = value

    @property
    def location(self):
        return self._data.get("location")

    @location.setter
    def location(self, value):
        self._data['location'] = value

    @property
    def y(self):
        return self._data.get("y")

    @y.setter
    def y(self, value):
        self._data['y'] = value


class PlotStyle(AbstractStyle):
    def __init__(self):
        super().__init__()

    @property
    def color(self):
        return self._data.get('color')

    @color.setter
    def color(self, value):
        self._data['color'] = value

    @property
    def line_type(self):
        return self._data.get('line_type')

    @line_type.setter
    def line_type(self, value: LineType):
        self._data['line_type'] = value

    @property
    def marker_shape(self):
        return self._data.get('shape')

    @marker_shape.setter
    def marker_shape(self, value: MarkerShape):
        self._data['shape'] = value

    @property
    def line_weight(self):
        return self._data.get('line_weight')

    @line_weight.setter
    def line_weight(self, value):
        self._data['line_weight'] = value

    @property
    def marker_weight(self):
        return self._data.get('marker_weight')

    @marker_weight.setter
    def marker_weight(self, value):
        self._data['marker_weight'] = value


class BoxStyle(AbstractStyle):
    def __init__(self):
        super().__init__()

    @property
    def show_mean(self):
        return self._data.get("mean", False)

    @show_mean.setter
    def show_mean(self, value):
        self._data["mean"] = value

    @property
    def mean_line(self):
        return self._data.get("mean_line", False)

    @mean_line.setter
    def mean_line(self, value):
        self._data["mean_line"] = value

    @property
    def vert(self):
        return self._data.get("vert", False)

    @vert.setter
    def vert(self, value):
        self._data["vert"] = value
