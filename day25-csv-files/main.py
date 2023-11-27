

## Three Ways to Read CSV Files ##


# 1. Using "import csv"

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)


# 2. Using no imports

# with open("weather_data.csv") as raw_data:
#     lines = raw_data.readlines()
#     data = []
#     temperature = []
#     for line in lines[1:]:
#         stripped_line = line.strip()
#         line_data = stripped_line.split(",")
#         data.append(line_data)
#         temperature.append(int(line_data[1]))
#
# print(data)
# print(temperature)


# 3. Using "import pandas"

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# print(data)
# print(data["temp"])
