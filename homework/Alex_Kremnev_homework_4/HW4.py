my_dict = {
    "tuple": (1, 2, 3, 4, 5),
    "list": ["aple", "first", "ss", "ew", "mm"],
    "dict": {
        "name": "Alice",
        "city": "London",
        "color": "blue",
        "language": "Python",
        "year": 2025,
    },
    "set": {"book", "lamp", "tea", "window", 100},
}

print(my_dict["tuple"][-1])  #  выведите на экран последний элемент

print(my_dict["list"].append("end"))  #  добавьте в конец списка еще один элемент
print(my_dict["list"].pop(1))  #  удалите второй элемент списка
print(my_dict["list"])

my_dict["dict"][
    "i am a tuple"
] = "value"  #  добавьте элемент с ключом ('i am a tuple',) и любым значением
print(my_dict["dict"])
my_dict["dict"].pop("name")  #  удалите какой-нибудь элемент
print(my_dict["dict"])

my_dict["set"].add("dalas")  #  добавьте новый элемент в множество
my_dict["set"].pop()  #  удалите элемент из множества
print(my_dict["set"])
