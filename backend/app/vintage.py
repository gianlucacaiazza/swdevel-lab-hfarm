from vintage_modules import filter_wines_by_vintage

# List of CSV file names related to different types of wines
wines = ['Red.csv', 'Rose.csv', 'Sparkling.csv', 'White.csv']

# User input for the maximum and minimum vintage
vintage_max = float(input('Enter the maximum vintage: '))
vintage_min = float(input('Enter the minimum vintage: '))

# Call the function and print the results
result = filter_wines_by_vintage(wines, vintage_min, vintage_max)
print(result)