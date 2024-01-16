def list_provinces(df):
	unique =  df.get('Denominazione Provincia').unique()
	return [x for x in unique if x]

def list_cities(df):
	unique = df.get('Denominazione Comune').unique()
	return [x for x in unique if x]

def list_school_types(df):
	unique =  df.get('Tipologia Scuola').unique()
	return [x for x in unique if x]