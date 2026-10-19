import csv
with open("weather_data.csv",mode="r") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for index,row in enumerate(data):
        if index > 0:
            temperatures.append(int(row[1]))

    print(temperatures)

