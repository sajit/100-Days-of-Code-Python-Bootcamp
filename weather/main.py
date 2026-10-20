# import csv
# with open("weather_data.csv",mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for index,row in enumerate(data):
#         if index > 0:
#             temperatures.append(int(row[1]))

#     print(temperatures)

from panda_file_help import get_weather_data_as_dict, get_weather_data

weather_data = get_weather_data_as_dict()
temp_list = weather_data['temp'].values()
avg_temp = sum(temp_list)/len(temp_list)
print(f"Average temp {avg_temp}")
max_temp = max(temp_list)
print(f"Max temp {max_temp}")
wd_df =get_weather_data()
print(wd_df[wd_df['day'] == "Monday"])
mt_day = wd_df[wd_df['temp'] == max_temp]
print(f"Max temp on {mt_day.day}")



