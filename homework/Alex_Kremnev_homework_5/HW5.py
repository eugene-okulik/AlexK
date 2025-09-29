#  задание 1
person = ["John", "Doe", "New York", "+1372829383739", "US"]
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

#  задание 2
line = "результат операции: 42"
position_1 = line.index(":") + 2
print(position_1)
num_str = line[position_1:]
print(num_str)
print(type(num_str))
number = int(num_str)
print(number)
print(type(number))
summa = number + 10
print(summa)

line = "результат операции: 514"
position_1 = line.index(":") + 2
print(position_1)
num_str = line[position_1:]
print(num_str)
print(type(num_str))
number = int(num_str)
print(number)
print(type(number))
summa = number + 10
print(summa)

line = "результат работы программы: 9"
position_1 = line.index(":") + 2
print(position_1)
num_str = line[position_1:]
print(num_str)
print(type(num_str))
number = int(num_str)
print(type(number))
summa = number + 10
print(summa)


#  задание 3
students = ["Ivanov", "Petrov", "Sidorov"]
subjects = ["math", "biology", "geography"]
print(f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}")
