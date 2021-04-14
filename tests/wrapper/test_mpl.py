from unittest import TestCase

from plots import create_plot


class TestMPL(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self._plot = create_plot('matplotlib')

    def test_title(self):
        title = "title"
        self._plot.title = title
        self.assertEqual(self._plot._ax.get_title(), title)

    def test_title_style(self):
        self.fail()

    def test_title_position(self):
        self.fail()

    def test_x_label(self):
        title = "title"
        self._plot.title = title
        self.assertEqual(self._plot._ax.get_xlabel(), title)

    def test_y_label(self):
        title = "title"
        self._plot.title = title
        self.assertEqual(self._plot._ax.get_ylabel(), title)
