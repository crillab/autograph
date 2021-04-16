from enum import Enum, auto


class EnumStyle(Enum):
    def __init__(self, mpl_string, plotly_string):
        self._mpl_string = mpl_string
        self._plotly_string = plotly_string

    @property
    def mpl_string(self):
        return self._mpl_string

    @property
    def plotly_string(self):
        return self._plotly_string

    @classmethod
    def all_mpl_strings(cls):
        for s in cls:
            yield s.mpl_string

    @classmethod
    def all_plotly_strings(cls):
        for s in cls:
            yield s.plotly_string


class LineType(EnumStyle):
    SOLID = "-", None
    DASH = "--", "dash"
    DOT = ":", "dot"
    DASH_DOT = "-.", "dashdot"


class MarkerShape(EnumStyle):
    CIRCLE = "o", "circle"
    SQUARE = ",", "square"
    TRIANGLE_DOWN = "v", "triangle-down"
    TRIANGLE_UP = "^", "triangle-up"
    TRIANGLE_LEFT = "<", "triangle-left"
    TRIANGLE_RIGHT = ">", "triangle-right"
    PLUS = "P", "cross"
    PLUS_THIN = "+", "cross-thin"


class Position(Enum):
    TOP = auto()
    LEFT = auto()
    RIGHT = auto()
    BOTTOM = auto()
