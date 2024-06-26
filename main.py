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
