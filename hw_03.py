import sys
import os
from colorama import init, Fore

# Увімкнути кольори
init()

def show_folder(path, level=0):
    """
    Проста функція для показу папок і файлів
    """
    try:
        # Перевірка наявності папки
        if not os.path.exists(path):
            print("ПОМИЛКА: папка не знайдена!")
            return
        
        # Отримати все що є в папці
        items = os.listdir(path)
        
        # Відсортувати
        items.sort()
        
        # Пройти по кожному елементу
        for item in items:
            full_path = os.path.join(path, item)
            
            # Зробити відступи
            spaces = "    " * level
            
            # Перевірка файлу чи папка це
            if os.path.isdir(full_path):
                # Це папка - синій колір
                print(spaces + "📁 " + Fore.BLUE + item + Fore.RESET)
                # Заходимо в цю папку
                show_folder(full_path, level + 1)
            else:
                # Це файл - зелений колір
                print(spaces + "📄 " + Fore.GREEN + item + Fore.RESET)
                
    except Exception as e:
        print("Сталася помилка:", e)

# Початок програми
if __name__ == "__main__":
    # Перевірити чи дали шлях
    if len(sys.argv) < 2:
        print("Треба вказати шлях до папки!")
        print("Наприклад: python hw03.py D:\Git\etc")
    else:
        # Взяти шлях з командного рядка
        folder_path = sys.argv[1]
        print("Структура папки:", folder_path)
        show_folder(folder_path)