from data import basic_plants_list, plants_list

print(plants_list[0])

for plant in basic_plants_list:
    print(plant[0])

print("-" * 30)
for plant in plants_list:
    print(plant.name)