from IPython.display import display, clear_output
import ipywidgets as widgets
import pandas as pd

def filter_wines_by_rating(wine_files):
    all_wines = pd.DataFrame()

    # Concatenation of data from CSV files
    for wine_type in wine_files:
        all_wines = pd.concat([all_wines, pd.read_csv(wine_type)], ignore_index=True)

    return all_wines

def mostra_dati(all_wines, output):
    def handler(change):
        with output:
            clear_output(wait=True)
            rating_selezionato = change.new
            risultato = all_wines[all_wines['Rating'] == rating_selezionato][['Name', 'Rating']]
            display(risultato)
    return handler