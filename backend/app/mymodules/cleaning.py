import pandas as pd
import numpy as np

schools_data = pd.read_csv('veneto.csv', encoding='ISO-8859-1')
# Remove useless columns
schools_data_cleaned = schools_data.drop (columns=["Codice Plesso Scolastico", "Codice ISTAT Comune", "Latitudine", "Longitudine", "Auditorium Aula Magna"])
