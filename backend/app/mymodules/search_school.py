import json

def schools_by_province(province: str, df):

	# Query per ricercare all'interno del csv tutti gli elementi che hanno
	# denominazione provincia = province (parametro passato in input)

	# Eseguo la query e formatto l'output. Faccio la trasposta della
	# tabella, in modo da avere un output comodo da utilizzare.
	result = df[df['Denominazione Provincia'].str.lower() == province.lower()].transpose()

	# Ritorno un json con i dati formattati.
	return { 'result': json.loads(result.to_json()) }
