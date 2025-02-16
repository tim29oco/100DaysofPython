# GOAL
# Use data to create a CSV
# Determine how many Gray, Cinnamon, and Black Squirrels there are
# Create a new CSV with the information


# Tim's Solution
# import pandas
#
# data = pandas.read_csv("squirrels.csv")
#
# squirrel_color_list = data["Primary Fur Color"].to_list()
# cinnamon = squirrel_color_list.count("Cinnamon")
# gray = squirrel_color_list.count("Gray")
# black = squirrel_color_list.count("Black")
#
# squirrel_dict = {
#     "Fur Color": ["gray", "cinnamon", "black"],
#     "Count": [gray, cinnamon, black]
# }
#
# new_data = pandas.DataFrame(squirrel_dict)
# new_data.to_csv("tims_code.csv")

# Angela's Solution

import pandas

data = pandas.read_csv("squirrels.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(f"Number of Gray Squirrels: {gray_squirrels_count}")
print(f"Number of Red Squirrels: {red_squirrels_count}")
print(f"Number of Black Squirrels: {black_squirrels_count}")

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("Tims_code.csv")