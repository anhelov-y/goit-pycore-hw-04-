def add_contact(args, contacts):
    # Додає новий контакт до словника
    if len(args) == 2:
        name = args[0]
        phone = args[1]
        contacts[name] = phone
        return f"Додано {name}: {phone}"
    else:
        return "Неправильно! Пиши: додай Ім'я Номер"

def change_contact(args, contacts):
    #Зміна номеру телефону для існуючого контакту
    if len(args) == 2:
        name = args[0]
        new_phone = args[1]
        if name in contacts:
            contacts[name] = new_phone
            return f"Змінено {name}: {new_phone}"
        else:
            return f"Немає такого {name}"
    else:
        return "Неправильно! Пиши: зміни Ім'я НовийНомер"

def show_phone(args, contacts):
    #Показує номер телефону за ім'ям
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return f"Номер {name}: {contacts[name]}"
        else:
            return f"Немає такого {name}"
    else:
        return "Неправильно! Пиши: телефон Ім'я"

def show_all(contacts):
    #Показує всі збережені контакти
    if contacts:
        result = "Всі контакти:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result
    else:
        return "Ще немає контактів"

def main():
    # Gустий словник для контактів
    contacts = {}
    print("Привіт! Я бот-помічник")
    
    # Основний цикл програми 
    while True:
        user_input = input("Введи команду: ")
        
        # Перетворюємо на нижній регістр і прибираємо пробіли
        command = user_input.lower().strip()

        if command == "вихід" or command == "exit":
            print("Бувай!")
            break
            
        elif command == "привіт" or command == "hello":
            print("Привіт! Як справи?")
            
        # Додавання контакту 
        elif command.startswith("додай "):
            args = command.split(" ")[1:]

            print(add_contact(args, contacts))
                
        # Команда зміни номера
        elif command.startswith("зміни "):
            args = command.split(" ")[1:]
            print(change_contact(args, contacts))
                
        # Команда пошуку номера
        elif command.startswith("телефон "):
            args = command.split(" ")[1:]
            print(show_phone(args, contacts))
                
        # Команда показу всіх контактів
        elif command == "всі" or command == "all":
            print(show_all(contacts))
                
        else:
            print("Не вірно введена команда!")

# Запускаємо програму
if __name__ == "__main__":
    main()