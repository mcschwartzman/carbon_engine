from carbon_engine.sea_level_analysis import model_sea_level
from carbon_engine.atmospheric_analysis import model_atmospheric_carbon

import numpy as np
import pylab

import carbon_engine

sea_level = model_sea_level(2100)
atmospheric_carbon = model_atmospheric_carbon(2100)

pylab.plot(sea_level[0], (sea_level[1] * 1000))
pylab.plot(atmospheric_carbon[0], atmospheric_carbon[1])

first_year = sea_level[0][0]
last_year = atmospheric_carbon[0][-1]
overlapping_years = list(range(first_year, last_year))
print(overlapping_years)

sea_level_overlapped = sea_level[2](overlapping_years)
sea_level_overlapped = sea_level_overlapped * 1000
print(sea_level_overlapped)

atmospheric_carbon_overlapped = atmospheric_carbon[2](overlapping_years)
print(atmospheric_carbon_overlapped)

ratios = []

for i in range(0, len(overlapping_years)):

    ratios.append(100 * (sea_level_overlapped[i] / atmospheric_carbon_overlapped[i]))

print(ratios)

pylab.grid(True)

pylab.plot(overlapping_years, ratios)

pylab.legend(['Sea Level Rise (mm)','Atmospheric Carbon (ppm)', 'Ratio (%)'])
pylab.title('Carbon Footprint - Sea Level Relationship')

pylab.show()