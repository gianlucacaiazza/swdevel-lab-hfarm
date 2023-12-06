import pandas as pd

def filter_wines_by_vintage(wine_files, vintage_min, vintage_max):
    """
    Filter wines based on a specified vintage range.

    Parameters:
    - wine_files: List of CSV file names related to different types of wines.
    - vintage_min: Desired minimum vintage.
    - vintage_max: Desired maximum vintage.

    Returns:
    - Pandas DataFrame with names and vintages of wines in the specified vintage range.
    """
    # DataFrame to store all data from CSV files
    all_wines = pd.DataFrame()

    # Concatenation of data from CSV files
    for wine_type in wine_files:
        all_wines = pd.concat([all_wines, pd.read_csv(wine_type)], ignore_index=True)

    # Convert "Year" column to numeric values, handling non-numeric values by setting them to NaN
    all_wines["Year"] = pd.to_numeric(all_wines["Year"], errors='coerce')

    # Select wines in the specified vintage range
    wines_chosen_vintage = all_wines[(all_wines["Year"] >= vintage_min) & (all_wines["Year"] <= vintage_max)]

    return wines_chosen_vintage[["Name", "Year"]]