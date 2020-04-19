import timeit

menu = [
    ["rice", "egg", "veggie"],
    ["rice", "lintels", "veggie"],
    ["rice", "chicken", "veggie"],
    ["rice", "egg", "veggie", "curd"],
    ["rice", "egg", "chicken", "curd"],
    ["rice", "egg", "chicken", "lintels", "curds"],
    ["rice", "egg", "lintels", "curd"],
    ["rice", "curd"]
]

for meal in menu:
    if 'lintels' not in meal:
        print(meal)

print("-" * 30)


def lintelss_comp():
    # meals = [meal for meal in menu if "lintels" not in meal]
    meals = [meal for meal in menu if not_lintels(meal)]
    return meals

print("-" * 30)


def not_lintels(meal_list: list):
    return "lintels" not in meal_list

def lintelss_filter():
    linteless_meal = list(filter(not_lintels, menu))
    return linteless_meal

if __name__ == '__main__':
    print(timeit.timeit(lintelss_comp, number=10000))
    print(timeit.timeit(lintelss_filter, number=10000))