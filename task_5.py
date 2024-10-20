# Используя этот шаблон проекта, реализуйте игры «Камень, ножницы, бумага» и «Угадай число».

def rock_paper_scissors(pick_bot, count_bot, count_gamer):
      
    gamer = input("Камень? Ножницы? Бумага?: ")
    gamer = gamer.lower()
    
    if gamer == "камень" and pick_bot == 1:
        print("У меня тоже камень! Давай еще раз!")
        print(f"Счет: Игрок - {count_gamer}; Бот - {count_bot}")
        rock_paper_scissors(3, count_bot, count_gamer)
    
    elif gamer == "камень" and pick_bot == 2:
        print("У меня ножницы! Ты победил!")
        count_gamer += 1
        print(f"Счет: Игрок - {count_gamer}; Бот - {count_bot}")
        rock_paper_scissors(1, count_bot, count_gamer)
    
    elif gamer == "камень" and pick_bot == 3:
        print("У меня бумага! Ты проиграл!")
        count_bot += 1
        print(f"Счет: Игрок - {count_gamer}; Бот - {count_bot}")
        rock_paper_scissors(2, count_bot, count_gamer)

    elif gamer == "ножницы" and pick_bot == 1:
        print("У меня камень! Ты проиграл!")
        count_bot += 1
        print(f"Счет: Игрок - {count_gamer}; Бот - {count_bot}")
        rock_paper_scissors(2, count_bot, count_gamer)
    
    elif gamer == "ножницы" and pick_bot == 2:
        print("У меня ножницы! Давай еще раз!")
        print(f"Счет: Игрок - {count_gamer}; Бот - {count_bot}")
        rock_paper_scissors(3, count_bot, count_gamer)
    
    elif gamer == "ножницы" and pick_bot == 3:
        print("У меня бумага! Ты победил!")
        count_gamer += 1
        print(f"Счет: Игрок - {count_gamer}; Бот - {count_bot}")
        rock_paper_scissors(1, count_bot, count_gamer)
        
    elif gamer == "бумага" and pick_bot == 1:
        print("У меня камень! Ты победил!")
        count_gamer += 1
        print(f"Счет: Игрок - {count_gamer}; Бот - {count_bot}")
        rock_paper_scissors(1, count_bot, count_gamer)
    
    elif gamer == "бумага" and pick_bot == 2:
        print("У меня ножницы! Ты проиграл!")
        count_bot += 1
        print(f"Счет: Игрок - {count_gamer}; Бот - {count_bot}")
        rock_paper_scissors(2, count_bot, count_gamer)
    
    elif gamer == "бумага" and pick_bot == 3:
        print("У меня бумага! Давай еще раз!")
        print(f"Счет: Игрок - {count_gamer}; Бот - {count_bot}")
        rock_paper_scissors(3, count_bot, count_gamer)
    
    else:
        print("Неправельный ввод! Хотите выйти, продилжить или пререйти на 'Угадай число'? ")
        m = int(input("1. Выйти; 2. Продолжить; 3. Перейти на 'Угадай число': "))
        
        if m == 1:
            print("Спасибо за игру!")
        
        elif m == 2:
            print("Тогда продолжим. ")
            rock_paper_scissors(2, count_bot, count_gamer)
        
        elif m == 3:
            print("Загадывай число!")
            guess_the_number()     

def guess_the_number():
    
    number = int(input("Загадай число от 1 до 100: "))
    
    result = 50
    count = 1
    
    while True:
        
        print("Для ответа программе: 1 - равно, 2 - больше, 3 - меньше.")
        print("Твоё число равно, меньше или больше, чем число ", result, "?")
        question = int(input())
        
        if question == 1:
            print("Ура я угадал!")
            print("Хотите выйти или еще раз, или пререйти на 'Камень, ножницы, бумага'? ")
            m = int(input("1. Выйти; 2. Еще раз; 3. Перейти на 'Камень, ножницы, бумага': "))
            
            if m == 1:
                print("Спасибо за игру!")
                break
            
            elif m == 2:
                print("Ну давай)). ")
                guess_the_number()
            
            elif m == 3:
                print("Камень! Ножницы! Бумага!")
                rock_paper_scissors(2, 0, 0)
            
        if question == 3:
            result -= int(25 / count)
            count += 1
        if question == 2:
            result += int(25 / count)
            count += 1

def main_menu():
    print("Привет! Давай поиграем! ")
    choice = int(input("1. Камень, ножницы, бумага; 2. Угадай число. \nВыбери игру: "))
    
    if choice == 1:
        print("Камень! Ножницы! Бумага!")
        rock_paper_scissors(2, 0, 0)

    elif choice == 2:
        print("Загадывай число!")
        guess_the_number()

main_menu()