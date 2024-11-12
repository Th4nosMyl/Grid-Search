class MBR:
    # Constructor method to initialize the MBR object with minimum and maximum x and y values
    def __init__(self, x_min, y_min, x_max, y_max):
        self.xmin = x_min  # Set the minimum x value
        self.ymin = y_min  # Set the minimum y value
        self.xmax = x_max  # Set the maximum x value
        self.ymax = y_max  # Set the maximum y value

    # Method to print the MBR coordinates in a formatted string
    def print(self):
        print(f"(xL,yL)=({self.xmin}, {self.ymin}) (xU,yU)=({self.xmax}, {self.ymax})")

    # Getter for xmin using @property decorator
    @property
    def xmin(self):
        return self._xmin  # Return the minimum x value
    
    # Getter for xmax using @property decorator
    @property
    def xmax(self):
        return self._xmax  # Return the maximum x value
    
    # Getter for ymin using @property decorator
    @property
    def ymin(self):
        return self._ymin  # Return the minimum y value
    
    # Getter for ymax using @property decorator
    @property
    def ymax(self):
        return self._ymax  # Return the maximum y value

    # Setter for xmin using @property decorator
    @xmin.setter
    def xmin(self, value):
        self._xmin = value  # Set the minimum x value

    # Setter for xmax using @property decorator
    @xmax.setter
    def xmax(self, value):
        self._xmax = value  # Set the maximum x value

    # Setter for ymin using @property decorator
    @ymin.setter
    def ymin(self, value):
        self._ymin = value  # Set the minimum y value

    # Setter for ymax using @property decorator
    @ymax.setter
    def ymax(self, value):
        self._ymax = value  # Set the maximum y value