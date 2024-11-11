class MBR:
    def __init__(self, x_min, y_min, x_max, y_max):
        self.xmin = x_min
        self.ymin = y_min
        self.xmax = x_max
        self.ymax = y_max

    def print(self):
        print(f"(xL,yL)=({self.xmin}, {self.ymin}) (xU,yU)=({self.xmax}, {self.ymax})")

    # Getters και setters με χρήση @property (προαιρετικά)
    @property
    def xmin(self):
        return self._xmin
    
    @property
    def xmax(self):
        return self._xmax
    
    @property
    def ymin(self):
        return self._ymin
    
    @property
    def ymax(self):
        return self._ymax

    @xmin.setter
    def xmin(self, value):
        self._xmin = value

    @xmax.setter
    def xmax(self, value):
        self._xmax = value

    @ymin.setter
    def ymin(self, value):
        self._ymin = value

    @ymax.setter
    def ymax(self, value):
        self._ymax = value