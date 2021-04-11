from plots.plot import Plot
import matplotlib.pyplot as plt


class MPL(Plot):

    def __init__(self):
        super().__init__()
        self._figure, self._ax = plt.subplot()

    @property
    def title(self):
        return super().title()

    @title.setter
    def title(self, value):
        super().title(value)
        self._ax.set_title(value)

    @property
    def title_style(self):
        return super().title_style()

    @title_style.setter
    def title_style(self, value):
        super().title_style(value)
        self._ax.set_title(self.title, )

    @property
    def title_position(self):
        return super().title_position()

    @property
    def x_label(self):
        return super().x_label()

    @x_label.setter
    def x_label(self, value):
        super().x_label(value)
        self._ax.set_xlabel(value)

    @property
    def y_label(self):
        return super().y_label()

    @y_label.setter
    def y_label(self, value):
        super().y_label(value)
        self._ax.set_ylabel(value)

    # def set_tile(self, label, fontdict=None, loc=None, pas=None, y=None, **kwargs):
    #     self.ax.set_title(label, fontdict, loc, pas, y, **kwargs)
    #
    # def set_xlabel(self, xlabel, fontdict=None, labelpad=None, loc=None, **kwargs):
    #     self.ax.set_xlabel(xlabel, fontdict, labelpad, loc, **kwargs)
    #
    # def set_ylabel(self, ylabel, fontdict=None, labelpad=None, loc=None, **kwargs):
    #     self.ax.set_ylabel(ylabel, fontdict, labelpad, loc, **kwargs)
    #
    # def legend(self, *args, **kwargs):
    #     self.ax.legend(*args, **kwargs)
    #
    # def set_xscale(self, values, **kwargs):
    #     self.ax.set_xscale(values, **kwargs)
    #
    # def set_yscale(self, values, **kwargs):
    #     self.ax.set_yscale(values, **kwargs)
    #
    # def save_figure(self, fname, dpi=None, facecolor='w', edgecolor='w', orientation='portrait',
    #                 papertype=None, format=None, transparent=False, bbox_inches=None,
    #                 pad_inches=0.1, frameon=None, metadata=None, **kwargs):
    #     self.figure.savefig(fname, dpi=dpi, facecolor=facecolor, edgecolor=edgecolor,
    #                         orientation=orientation,
    #                         papertype=papertype, format=format, transparent=transparent,
    #                         bbox_inches=bbox_inches,
    #                         pad_inches=pad_inches, frameon=frameon, metadata=metadata, **kwargs)
    #
    # def get_figure(self):
    #     return self.figure, self.ax
