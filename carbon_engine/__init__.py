class CarbonEngine:

    slope = 0

    def __init__(self, slope):

        self.slope = slope

    def depth_at_year(self, year):

        return self.slope * year