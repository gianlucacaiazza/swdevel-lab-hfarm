import pandas as pd

def best_school_in_town(data, city, school_level):
    """
    Trova la scuola con il maggior numero di servizi in una città e un livello di scuola specificati.
    
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
    
    filtered_data = data[(data['Denominazione Comune'] == city) &
                         (data['Tipologia Scuola'] == school_level)]
    
    if filtered_data.empty:
        return "Nessun dato disponibile per la città e il livello di scuola specificato."
    
    # Calcola il numero di servizi per ciascuna scuola
    filtered_data['Service Count'] = filtered_data[['Auditorium Aula Magna', 'Mensa', 'Palestra Piscina']].sum(axis=1)
    
    # Ordina le scuole in base al numero di servizi
    filtered_data = filtered_data.sort_values(by='Service Count', ascending=False)
    
    best_school = filtered_data.iloc[0]
    
    return {
        'Nome Scuola': best_school['Denominazione Plesso Scolastico'],
        'Servizi': {
            'Auditorium Aula Magna': best_school['Auditorium Aula Magna'],
            'Mensa': best_school['Mensa'],
            'Palestra Piscina': best_school['Palestra Piscina']
        },
        'Conteggio servizi': best_school['Service Count']
    }