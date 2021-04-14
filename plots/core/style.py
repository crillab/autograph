from matplotlib import rcParams


class TextStyle:
    def __init__(self, size='larger', weight='bold',
                 color='auto', **kwargs):
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
        return self.location

    @property
    def y(self):
        return self._y
