# Tutorial

## Introduction 

AUtogRAPH is a unified library for creating static and interactive visualization in Python. T
It offers a unique simplified interface for creating graphics. 
It currently manages two libraries in the background: [Matplotlib](https://github.com/matplotlib/matplotlib)
and [Plotly](https://github.com/plotly/plotly.py). New libraries will be added gradually. 


## Installation 

To execute *Autograph* on your computer, you first need to install
[Python](https://www.python.org/downloads/) on your computer
(at least version 3.8).

As the `autograph` library is
[available on PyPI](https://pypi.org/project/crillab-autograph/), you install it
using `pip`.

```bash
pip install crillab-autograph
```

Note that, depending on your Python installation, you may need to use `pip3`
to install it, or to execute `pip` as a module, as follows.

```bash
python3 -m pip install crillab-autograph
```

## Create plot 

With *autograph* you can create graphics from a single interface, you just 
need to specify the name of the backend (e.g. the library) that will 
generate the graphics:

```python
from autograph import create_plot
plot = create_plot("matplotlib") # plotly is also possible
```

## Customize plot 

### Title and style of title 

For specify the title of your plot, you just have to use the `title` property. 

```python
plot.title="My awesome plot"
```

If you want customize the font, the color, the weight or the size you can use 
the `TextStyle` class :

```python
from autograph.core.style import TextStyle
from autograph.core.enumstyle import FontWeight
plot.title_style=TextStyle()
plot.title_style.font_name="Arial"
plot.title_style.size=12
plot.title_style.color="red"
plot.title_style.weight=FontWeight.BOLD
```


### Axis

```python
plot.x_label="X"
```

```python 
plot.x_label_style=TextStyle()
plot.x_label_style.font_name="Arial"
plot.x_label_style.size=10
plot.x_label_style.color="blue"
plot.x_label_style.weight=FontWeight.N_100
```

It is possible to do the same thing for the y-axis by using the `y_label` 
and `y_label_style` properties.