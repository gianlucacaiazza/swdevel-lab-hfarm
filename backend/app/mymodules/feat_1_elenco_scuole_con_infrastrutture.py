import pandas as pd

# Carico il dataset
file_path = '/M.E.K.E-Group/backend/app/veneto.csv'
data = pd.read_csv(file_path, delimiter=';')

# Selezione delle colonne rilevanti e creazione del DataFrame personalizzato
colonne_rilevanti = ['Denominazione Provincia', 'Mensa', 'Palestra Piscina']
data_personalizzato = data[colonne_rilevanti]

def elenco_scuole_con_infrastrutture(data, nome_provincia, infrastrutture):
    colonne_base = ['Denominazione Comune', 'Denominazione Plesso Scolastico', 'Tipologia Scuola']
    
    # Verifica se la provincia esiste nel dataset
    if nome_provincia.upper() not in data['Denominazione Provincia'].str.upper().unique():
        return "Errore: provincia non esistente."

    # Controlla se la lista delle infrastrutture è vuota
    if not infrastrutture:
        return "Errore: nessuna infrastruttura specificata."

    # Filtra il dataset per il nome della provincia specificato
    data_provincia = data[data['Denominazione Provincia'].str.upper() == nome_provincia.upper()]

    # Filtra per infrastrutture
    for infrastruttura in infrastrutture:
        if infrastruttura not in data.columns:
            return f"Errore: colonna '{infrastruttura}' non presente nel dataset."
        data_provincia = data_provincia[data_provincia[infrastruttura] > 0]
        
    # Controlla se ci sono scuole rimanenti dopo il filtraggio
    if data_provincia.empty:
        return "Nessuna scuola trovata con le infrastrutture specificate nella provincia data."

        
    # Unione delle colonne rilevanti
    colonne_rilevanti = colonne_base + infrastrutture
    scuole_selezionate = data_provincia[colonne_rilevanti].drop_duplicates()

    return scuole_selezionate
