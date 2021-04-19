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

from autograph.core.plot import Plot
from autograph.wrapper.mpl import MPL
from autograph.wrapper.plotly import Plotly


def create_plot(name: str):
    for elt in Plot.__subclasses__():
        if elt.name == name.lower():
            return globals()[elt.__name__]()
    raise ValueError(f'{name} is not a valid class')


__all__ = [
    '__title__',
    '__summary__',
    '__uri__',
    '__version__',
    '__author__',
    '__email__',
    '__license__',
    '__copyright__',
]

__title__ = 'autograph'
__summary__ = 'AUtogRAPH - A Unified libRary for drAwing Plots in pytHon'
__keywords__ = 'visualization plots'
__uri__ = 'https://github.com/crillab/autograph'
__version__ = '0.1.0-rc3'
__author__ = 'Thibault Falque, Romain Wallon, Hugues Wattez'
__email__ = 'thibault.falque@exakis-nelite.com, wallon@lix.polytechnique.fr, wattez@cril.fr'

__license__ = 'MIT'
__copyright__ = '2021-2022 - Univ Artois & CNRS, Exakis Nelite'
