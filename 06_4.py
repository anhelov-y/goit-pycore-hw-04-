def main():
    # Створюємо пустий словник для контактів
    contacts = {}
    print("Привіт! Я бот-помічник")
    
    # Основний цикл програми 
    while True:
        # Отримуємо команду від користувача
        user_input = input("Введи команду: ")
        

        command = user_input.lower().strip()
        
        # Команда виходу з програми
        if command == "вихід" or command == "exit":
            print("Бувай!")
            break  # зупинка циклу
            
        elif command == "привіт" or command == "hello":
            print("Привіт! Як справи?")
            
        # Команда для додавання контакту 
        elif command.startswith("додай "):
            # Розбиваємо команду на слова: ["додай", "Ім'я", "Номер"]
            parts = command.split(" ")
            
            # Перевіряємо що отримали 3 слова: команда, ім'я, номер
            if len(parts) == 3:
                name = parts[1]    # друге слово - ім'я
                phone = parts[2]   # третє слово - номер
                contacts[name] = phone  # зберігаємо в словник
                print(f"Додано {name}: {phone}")
            else:
                # Якщо неправильна кількість слів
                print("Неправильно! Пиши: додай Ім'я Номер")
                
        # Команда зміни номера - починається з "зміни "
        elif command.startswith("зміни "):
            parts = command.split(" ")
            if len(parts) == 3:
                name = parts[1]
                new_phone = parts[2]
                # Перевіряємо чи існує такий контакт
                if name in contacts:
                    contacts[name] = new_phone  # оновлюємо номер
                    print(f"Змінено {name}: {new_phone}")
                else:
                    print(f"Немає такого {name}")
            else:
                print("Неправильно! Пиши: зміни Ім'я НовийНомер")
                
        # Команда пошуку номера - починається з "телефон "
        elif command.startswith("телефон "):
            parts = command.split(" ")
            if len(parts) == 2:
                name = parts[1]
                # Перевіряємо чи є контакт у словнику
                if name in contacts:
                    print(f"Номер {name}: {contacts[name]}")
                else:
                    print(f"Немає такого {name}")
            else:
                print("Неправильно! Пиши: телефон Ім'я")
                
        # Команда показу всіх контактів
        elif command == "всі" or command == "all":
            # Перевіряємо чи словник не порожній
            if contacts:
                print("Всі контакти:")
                # Проходимо по всіх контактах у словнику
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")
            else:
                print("Ще немає контактів")
                
        # Якщо команду не розпізнано
        else:
            print("Не вірно введена команда!")

# Ця перевірка потрібна щоб код запускався тільки коли ми запускаємо цей файл напряму
# а не коли його імпортують в інший файл
if __name__ == "__main__":
    main()  # Запускаємо нашу головну функцію
