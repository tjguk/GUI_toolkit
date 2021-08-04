# Layouts contain widgets such as buttons and text boxes
# Depending on the type of layout, widgets can be arranged in different ways
# The box layout allows for widgets to be stacked vertically or horizontally
import pygame

class BoxLayout:
    def __init__(self):
        self.mode = "horizontal"
        self.background_colour = (0, 0, 0)
        self.widget_border = 10
        self.padding = [0, 0, 0, 0]
        # padding = [header, footer, left_margin, right_margin]

        self._widgets = []
        self._num_widgets = 0
        self._widget_width = 0
        self._widget_height = 0
        self._widget_coords = []
        self._dimensions = [400, 600]
        self._position = [0, 0]
        self._layout_width = 0
        self._layout_height = 0
        
    def assign_dimensions(self, dimensions):
        """With the option of having multiple layouts on one screen, it must be the app.py 
        program that assigns the dimensions of the layout as the layout itself is unaware of
        other layouts"""
        
        self._dimensions = dimensions
        self._layout_width = self._dimensions[0]
        self._layout_height = self._dimensions[1]
        print("height", self._layout_height)

    def assign_position(self, position):
        """With the option of having multiple layouts on one screen, it must be the app.py
        program that assigns the position of the layout (based on the top left corner) as the layout
        itself is unaware of other layouts"""

        self._position = position
        print("coords", position)
        self._align()
        self._update_widgets()

    def add_widget(self, widget: object):
        self._widgets.append(widget)
        self._num_widgets += 1

    def _align(self):
        self._widget_coords = []
        self._layout_width -= (self.padding[2] + self.padding[3])
        self._layout_height -= (self.padding[0] + self.padding[1])
        print(self._position)

        if self._num_widgets > 0:
            if self.mode == "horizontal":
                self._widget_width = (self._layout_width - (self.widget_border * (self._num_widgets + 1))) / self._num_widgets
                self._widget_height = self._layout_height - (self.widget_border * 2)

                for i in range(len(self._widgets)):
                    x_coord = (self.padding[2] + (self.widget_border * (i + 1)) + (i * self._widget_width)) + self._position[0]
                    y_coord = (self.padding[0] + self.widget_border) + self._position[1]

                    self._widget_coords.append((x_coord, y_coord))

            elif self.mode == "vertical":
                self._widget_width = self._layout_width - (self.widget_border * 2)
                self._widget_height = (self._layout_height - (self.widget_border * (self._num_widgets + 1))) / self._num_widgets

                for i in range(len(self._widgets)):
                    x_coord = (self.padding[2] + self.widget_border) + self._position[0]
                    y_coord = (self.padding[0] + (self.widget_border * (i + 1)) + (i * self._widget_height)) + self._position[1]
                    self._widget_coords.append((x_coord, y_coord))

    def _update_widgets(self):
        for i, widget in enumerate(self._widgets):
            widget.assign_position(self._widget_coords[i])
            widget.assign_dimensions((self._widget_width, self._widget_height))

    def draw_background(self, surface):
        pygame.draw.rect(surface, self.background_colour, [self._position[0], self._position[1], self._dimensions[0], self._dimensions[1]])

    def provide_widgets(self):
        return self._widgets
        # return dict(zip(self._widgets, self._widget_coords))
