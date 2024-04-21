import pyqtgraph as pg
from PyQt6.QtGui import QColor
import pandas as pd
import numpy as np


class Signal:
    """
    The Signal class represents a signal with various attributes and methods for manipulation.

    Attributes:
        id (int): A unique identifier for each instance of the class.
        colors (list): A list of color codes represented as strings for visualization.
        name (str): The name of the signal.
        state (tuple): A tuple representing the current state of the signal.
        x (list): A list of x-coordinates for the signal data.
        y (list): A list of y-coordinates for the signal data.
        color (str): The color used to visualize the signal.
        pen (object): A pen object used for graphical rendering.
        key (str): A unique key for the signal based on its name and ID.
        is_visible (bool): A flag indicating whether the signal is currently visible.

    Methods:
        __init__(self, name):
            Initializes a new instance of the Signal class.

        change_handler(self, handlerId):
            Changes the handler ID associated with the signal.

        change_title(self, title):
            Changes the title of the signal.

        change_color(self, color):
            Changes the color used to visualize the signal.

        toggle_show(self):
            Toggles the visibility of the signal.

        update_state(self, state):
            Updates the state of the signal with new data.
    """

    id = 0  # Class variable to maintain unique IDs for instances
    colors = [
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf",
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf",
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf",
    ]

    def __init__(self, name):
        """
        Initializes a new instance of the Signal class.

        Args:
            name (str): The name of the signal.
        """
        self.toggle_presses = 0
        Signal.id += 1  # Increment the class variable for a unique ID
        self.toggle_presses = 0
        self.id = Signal.id  # Assign the unique ID to the instance
        self.handler = -1
        self.timer = None
        self.tempColor = "#ffffff"
        self.name = name
        self.state = (None, None)  # Initialize state as a tuple (x, y)
        self.popped_x_vals, self.popped_y_vals = [], []
        self.x = list(
            np.arange(0, 20, 0.0025)
        )  # Generate x-coordinates as a list from 0 to 999
        self.y = [
            np.random.randint(-4, 5) for i in range(1000)
        ]  # Generate random y-coordinates
        self.color = Signal.colors[
            self.id
        ]  # Assign a color from the class variable 'colors'

        self.pen = pg.mkPen(
            color=self.color
        )  # Create a pen object for graphical rendering
        self.key = self.name + str(
            self.id
        )  # Generate a unique key based on name and ID
        self.is_visible = True  # Initialize visibility flag as False

    def change_handler(self, handlerId):
        self.handler = handlerId

    def set_x_vals(self, x_values):
        self.x = list(x_values)

    def set_y_vals(self, y_values):
        self.y = list(y_values)

    def change_title(self, title):
        """
        Changes the title of the signal.

        Args:
            title (str): The new title for the signal.
        """
        self.name = title  # Set the title attribute to the provided value

    def change_color(self, color):
        """
        Changes the color used to visualize the signal.

        Args:
            color (str): The new color code for the signal.
        """
        self.color = color  # Update the color attribute with the provided color
        self.pen.setColor(QColor(color))

    def toggleShow(self):
        """
        Toggle the visibility of an element and change its color based on the number of times it's been toggled.

        This function increments the `toggle_presses` attribute by 1, changes the element's color to transparent (#00000000),
        and, if the number of toggle presses is even, changes the color to the element's original color.

        Args:
            self (object): The instance of the class containing this method.

        Returns:
            None
        """
        # print("here")
        self.toggle_presses += 1
        self.change_color("#00000000")
        if self.toggle_presses % 2 == 0:
            self.change_color(Signal.colors[self.id])
        return self.toggle_presses % 2 == 0

    def isVisible(self):
        return self.toggle_presses % 2 == 0

    def update_state(self, state):
        """
        Updates the state of the signal with new data.

        Args:
            state (tuple): A tuple representing the new state data (x, y).
        """
        self.state = state  # Update the state attribute with the provided state data
