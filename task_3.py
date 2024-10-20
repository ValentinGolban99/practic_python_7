# Напишите программу, запрашивающую у пользователя число и действие, 
# которое нужно сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру. 
# Каждое действие оформите в виде отдельной функции, а основную программу зациклите.
# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.

def main():
    
    argument = int(input("Введите число: "))
    print("1. - сумма цифр числа; 2. - максимальная цифра числа; 3. - минимальная цифра числа.")
    action = int(input("Выберите действие: "))

    if action == 1:
        summa(argument)
        main()
        
    if action == 2:
        max_num(argument)
        main()
        
    if action == 3:
        min_num(argument)
        main()
    
def summa(argument):
    
    num = argument
    result = 0
    
    while num:
        result += num % 10
        num //= 10
        
    print(f"Сумма цифр от числа {argument} равна {result}. ")

def max_num(argument):
    number = argument
    result = 0
    num = 0
    
    while number:
        num = number % 10
        if num > result:
            result = num
        number //= 10
        
        
    print(f"Максимальная цифра от числа {argument} равна {result}. ")
    
def min_num(argument):
    number = argument
    result = 10
    num = 0
    
    while number:
        num = number % 10
        if num < result:
            result = num
        number //= 10
        
        
    print(f"Минимальная цифра от числа {argument} равна {result}. ")

main()


