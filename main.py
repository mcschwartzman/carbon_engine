import numpy as np
import pylab

import carbon_engine

years = [2030, 2040, 2050,2060,2070,2080,2090,2100,2110,2120,2130,2140]
levels = [0.23, 0.33, 0.44, 0.56, 0.69, 0.82, 0.96, 1.12, 1.24, 1.39, 1.54, 1.69]

engine = carbon_engine.CarbonEngine(2)

# calculate year intervals to show with projection
last_year = years[-1]

test_year = 2150

additional_years = []

if (test_year > last_year):

    # make an array from the last year to the test year in increments of 10
    # append that array to the years array

    additional_years = list(range(last_year, test_year, 10))

# fitting
fit = np.polyfit(years, levels, 2)
projection = np.poly1d(fit)
projected_levels = projection(years + additional_years)


# plotting and showing
pylab.scatter(years, levels)
pylab.plot(years + additional_years, projected_levels)
pylab.show()


print(projection(test_year))