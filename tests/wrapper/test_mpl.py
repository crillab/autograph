from unittest import TestCase

from plots import create_plot


class TestMPL(TestCase):

    def setUp(self) -> None:
        super().setUp()
        create_plot('matplotlib')

    def test_title(self):
        self.fail()

    def test_title_style(self):
        self.fail()

    def test_title_position(self):
        self.fail()

    def test_x_label(self):
        self.fail()

    def test_y_label(self):
        self.fail()
