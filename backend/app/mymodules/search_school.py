import json

def schools_by_province(province, df):

	# Query per ricercare all'interno del csv tutti gli elementi che hanno
	# denominazione provincia = province (parametro passato in input)
	query = '`Denominazione Provincia` == "{}"'.format(province);

	# Eseguo la query e formatto l'output. Faccio la trasposta della
	# tabella, in modo da avere un output comodo da utilizzare.
	result = df.query(query).transpose()

	# Ritorno un json con i dati formattati.
	return { 'result': json.loads(result.to_json()) }
