messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]

# Your code goes below here
messy_list.insert(0, messy_list.pop(3))
messy_list.remove("a")
del messy_list[-1]
messy_list.remove(False)

print(messy_list)