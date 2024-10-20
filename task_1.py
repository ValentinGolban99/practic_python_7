# Напишите функцию summa_n, которая принимает одно целое положительное число N и выводит сумму всех чисел от 1 до N включительно.

# Пример работы программы
# Введите число: 5
# Сумма чисел от 1 до 5 равна 15

def summa_n(number):
    result = 0
    
    for i in range(number + 1):
        result += i
        i += 1
    print(result)

number = int(input("Введите число: "))

if number > 0:
    summa_n(number)

else:
    print("Ошибка! Введите положительное число.")
