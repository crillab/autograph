from autograph.core.plot import Plot
from autograph.wrapper.mpl import MPL
from autograph.wrapper.plotly import Plotly



def create_plot(name: str):
    for elt in Plot.__subclasses__():
        if elt.name == name.lower():
            return globals()[elt.__name__]()
    raise ValueError(f'{name} is not a valid class')
