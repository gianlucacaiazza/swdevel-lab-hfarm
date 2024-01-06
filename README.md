#M.E.K.E README FILE

M.e.k.e software projectfor the Lab of Software porject development exam.

#What does our software consist of?

We used the CSV file provided to develop software that assists students in finding the school best suited to their specific needs. This tool analyzes data relating to schools in the Veneto region, allowing students to select an institution based on personalized criteria, such as school type, geographical location, and other relevant characteristics.

We used the details regarding the province, the number of services offered by each school and the city, contained in the CSV file.

From the main interface of our software, users can access a variety of services. Among these, there is the functionality that allows you to find the best school in a specific city, based on criteria such as the services offered. Additionally, you can search by filtering by the grade level of a school within a given province, making it easier to select primary, secondary or other level institutions in specific geographic areas.
Another important feature of the software is the ability to generate a list of schools based on the type of managing entity: public, private or religious. 

#Development of the application

#feature 1 
The function elenco_scuole_con_infrastrutture is designed to identify schools within a specified Italian province that have certain infrastructural facilities. This tool is particularly useful for educational administrators, policy makers, or researchers interested in analyzing the distribution and availability of school facilities such as cafeterias and sports facilities across different regions.

The function accepts three parameters:

data: A DataFrame representing the dataset of school information.
nome_provincia: A string representing the name of the province to be analyzed.
infrastrutture: A list of infrastructure facilities to look for in schools (e.g., 'Mensa' for cafeteria, 'Palestra Piscina' for gym and pool).

It filters the provided dataset to focus only on the schools located in the specified province.
The function then identifies schools that possess all of the listed infrastructural facilities.
If a non-existent province is entered, the function returns an error message indicating that the province does not exist in the dataset.

#feature 2 
