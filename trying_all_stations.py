#make a dictionary
sth = {
    'name of station': [0] * 12
    'name': [0] * 12
}
#what teun did, and what you can try!!! 
for measurement in precipitation_data:
    date_split = measurement ['date'].split('-')
    month = int(date_split[1])
    totals[measurement['station']][month-1] += measurement['value']