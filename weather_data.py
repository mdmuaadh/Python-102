# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name:Muaadh Mohideen
# Section:ENGR 102-559
# Assignment:Lab 11 Individual
# Date:11/02/2025

import csv

def weather_data():
    all_rows =[]
    max_temperature_overall=float("-inf")
    min_temperature_overall=float("inf")

    with open("WeatherDataCLL.csv", "r") as file_handle:
        reader =csv.DictReader(file_handle)
        for row_data in reader:
            all_rows.append(row_data)
            max_cell_text=(row_data.get("Maximum Temperature (F)") or "").strip()
            min_cell_text=(  row_data.get("Minimum Temperature (F)") or "").strip()
            if max_cell_text:
                try:
                    max_value =float(max_cell_text)
                    if max_value> max_temperature_overall:
                        max_temperature_overall =max_value
                except ValueError:
                    pass

            if min_cell_text:
                try:
                    min_value = float(min_cell_text)
                    if min_value < min_temperature_overall:
                        min_temperature_overall = min_value
                except ValueError:
                    pass

    print(f"10-year maximum temperature: {int(round(max_temperature_overall))} F")
    print(f"10-year minimum temperature: {int(round(min_temperature_overall))} F")
    print()

    # inputs
    try:
        # month input
        month_input =input("Please enter a month: ").strip()
        month_map = {
            "january":1,"february":2,"march":3,"april":4,"may":5,"june":6,
            "july":7,"august":8,"september":9,"october":10,"november":11,"december":12
        }
        if month_input.isdigit():
            month_number = int(month_input)
            # keep a nicely formatted month name for printing
            month_name = [m for m,n in month_map.items() if n == month_number][0].title() if 1 <= month_number <= 12 else None
        else:
            key = month_input.lower()
            month_number = month_map.get(key, 0)
            month_name = key.title() if month_number else None

        year_number = int(input("Please enter a year: ").strip())
        if not (1 <= month_number <= 12):
            raise ValueError
    except ValueError:
        print("Invalid month or year.")
        return
    print()

    #rows for month and year
    rows_for_month= []
    for row_data in all_rows:
        date_text = (row_data.get("Date") or "").strip()
        parts = date_text.split("/")
        if len(parts) !=3:
            continue
        try:
            month_in_row = int(parts[0])
            year_in_row  = int(parts[2])
        except ValueError:
            continue
        if month_in_row == month_number and year_in_row == year_number:
            rows_for_month.append(row_data)

    if not rows_for_month:
        print("No data available for the specified month and year.")
        return

    # summation and counting for it 
    pressure_sum =wet_bulb_sum = avg_temp_sum = dew_point_sum = rh_sum = wind_speed_sum = 0.0
    pressure_count =wet_bulb_count =avg_temp_count = dew_point_count = rh_count = wind_speed_count = 0
    precip_day_count =0
    observed_day_count =0

    for day_row in rows_for_month:
        observed_day_count += 1
        if day_row["Average Pressure (in Hg)"] and day_row["Average Pressure (in Hg)"].strip():
            try:
                pressure_sum += float(day_row["Average Pressure (in Hg)"])
                pressure_count += 1
            except ValueError:
                pass
        if day_row["Average Wet Bulb Temperature (F)"] and day_row["Average Wet Bulb Temperature (F)"].strip():
            try:
                wet_bulb_sum += float(day_row["Average Wet Bulb Temperature (F)"])
                wet_bulb_count += 1
            except ValueError:
                pass
        if day_row["Average Temperature (F)"] and day_row["Average Temperature (F)"].strip():
            try:
                avg_temp_sum += float(day_row["Average Temperature (F)"])
                avg_temp_count += 1
            except ValueError:
                pass
        if day_row["Average Dew Point (F)"] and day_row["Average Dew Point (F)"].strip():
            try:
                dew_point_sum += float(day_row["Average Dew Point (F)"])
                dew_point_count += 1
            except ValueError:
                pass
        if day_row["Average Relative Humidity (%)"] and day_row["Average Relative Humidity (%)"].strip():
            try:
                rh_sum += float(day_row["Average Relative Humidity (%)"])
                rh_count += 1
            except ValueError:
                pass
        if day_row["Average Daily Wind Speed (mph)"] and day_row["Average Daily Wind Speed (mph)"].strip():
            try:
                wind_speed_sum += float(day_row["Average Daily Wind Speed (mph)"])
                wind_speed_count += 1
            except ValueError:
                pass
        if day_row["Precipitation (in)"] and day_row["Precipitation (in)"].strip():
            try:
                if float(day_row["Precipitation (in)"]) > 0:
                    precip_day_count+= 1
            except ValueError:
                pass

  #calcualte means
    if pressure_count>0:pressure_mean = pressure_sum / pressure_count
    else:                  pressure_mean = 0.0
    if avg_temp_count>0: average_temperature_mean = avg_temp_sum / avg_temp_count
    else:                  average_temperature_mean = 0.0
    if wet_bulb_count>0: wet_bulb_mean = wet_bulb_sum / wet_bulb_count
    else:                  wet_bulb_mean = 0.0
    if dew_point_count>0: dew_point_mean = dew_point_sum / dew_point_count
    else:                    dew_point_mean = 0.0
    if rh_count> 0: relative_humidity_mean = rh_sum / rh_count
    else:            relative_humidity_mean = 0.0
    if wind_speed_count>0: wind_speed_mean = wind_speed_sum / wind_speed_count
    else:                    wind_speed_mean = 0.0
    if observed_day_count> 0:precipitation_percent = (precip_day_count / observed_day_count) * 100.0
    else:                      precipitation_percent = 0.0

    # print results 
    print(f"For {month_name} {year_number}:")
    print(f"Mean average daily pressure: {pressure_mean:.2f} in Hg")
    print(f"Mean average daily temperature: {average_temperature_mean:.1f} F")
    print(f"Mean average daily wet bulb temperature: {wet_bulb_mean:.1f} F")
    print(f"Mean average daily dew point: {dew_point_mean:.1f} F")
    print(f"Mean average daily relative humidity: {relative_humidity_mean:.1f}%")
    print(f"Mean average daily wind speed: {wind_speed_mean:.2f} mph")
    print(f"Percentage of days with precipitation: {precipitation_percent:.1f}%")

weather_data()