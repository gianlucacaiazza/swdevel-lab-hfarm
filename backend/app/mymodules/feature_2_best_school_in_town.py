"""
Feature 2 - Best school in town

This function assesses schools based on services and amenities like cafeterias, gyms, and auditoriums, 
helping families in selecting the ideal school based on educational level and facilities.
"""

def best_school_in_town(data, city, school_level):


"""
Finding the school with the most services in a given city and school level

Parameters:
- data (DataFrame):the dataframe containing school data
- city (str): the city for which to find the school 
- school_level (str): the level of school (ex. 'primaria', 'secondaria primo grado')

Returns:
dict: a dictionary containing information about the school with the most services, 
including 'school name', 'services', 'service count'
If no data is available for the specified city or school level, 
return an informative message.
"""

filtered_data = data[(data['Denominazione Comune'] == city)
                     (data['Tipologia Scuola'] == school_level)]

if filtered_data.empty:
    return "No data available for the specific city and school level."

#Count the numer of services for each school
filtered_data['Service count'] = filtered_data[['Auditorium Aula Magna', 'Mensa', 'Palestra Piscina']].sum(axis=1)


#Sort the school by the number of services
filtered_data = filtered_data.sort_values(by='Service count', ascending=False)   

best_school = filtered_data.iloc[0]

return{
    'School Name': best_school['Denominazione Plesso Scolastico'],
    'Services':{
        'Auditorium Aula Magna': best_school['Auditorium Aula Magna'],
        'Mensa': best_school['Mensa'],
        'Palestra Piscina': best_school['Palestra Piscina']
    },
    'Service Count': best_school['Service Count']
}
