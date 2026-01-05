"""
Project: Pet Adoption Data Analysis
Goal: Analyze adoption trends to understand which animals are adopted most often,
their average age, and the time taken for adoption.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("pets.csv")

# Before Cleaning
print("Null values before cleaning:")
print(data.isnull().sum())

# After Cleaning
print("Rows after cleaning:", len(data))

# Data Cleaning
print("Duplicate rows:", data.duplicated().sum())
data.duplicated().sum()
data.drop_duplicates(inplace=True)
print("Rows after cleaning:", len(data), "\n")


animals_sorted = data.sort_values(by="Animal", ascending=True)

animals = ["Dog", "Cat", "Bunny", "Fish", "Bird"]

sum_by_animal = data.groupby("Animal").size().reindex(animals)
print(sum_by_animal)
totals = sum_by_animal.tolist()
print(totals)

plt.bar(animals, totals)
plt.xlabel("Animals")
plt.ylabel("Total Number of Pets adopted")
plt.title("Animals Adopted")
plt.show()


# Calculates the averages

# Finds the Averages for each pet
average_dogs = data[data["Animal"] == "Dog"]["Age"].mean().round(2)
average_cats = data[data["Animal"] == "Cat"]["Age"].mean().round(2)
average_bunnies = data[data["Animal"] == "Bunny"]["Age"].mean().round(2)
average_fish = data[data["Animal"] == "Fish"]["Age"].mean().round(2)
average_birds = data[data["Animal"] == "Bird"]["Age"].mean().round(2)
averages = [
    int(average_dogs),
    int(average_cats),
    int(average_bunnies),
    int(average_fish),
    int(average_birds),
]

plt.bar(animals, averages)
plt.xlabel("Animals")
plt.ylabel("Average Amount of Animals Adopted")
plt.title("Average for Animals Adopted")
plt.show()


time_dogs = data[data["Animal"] == "Dog"]["Days in Adoption Center"].mean().round(2)
time_cats = data[data["Animal"] == "Cat"]["Days in Adoption Center"].mean().round(2)
time_bunnies = (
    data[data["Animal"] == "Bunny"]["Days in Adoption Center"].mean().round(2)
)
time_fish = data[data["Animal"] == "Fish"]["Days in Adoption Center"].mean().round(2)
time_birds = data[data["Animal"] == "Bird"]["Days in Adoption Center"].mean().round(2)
days = [
    int(time_dogs),
    int(time_cats),
    int(time_bunnies),
    int(time_fish),
    int(time_birds),
]
plt.bar(animals, days)
plt.xlabel("Animals")
plt.ylabel("Days")
plt.title("Time Taken for each animal to get adopted")
plt.show()

most_adopted = data["Animal"].mode()[0]
print(most_adopted)
