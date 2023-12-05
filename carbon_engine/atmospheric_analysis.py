from carbon_engine.data_processing import get_columns

import numpy as np
import pylab

annual_mean_atmospheric_co2_file = '/home/mcschwartzman/git/carbon_engine/data/co2_annmean_gl.csv'

def model_atmospheric_carbon(test_year):

    years = get_columns(annual_mean_atmospheric_co2_file, 0)
    years = [int(year) for year in years]

    co2_readings = get_columns(annual_mean_atmospheric_co2_file, 1)
    co2_readings = [float(reading) for reading in co2_readings]

    last_year = years[-1]

    additional_years = []

    if (test_year > last_year):

        additional_years = list(range(last_year, test_year, 1))

    projected_years = years + additional_years

    fit = np.polyfit(years, co2_readings, 2)
    projection = np.poly1d(fit)
    projected_co2_readings = projection(projected_years)

    return [projected_years, projected_co2_readings, projection, years, co2_readings]
