def check_duplicates(input_string):
    elements = input_string.split()
    unique_elements = set(elements)
    text = "Повторяющихся значений нет"
    if len(elements) != len(unique_elements):
        text = "Есть повторяющиеся значения"
    print(text)

# Запрос строки у пользователя
user_input = input("Введите строку: ")
check_duplicates(user_input) # Выполняем проверку
