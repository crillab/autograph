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


class FontWeight(EnumStyle):
    BOLD = "bold", "<span style='font-weight:bold'>{}</span>"
    NORMAL = "normal", "<span style='font-weight:normal'>{}</span>"
    N_100 = 100, "<span style='font-weight:100'>{}</span>"
    N_200 = 200, "<span style='font-weight:200'>{}</span>"
    N_300 = 300, "<span style='font-weight:300'>{}</span>"
    N_400 = 400, "<span style='font-weight:400'>{}</span>"
    N_600 = 600, "<span style='font-weight:600'>{}</span>"
    N_800 = 800, "<span style='font-weight:800'>{}</span>"
    N_900 = 900, "<span style='font-weight:900'>{}</span>"


class Position(Enum):
    TOP = auto()
    LEFT = auto()
    RIGHT = auto()
    BOTTOM = auto()
