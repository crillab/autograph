from unittest import TestCase

from plots import create_plot, Plot
from plots.core.style import TextStyle


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
