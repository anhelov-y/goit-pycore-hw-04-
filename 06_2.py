def get_cats_info(path):
    result = []
    
    # Відкриття файлу за допомогою with
    try:
        with open(path, 'r', encoding='utf-8') as file:
            # Читаємо файл по рядках та прибираємо пробіли
            for line in file:
                line = line.strip()
                
                if line:
                    data = line.split(',')
                    
                    # Має бути 3 частини: id, ім'я, вік
                    if len(data) == 3:
                        # Беремо дані
                        cat_id = data[0]
                        name = data[1]
                        age = data[2]
                        
                        # Робимо словник для кота та додаємо в список
                        cat = {
                            "id": cat_id,
                            "name": name, 
                            "age": age
                        }
                        
                        result.append(cat)
        
    except FileNotFoundError:
        print("Не вдалося відкрити файл!")
        return result
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return result
    
    return result

# Створення списку з котами
def create_cats_file():
    cats_data = [
        "60b90c1c13067a15887e1ae1,Tayson,3",
        "60b90c2413067a15887e1ae2,Vika,1", 
        "60b90c2e13067a15887e1ae3,Barsik,2",
        "60b90c3b13067a15887e1ae4,Simon,12",
        "60b90c4613067a15887e1ae5,Tessi,5"
    ]
    
    # Запис у файл 
    with open("cats.txt", "w", encoding="utf-8") as file:
        for cat_line in cats_data:
            file.write(cat_line + "\n")
    
    print("Файл cats.txt створено!")

create_cats_file()
cats = get_cats_info("cats.txt")

if cats:
    print("Знайдені коти:")
    for cat in cats:
        print(f"ID: {cat['id']}, Ім'я: {cat['name']}, Вік: {cat['age']}")
else:
    print("Котів не знайдено!")