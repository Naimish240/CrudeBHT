class Quadrant:
    """
    A Quadrant describes a square region in space. In our two dimensional simulation, a quadrant
    has x and y coordinates for its center, as well as a diameter property that describes its width
    and height
    """
    def __init__(self, xmid: float, ymid: float, diameter: float):
        self.xmid = xmid
        self.ymid = ymid
        self.diameter = diameter

    def contains(self, xmid, ymid):
        """
        Check if this Quadrant contains a point
        """
        if (xmid <= self.xmid + self.diameter/2.0) and \
           (xmid >= self.xmid - self.diameter/2.0) and \
           (ymid <= self.ymid + self.diameter/2.0) and \
           (ymid >= self.ymid - self.diameter/2.0):
            return True
        return False

    def NW(self) -> 'Quadrant':
        return Quadrant(self.xmid - self.diameter / 4.0, self.ymid + self.diameter / 4.0, self.diameter / 2.0)

    def NE(self) -> 'Quadrant':
        return Quadrant(self.xmid + self.diameter / 4.0, self.ymid + self.diameter / 4.0, self.diameter / 2.0)

    def SW(self) -> 'Quadrant':
        return Quadrant(self.xmid - self.diameter / 4.0, self.ymid - self.diameter / 4.0, self.diameter / 2.0)

    def SE(self) -> 'Quadrant':
        return Quadrant(self.xmid + self.diameter / 4.0, self.ymid - self.diameter / 4.0, self.diameter / 2.0)