import json
with open ("precipitation.json") as f:
    the_data = json.load(f)

#PART 1
#Station Code SEATTLE = GHCND:US1WAKG0038

#Use station code to filter out Seattle
seattle = []
for station in the_data:
    station_id = station['station']
    if station_id == "GHCND:US1WAKG0038":
        seattle.append(station)
#print(seattle)
# Calculate total precipitation per month for location
# Use dates and split per month, and value per month

total_monthly_precipitation = [0,0,0,0,0,0,0,0,0,0,0,0]
x = range(11)
month_num = []

for val_date in seattle: 
    date = str(val_date['date'])
    date_split = date.split('-')
    month = int(date_split[1])
    total_monthly_precipitation[month-1] += (val_date['value'])

#PART2 - Total Yearly Precipitation
total_yearly_precipitation = sum(total_monthly_precipitation)

relative_monthly_precipitation = []
for monthly_precip in total_monthly_precipitation:
    relative_monthly_precipitation.append(monthly_precip/total_yearly_precipitation)

results = {
            "Seattle": {
                 "station": "GHCND:US1WAKG0038",
                 "state": "SE",
                 "total_monthly_precipitation": total_monthly_precipitation,
                 "total_yearly_precipitation": total_yearly_precipitation,
                 "relative_monthly_precipitation": relative_monthly_precipitation,
                 #"relative_yearly_precipitation": ...
            },
        }

with open('results.json', 'w') as file:
    json.dump(results, file, indent= 4)
