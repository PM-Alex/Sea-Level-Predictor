import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df_a = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df_a['Year'], df_a['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    linear_a = linregress(df_a['Year'], df_a['CSIRO Adjusted Sea Level'])
    plt.plot(range(1880, 2051, 1), linear_a.slope * range(1880, 2051, 1) + linear_a.intercept)

    # Create second line of best fit
    df_b = df_a[df_a['Year'] >= 2000]
    linear_b = linregress(df_b['Year'], df_b['CSIRO Adjusted Sea Level'])
    plt.plot(range(2000, 2051, 1), linear_b.slope * range(2000, 2051, 1) + linear_b.intercept)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()