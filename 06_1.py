def total_salary(path):
    # Пробуємо відкрити файл
    try:
        # Відкриваємо файл для читання
        file = open(path, 'r', encoding='utf-8')
        
        total = 0  # тут буде сума всіх зарплат
        count = 0  # тут буде кількість розробників
        
        # Читаємо файл по рядках
        for line in file:
            line = line.strip()  # прибираємо зайві пробіли
            if line:  # якщо рядок не порожній
                # Розділяємо рядок по комі
                parts = line.split(',')
                
                # Перевіряємо що отримали 2 частини
                if len(parts) == 2:
                    name = parts[0]    # перша частина - ім'я
                    salary = parts[1]  # друга частина - зарплата
                    
                    # Перетворюємо зарплату в число
                    salary_number = int(salary)
                    
                    # Додаємо до загальної суми
                    total += salary_number
                    count += 1
        
        # Закриваємо файл
        file.close()
        
        # Якщо знайшли хоча б одного розробника
        if count > 0:
            average = total / count
            return (total, average)
        else:
            return (0, 0)
            
    except FileNotFoundError:
        print(f"Файл {path} не знайдено!")
        return (0, 0)
    except ValueError:
        print("Помилка: зарплата має бути числом!")
        return (0, 0)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0, 0)

# Перевіряємо роботу функції
if __name__ == "__main__":
    # Можемо створити тестовий файл
    with open("test_salaries.txt", "w", encoding="utf-8") as f:
        f.write("Alex Korp,3000\n")
        f.write("Nikita Borisenko,2000\n")
        f.write("Sitarama Raju,1000\n")
        f.write("Anna Borisenko,1500\n")
        f.write("Denis Rubalko,2500\n")
    
    # Викликаємо нашу функцію
    total, average = total_salary("test_salaries.txt")
    
    print(f"Загальна сума заробітної плати: {total}")
    print(f"Середня заробітна плата: {average}")