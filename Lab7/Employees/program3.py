import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

def calculate_age(birth_date_str):
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
    today = datetime.today().date()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

def get_age_category(age):
    if age < 18:
        return "younger_18"
    elif 18 <= age <= 45:
        return "18-45"
    elif 45 < age <= 70:
        return "45-70"
    else:
        return "older_70"

def main():
    if not os.path.exists("employees.csv"):
        print("Повідомлення: Відсутній, або проблеми при відкритті файлу CSV.")
        return

    try:
        df = pd.read_csv("employees.csv", encoding="utf-8")
        print("Ok")
    except Exception:
        print("Повідомлення: Відсутній, або проблеми при відкритті файлу CSV.")
        return

    # Додаємо вік та категорію
    df['Вік'] = df['Дата народження'].apply(calculate_age)
    df['Категорія'] = df['Вік'].apply(get_age_category)

    # 1. Співробітники за статтю
    gender_counts = df['Стать'].value_counts()
    print("\n--- Співробітники за статтю ---")
    print(gender_counts.to_string())

    plt.figure(figsize=(6, 4))
    gender_counts.plot(kind='pie', autopct='%1.1f%%', colors=['#66b3ff', '#ff9999'])
    plt.title('Розподіл співробітників за статтю')
    plt.ylabel('')
    plt.show()

    # 2. Співробітники за віковими категоріями
    age_counts = df['Категорія'].value_counts()
    print("\n--- Співробітники за віковими категоріями ---")
    print(age_counts.to_string())

    plt.figure(figsize=(8, 5))
    age_counts.plot(kind='bar', color='skyblue')
    plt.title('Розподіл за віковими категоріями')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість')
    plt.xticks(rotation=0)
    plt.show()

    # 3. Стать всередині кожної вікової категорії
    gender_age_counts = df.groupby(['Категорія', 'Стать']).size().unstack(fill_value=0)
    print("\n--- Стать всередині вікових категорій ---")
    print(gender_age_counts.to_string())

    gender_age_counts.plot(kind='bar', figsize=(10, 6), color=['#ff9999', '#66b3ff'])
    plt.title('Розподіл за статтю у вікових категоріях')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість')
    plt.xticks(rotation=0)
    plt.legend(title='Стать')
    plt.show()

if __name__ == "__main__":
    main()