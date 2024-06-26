# Экзаменационная работа

#### Код: 

```python
def check_duplicates(input_string):
    elements = input_string.split()
    unique_elements = set(elements)
    if len(elements) != len(unique_elements):
        print("Есть повторяющиеся значения")
    else:
        print("Повторяющихся значений нет")

# Запрос строки у пользователя
user_input = input("Введите строку: ")
check_duplicates(user_input)
```

#### Как использовать

Введите строку: [первое значение] [второе значение] [n значение]

Строка преобразуется в массив из строк, при помощи деления знаком Space (пробел), и если в этом массиве обнаруживаются идентичные строки, то программа об этом сообщит. 
