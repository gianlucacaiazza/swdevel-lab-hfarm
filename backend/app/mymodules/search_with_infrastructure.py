
__possible_infrastructures = ["Spazi Didattici", "Auditorium Aula Magna", "Mensa", "Palestra Piscina", "Spazi Amministrativi"]

def search_with_infrastructure(province_name, infrastructure_name: str, df):
    
    # Verifica se la provincia esiste nel dataset
    if province_name.upper() not in df['Denominazione Provincia'].str.upper().unique():
        return None

    # Controlla se la lista delle infrastrutture è vuota
    if not infrastructure_name in __possible_infrastructures:
        return None

    # Filtra il dataset per il nome della provincia specificato
    with_province = df[df['Denominazione Provincia'].str.upper() == province_name.upper()]


    with_infrastructure = with_province[with_province[infrastructure_name] > 0]

    return with_infrastructure
    