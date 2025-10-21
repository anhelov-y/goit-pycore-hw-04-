def get_cats_info(path):
    # Це буде наш список з котами
    result = []
    
    # Спробуємо відкрити файл
    try:
        file = open(path, 'r', encoding='utf-8')
    except:
        print("Не вдалося відкрити файл!")
        return result
    
    # Читаємо файл по рядках
    for line in file:
        # Прибираємо пробіли в кінці рядка
        line = line.strip()
        
        # Якщо рядок не порожній
        if line:
            # Розбиваємо рядок по комах
            data = line.split(',')
            
            # Має бути 3 частини: id, ім'я, вік
            if len(data) == 3:
                # Беремо дані
                cat_id = data[0]
                name = data[1]
                age = data[2]
                
                # Робимо словник для кота
                cat = {
                    "id": cat_id,
                    "name": name, 
                    "age": age
                }
                
                # Додаємо кота до результату
                result.append(cat)
    
    # Закриваємо файл
    file.close()
    
    return result

# СПОЧАТКУ СТВОРИМО ФАЙЛ З КОТАМИ
def create_cats_file():
    # Дані про котів
    cats_data = [
        "60b90c1c13067a15887e1ae1,Tayson,3",
        "60b90c2413067a15887e1ae2,Vika,1", 
        "60b90c2e13067a15887e1ae3,Barsik,2",
        "60b90c3b13067a15887e1ae4,Simon,12",
        "60b90c4613067a15887e1ae5,Tessi,5"
    ]
    
    # Записуємо у файл
    with open("cats.txt", "w", encoding="utf-8") as file:
        for cat_line in cats_data:
            file.write(cat_line + "\n")
    
    print("Файл cats.txt створено!")

# ТЕПЕР ПЕРЕВІРИМО
create_cats_file()  # Створюємо файл
cats = get_cats_info("cats.txt")  # Читаємо файл

if cats:
    print("Знайдені коти:")
    for cat in cats:
        print(f"ID: {cat['id']}, Ім'я: {cat['name']}, Вік: {cat['age']}")
else:
    print("Котів не знайдено!")