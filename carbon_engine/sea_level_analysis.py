from carbon_engine.data_processing import get_columns



import numpy as np
import pylab

sea_level_file = '/home/mcschwartzman/git/carbon_engine/data/sea_level_decades.csv'

def model_sea_level(test_year):

    years = get_columns(sea_level_file, 0)
    years = [int(year) for year in years]
    
    sea_levels = get_columns(sea_level_file, 1)
    sea_levels = [float(level) for level in sea_levels]

    last_year = years[-1]

    additional_years = []

    if (test_year > last_year):

        additional_years = list(range(last_year, test_year, 10))

    projected_years = years + additional_years

    fit = np.polyfit(years, sea_levels, 2)
    projection = np.poly1d(fit)
    projected_sea_levels = projection(projected_years)

    return [projected_years, projected_sea_levels, projection, years, sea_levels]

