from data import people, basic_plants_list, plants_list

people = []

if all([person[1] for person in people ]):
    print("Send mail")
else:
    print("check ur mail")