# Методы строк
from aiohttp import payload_type

string = 'hello, world!'
uppercase = string.upper() # Преобразует все символы в верхний регистр
print(uppercase)

lowercase = string.lower() # Преобразует все символы в нижний регистр
print(lowercase)

replace = string.replace('hello', 'bye') # Изменяет какое-то слово на другой
print(replace)

isdigit = string.isdigit() # Проверяет есть ли число в строке
print(isdigit)

split = string.split(',') # Разделяет строку на массив
print(split)

strip = string.strip() # Удаляет пробелы в начале и в конце текста (не внутри него!)
print(strip)



# Методы списков
massive = [4, 7, 8, 1, 9, 0, -1]
second_massive = [12, 10, 11]

massive.sort(reverse=True) # Сортировка
print(massive)

massive.append(4) # Добавляет элемент в конец списка
print(massive)

massive.extend(second_massive) # Объединяет два массива
print(massive)

massive.insert(0, 77) # Добавляет элемент по назначенному индексу
print(massive)

massive.remove(1) # Удаляет первый найденный элемент в списке, если нет возвращает ошибку
print(massive)

delete = massive.pop() # Удаляет элемент по индексу по (умолчанию с конца)
print(delete, massive)

index = massive.index(0) # Возвращает индекс элемента, если его нет возвращает ошибку
print(index, massive)

copy = massive.copy() # Копирует список в новую переменную

massive.clear()
print(massive)



# Методы словарей
person = {
    'name': 'Kamaliddin',
    'age': 16,
    'job': 'Py-developer'
}

copied_dict = person.copy() # Копирует словарь в переменную


keys = person.keys()
values = person.values()
items = person.items()
print(keys)
print(values)
print(items)


item = person.get('name', None) # Возвращает значение ключа, если его нет возвращает None
print(item)

other_person = {
    'name': 'Alice',
    'age': 23,
    'city': 'New-York'
}

person.update(other_person) # Обновляет словарь используя другой
print(person)


delete = person.pop('job') # Удаляет ключ-значение, если его нет возвращает ошибку
print(person, delete)


popitem = person.popitem() # Удаляет последнее ключ-значение,
print(popitem, person)


person.setdefault('city', 'hobby-horsing') # Добавляет новое ключ-значение если заданного ключа нет, если есть - нет
print(person)


person.clear() # Очищает словарь
print(person)




# Методы множеств
my_set = {5, 2, 1, 9, 8, 7, 2}

my_set.add(3) # Добавляет в элемент
print(my_set)

my_set.update([4, 5, 6]) # Добавляет элементы из итерируемого объекта
print(my_set)

my_set.remove(3) # Удаляет элемент, если его нет вызывает ошибку
print(my_set)

my_set.discard(2) # Удаляет элемент, если его нет - не вызывает ошибку
print(my_set)

delete = my_set.pop() # Удаляет первый элемент
print(delete, my_set)


other_set = {-1, 0, 11, 10, 4, 3}
extended = my_set.union(other_set) # Объединяет два множества
print(extended)

intersection = other_set.intersection(my_set) # Возвращает элемент который и там и там есть
print(intersection)

diff = my_set.difference(other_set) # Возвращает не общие элементы
print(diff)

sym_diff = my_set.symmetric_difference(other_set) # Возвращает симметрическую разность множеств (все элементы, не общие для обоих).
print(sym_diff)

result = {1, 2}.isdisjoint({3, 4}) # Проверяет нет ли общих элементов
print(result)