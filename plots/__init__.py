from plots.core.plot import Plot
from plots.wrapper.mpl import MPL
from plots.wrapper.plotly import Plotly


def create_plot_with_mpl() -> Plot:
    return MPL()


def create_plot_with_plotly() -> Plot:
    return Plotly()


def create_plot(name: str):
    print(Plot.__subclasses__())
    for elt in Plot.__subclasses__():
        if elt.name == name.lower():
            return globals()[elt.__name__]()
    raise ValueError(f'{name} is not a valid class')
