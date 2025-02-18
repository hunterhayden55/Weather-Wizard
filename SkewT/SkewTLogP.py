# Skew T Log P Chart made by Hunter Hayden 2/3/25
import numpy as np
import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import units
import numpy.ma as ma

# Sample data for temperature, dew point, and pressure
# INPUT Pressure, Temperature, Dewpoint HERE
##########################################################
pressure = np.array([864.0, 855.0, 850.0, 750.0, 738.0, 708.0, 700.0, 655.0, 625.0, 615.0, 608.0, 592.0, 558.0, 556.0, 541.0, 521.0, 519.0, 501.0, 500.0, 492.0, 487.0, 472.0, 443.0, 434.0, 431.0, 411.0, 400.0, 395.0, 389.0, 371.0, 369.0, 364.0, 345.0, 320.0, 300.0, 296.0, 283.0, 250.0, 246.0, 224.0, 210.0, 200.0, 194.0, 172.0, 162.0, 150.0, 149.0, 137.0, 133.0, 124.0, 101.0, 100.0, 70.0, 50.0]) * units.hPa
temperature = np.array([35.2, 31.6, 31.2, 20.5, 19.1, 15.6, 14.6, 9.4, 5.7, 4.4, 3.6, 1.7, -2.5, -2.7, -3.1, -5.3, -5.6, -8.2, -8.3, -9.1, -8.9, -10.0, -12.2, -12.9, -13.1, -16.3, -18.1, -18.9, -19.9, -22.9, -23.3, -22.9, -25.8, -29.9, -33.1, -33.8, -36.0, -42.3, -43.1, -48.1, -51.1, -53.3, -54.5, -58.9, -61.3, -64.3, -64.5, -67.0, -67.9, -71.1, -80.5, -80.5, -72.7, -61.3]) * units.degC
dewpoint = np.array([1.2, -10.4, -8.8, -7.9, -7.8, -7.5, -7.4, -8.0, -8.4, -8.6, -9.2, -10.5, -13.5, -13.7, -25.1, -31.3, -31.3, -31.3, -31.3, -34.1, -43.9, -42.2, -38.6, -37.5, -37.1, -36.5, -36.1, -35.8, -35.5, -34.4, -34.3, -27.9, -30.1, -33.1, -37.6, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]) * units.degC
##########################################################


# Mask the missing dew point values
dewpoint = ma.masked_invalid(dewpoint)

# Create a new figure
fig = plt.figure(figsize=(9, 9))
skew = SkewT(fig)

# Plot the data and change width and colors
skew.plot(pressure, temperature, 'r', linewidth=2)
skew.plot(pressure, dewpoint, 'y', linewidth=2)

# Add the relevant lines
#skew.plot_dry_adiabats(linewidth=0.5, pressure=np.linspace(1000, 50, 20) * units.hPa)
skew.plot_dry_adiabats(t0=np.arange(-50, 300, 10) * units.degC, linewidth=0.5)
skew.plot_moist_adiabats(linewidth=0.5, pressure=np.linspace(1000, 50, 20) * units.hPa)

# Define the mixing ratios
mixing_ratios = np.array([0.4, 1, 2, 4, 8, 16]) * units('g/kg')

# Plot the mixing ratio lines
skew.plot_mixing_lines(mixing_ratios, pressure=np.linspace(1000, 50, 20) * units.hPa, linewidth=0.5)

# Add mixing ratio labels manually

skew.ax.text(-28, 1000, str(mixing_ratios[0].magnitude) + " g/kg", fontsize=6, verticalalignment='bottom')
skew.ax.text(-18, 1000, str(mixing_ratios[1].magnitude) + " g/kg", fontsize=6, verticalalignment='bottom')
skew.ax.text(-9, 1000, str(mixing_ratios[2].magnitude) + " g/kg", fontsize=6, verticalalignment='bottom')
skew.ax.text(0, 1000, str(mixing_ratios[3].magnitude) + " g/kg", fontsize=6, verticalalignment='bottom')
skew.ax.text(10, 1000, str(mixing_ratios[4].magnitude) + " g/kg", fontsize=6, verticalalignment='bottom')
skew.ax.text(21, 1000, str(mixing_ratios[5].magnitude) + " g/kg", fontsize=6, verticalalignment='bottom')

# Set the limits for the plot
skew.ax.set_ylim(1000, 50)
skew.ax.set_xlim(-40, 50)

# Add gridlines
skew.ax.grid(True)

# Label the axes
skew.ax.set_xlabel('Temperature (°C)')
skew.ax.set_ylabel('Pressure (hPa)')

# Show the plot
plt.show()
