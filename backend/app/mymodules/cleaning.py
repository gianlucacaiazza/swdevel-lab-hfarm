import pandas as pd

def load_and_clean_data(file_path):
    # Carica e pulisce i dati
    data = pd.read_csv(file_path, sep=';', header=0, encoding='ISO-8859-1')
    columns_to_drop = ["Codice Plesso Scolastico","Codice Edificio", "Edifici Attivo (SI-NO)", 
                   "Codice Istituzione Scolastica", "Codice ISTAT Comune", "Latitudine", "Longitudine" ]  # Elenco delle colonne da rimuovere
    data_cleaned = data.drop(columns=columns_to_drop)
    data_cleaned.fillna('Not found', inplace=True)
    data_cleaned.drop_duplicates(inplace=True)
    return data_cleaned