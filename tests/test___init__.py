from unittest import TestCase

from plots import create_plot, MPL
from plots.wrapper.plotly import Plotly


class Test(TestCase):
    def test_create_plot_by_name(self):
        plot = create_plot('matplotlib')
        self.assertEqual(type(plot), MPL)

    def test_create_plotly_plot(self):
        plot = create_plot('plotly')
        self.assertEqual(type(plot), Plotly)
