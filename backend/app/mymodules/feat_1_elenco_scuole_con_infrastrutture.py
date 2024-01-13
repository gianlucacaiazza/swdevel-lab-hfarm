def elenco_scuole_con_infrastrutture(data, nome_provincia, infrastrutture):
    
    # Verifica se la provincia esiste nel dataset
    if nome_provincia.upper() not in data['Denominazione Provincia'].str.upper().unique():
        return "Errore: provincia non esistente."

    # Filtra il dataset per il nome della provincia specificato
    data_provincia = data[data['Denominazione Provincia'].str.upper() == nome_provincia.upper()]

    # Filtra per infrastrutture
    for infrastruttura in infrastrutture:
        data_provincia = data_provincia[data_provincia[infrastruttura] > 0]

    # Selezione delle colonne rilevanti
    colonne_rilevanti = ['Denominazione Comune', 'Denominazione Plesso Scolastico', 'Tipologia Scuola'] + infrastrutture
    scuole_selezionate = data_provincia[colonne_rilevanti].drop_duplicates()

    return scuole_selezionate
