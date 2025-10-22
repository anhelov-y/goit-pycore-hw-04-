def total_salary(path):
    # Відкриття файлу за допомогою with
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0  # тут буде сума всіх зарплат
            count = 0  # тут буде кількість розробників
            
            # Читаємо файл по рядках, прибираємо пробіли та розділяємо по комі 
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    
                    # Перевірка 2 частин
                    if len(parts) == 2:
                        name = parts[0]    
                        salary = parts[1]  
                        
                        salary_number = int(salary)
                        
                        total += salary_number
                        count += 1
            
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
    
    total, average = total_salary("test_salaries.txt")
    
    print(f"Загальна сума заробітної плати: {total}")
    print(f"Середня заробітна плата: {average}")