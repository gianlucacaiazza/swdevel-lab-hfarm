import pandas as pd
import json


def best_school_in_town(city: str, school_level: str, df):
    """
    Trova la scuola con il maggior numero di servizi in una città e un livello
    di scuola specificati.

    Parameters:
    - data (DataFrame): il DataFrame contenente i dati delle scuole
    - city (str): la città per cui trovare la scuola
    - school_level (str): il livello della scuola (es. 'primaria', 'secondaria primo grado')

    Returns:
    dict: un dizionario contenente informazioni sulla scuola con il maggior numero di servizi,
    inclusi 'Nome Scuola', 'Servizi', 'Conteggio servizi'.
    Se non ci sono dati disponibili per la città o il livello di scuola specificato,
    restituisce un messaggio informativo.
    """

    filtered_data = df[(df['Denominazione Comune'].str.lower() == city.lower()) &
                       (df['Tipologia Scuola'].str.lower() == school_level.lower())]
    
    if filtered_data.empty:
        return None

    # Calcola il numero di servizi per ciascuna scuola
    filtered_data['Service Count'] = filtered_data[['Spazi Didattici', 'Auditorium Aula Magna',
                                                    'Mensa', 'Palestra Piscina', 'Spazi Amministrativi']].sum(axis=1)
    
    # Ordina le scuole in base al numero di servizi
    filtered_data = filtered_data.sort_values(by='Service Count', ascending=False)
    
    best_schools = filtered_data[filtered_data['Service Count'] == filtered_data.iloc[0]['Service Count']]

    return best_schools
