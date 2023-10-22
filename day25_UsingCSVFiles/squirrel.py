import pandas

data = pandas.read_csv("squirrel_census.csv")
fur_color = data["Primary Fur Color"].to_list()

# colors = []
# for color in fur_color:
#     if color not in colors:
#         colors.append(color)

color_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [0, 0, 0]
}

for color in fur_color:
    if color == "Gray":
        color_dict["Count"][0] += 1
    elif color == "Cinnamon":
        color_dict["Count"][1] += 1
    elif color == "Black":
        color_dict["Count"][2] += 1

result = pandas.DataFrame(color_dict)
result.to_csv("squirrel_report.csv")
print(result)
