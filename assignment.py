import json
with open ("precipitation.json") as f:
    the_data = json.load(f)

#Station Code SEATTLE = GHCND:US1WAKG0038

#attempt = the_data[1]['station']
#print(attempt)

#Use station code to filter out Seattle
seattle = []
for station in the_data:
    station_id = station['station']
    if station_id == "GHCND:US1WAKG0038":
        seattle.append(station)
#print(seattle)
# Calculate total precipitation per month for location
# Use dates and split per month, and value per month

month_list = [0,0,0,0,0,0,0,0,0,0,0,0]
x = range(11)
month_num = []

for val_date in seattle: 
    #splitting date for sorting
    date = str(val_date['date'])
    date_split = date.split('-')
    month = int(date_split[1])
    month_list[month-1] += (val_date['value'])
  
with open ('results.json', 'w', encoding = 'utf-8') as file:
    json.dump(month_list, file, indent = 4)
    
    
    

#print(seattle)
#print(seattle_dates)

