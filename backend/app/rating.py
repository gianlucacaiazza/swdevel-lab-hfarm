import pandas as pd
import ipywidgets as widgets
from IPython.display import display, clear_output
from rating_module import filter_wines_by_rating, mostra_dati

# Call the function filter_wines_by_rating to obtain the DataFrame all_wines.
all_wines = filter_wines_by_rating(['Red.csv', 'Rose.csv', 'Sparkling.csv', 'White.csv'])

# Create a list of unique wine types in the DataFrame.
wine_types_available = sorted(all_wines['Name'].unique())

# Widget FloatSlider for rating
rating_slider = widgets.FloatSlider(
    min=all_wines['Rating'].min(),
    max=all_wines['Rating'].max(),
    step=0.1,
    description='Select Rating:'
)

# Output widget to display results
output = widgets.Output()

# Implementation of the mostra_dati function directly in the code.
rating_slider.observe(mostra_dati(all_wines, output), names='value')

# Display the selection widget and the output
display(rating_slider, output)