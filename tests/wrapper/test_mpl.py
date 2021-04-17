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

from unittest import TestCase

from autograph import create_plot, Plot
from autograph.core.style import TextStyle


class TestMPL(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self._plot: Plot = create_plot('matplotlib')

    def test_title(self):
        title = "title"
        self._plot.title = title
        self.assertEqual(self._plot._ax.get_title(), title)

    def test_x_label(self):
        title = "x"
        self._plot.x_label = title
        self.assertEqual(self._plot._ax.get_xlabel(), title)

    def test_y_label(self):
        title = "y"
        self._plot.y_label = title
        self.assertEqual(self._plot._ax.get_ylabel(), title)

    def test_lim(self):
        self._plot.x_lim = 0, 10
        self._plot.y_lim = 0, 10

        self.assertEqual(0, self._plot.x_min)
        self.assertEqual(10, self._plot.x_max)

        self.assertEqual(0, self._plot.y_min)
        self.assertEqual(10, self._plot.y_max)

        self.assertEqual((0, 10), self._plot.x_lim)
        self.assertEqual((0, 10), self._plot.y_lim)
