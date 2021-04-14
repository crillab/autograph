from unittest import TestCase

from plots import create_plot, Plot, MPL, create_plot_with_mpl


class Test(TestCase):
    def test_create_plot_by_name(self):
        plot = create_plot('matplotlib')
        self.assertTrue(type(plot).__name__ == MPL.__name__)

    def test_create_matplolib_plot(self):
        plot = create_plot_with_mpl()
        self.assertTrue(type(plot).__name__ == MPL.__name__)
