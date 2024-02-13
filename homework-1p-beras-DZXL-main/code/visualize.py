import matplotlib.pyplot as plt
import numpy as np


def visualize_metrics(losses:list[float] =[], title: str =""):
    """
    param losses: a 1D array of loss values

    Displays a plot with loss values on the y-axis and batch number/epoch number on thex-axis
    """
    if not losses:
        return print("Must provide a list of losses to visualize")
    x = np.arange(1, len(losses) + 1)
    plt.plot(x, losses)
    plt.ylabel("Loss Value")
    plt.title(title)
    plt.show()