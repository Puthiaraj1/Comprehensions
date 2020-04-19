rices = ["plain", "egg", "veggie"]
toppings = ["chiecken", "mutton", "panner", "prawn"]

for meals in [(rice, topping) for rice in rices for topping in toppings]:
    print(meals)
print("*" * 20)

# for rice in rices:
#     for topping in toppings:
#         print((rice,topping))

for meals in [[(rice, topping) for rice in rices ]for topping in toppings]:
    print(meals)

