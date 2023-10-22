import pandas

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")


# data = pandas.read_csv("weather_data.csv")
# print(round(data["temp"].mean(), 2))
# print(data["temp"].max())
# print(data[data.temp == data.temp.max()])
# print(data[data.day == "Monday"].temp * 1.8 + 32)


# temp_list = data["temp"].to_list()
# print(round(sum(temp_list)/len(temp_list), 2))


# temp_sum = 0
# temp_count = 0
#
# for temp in temp_list:
#     temp_count += 1
#     temp_sum += temp
#
# temp_avg = round(temp_sum/temp_count, 2)
# print(temp_avg)
