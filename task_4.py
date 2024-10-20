# Напишите функцию count_letters(), которая принимает на вход текст и подсчитывает, 
# какое в нём количество цифр K и букв N. Функция должна вывести 
# на экран информацию о найденных буквах и цифрах в определённом формате.

# Пример

# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищем? л

# Количество цифр 0: 2
# Количество букв л: 1

def count_letters(arguments):
    count_number = 0
    count_letters = 0
    
    number = input("Какую цифру ищем?: ")
    letter = input("Какую букву ищем?: ")
    
    for i in arguments:
        
        if i == number:
            count_number += 1
        
        elif i == letter:
            count_letters += 1
    
    print(f"Колличество цифр '{number}': {count_number}")
    print(f"Колличество букв '{letter}': {count_letters}")

text = input("Введите текст: ")
count_letters(text)