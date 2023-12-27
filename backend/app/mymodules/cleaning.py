import pandas as pd
import numpy as np

#bisogna seeparare il csv in colonne ordinate
veneto_data = pd.read_csv('veneto.csv', sep=';', header=0, encoding='ISO-8859-1')
print(veneto_data.head())
print(veneto_data.info())
print(veneto_data.describe())

# Remove useless columns
veneto_data_cleaned = veneto_data.drop (columns=["Codice Plesso Scolastico","Codice Edificio","Edifici Attivo (SI-NO)", "Codice Istituzione Scolastica","Codice ISTAT Comune", "Latitudine", "Longitudine", "Auditorium Aula Magna"])

# Fill missing values in 'Denominazione Plesso Scolastico' and 'Tipologia Scuola' with 'Not found'
veneto_data_cleaned['Denominazione Plesso Scolastico'].fillna('Not found', inplace=True)
veneto_data_cleaned['Tipologia Scuola'].fillna('Not found', inplace=True)

# Check for remaining missing values 
print(veneto_data_cleaned.isnull().sum())