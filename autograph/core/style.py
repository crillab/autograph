from matplotlib import rcParams

from autograph.core.enumstyle import LineType,  MarkerShape


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
