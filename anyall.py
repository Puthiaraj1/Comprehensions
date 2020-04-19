entries = [1, 2, 3, 4, 5, 6]

print("all: {}".format(all(entries)))
print("any: {}".format(any(entries)))

print("Iterable with 'False' value")
entries_with_zero = [1, 2, 0, 4, 5, 6]
print("all: {}".format(all(entries_with_zero)))
print("any: {}".format(any(entries_with_zero)))

