from plots.core.plot import Plot
import matplotlib.pyplot as plt

from plots.core.style import TextStyle, TextPosition


class MPL(Plot):
    name = "matplotlib"

    def __init__(self):
        super().__init__()
        self._figure, self._ax = plt.subplots()
        self.title_style = TextStyle()
        self.title_position = TextPosition()

    def __change_title(self):
        if self.title is None:
            return

        self._ax.set_title(self.title, fontdict={
            'fontsize': self.title_style.size,
            'fontweight': self.title_style.weight,
            'color': self.title_style.color,
        }, loc=self.title_position.location, pad=self.title_position.pad, y=self.title_position.y)

    @Plot.title.setter
    def title(self, value):
        super().title = value
        self.__change_title()

    @Plot.title_position.setter
    def title_position(self, value):
        super().title_position = value
        self.__change_title()

    @Plot.x_label.setter
    def x_label(self, value):
        super().x_label = value
        self._ax.set_xlabel(value)

    @Plot.y_label.setter
    def y_label(self, value):
        super().y_label = value
        self._ax.set_ylabel(value)
