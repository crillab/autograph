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

from autograph.core.enumstyle import LineType, MarkerShape, Position


class LegendStyle:
    def __init__(self):
        self._data = {}

    @property
    def position(self):
        return self._data.get('position', Position.BOTTOM)

    @position.setter
    def position(self, value):
        self._data['position'] = value

    @property
    def n_col(self):
        return self._data.get('n_col', 1)

    @n_col.setter
    def n_col(self, value):
        self._data['n_col'] = value

    @property
    def title(self):
        return self._data.get('title', None)

    @title.setter
    def title(self, value):
        self._data['title'] = value


class TextStyle:
    def __init__(self, size='larger', weight='bold',
                 color=None, **kwargs):
        self._size = size
        self._weight = weight
        self._color = color

    @property
    def size(self):
        return self._size

    @property
    def weight(self):
        return self._weight

    @property
    def color(self):
        return self._color


class TextPosition:
    def __init__(self, pad=6.0, location='center', y=None):
        """

        :param pad: pad between axes and text in points
        :param location: alignment of the text: {left, right, center}
        :param y: position text (axes relative units).  None implies auto
        """
        self._pad = pad
        self._location = location
        self._y = y

    @property
    def pad(self):
        return self._pad

    @property
    def location(self):
        return self._location

    @property
    def y(self):
        return self._y


class PlotStyle:
    def __init__(self):
        self._data = {}

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
