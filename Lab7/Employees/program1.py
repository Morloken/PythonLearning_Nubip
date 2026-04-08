import csv
import random
from datetime import date
from faker import Faker

def main():
    fake = Faker(locale='uk_UA')
    
    # Словники По батькові (по 22 штуки)
    male_patronymics = [
        "Іванович", "Петрович", "Сергійович", "Михайлович", "Олександрович",
        "Володимирович", "Миколайович", "Васильович", "Анатолійович", "Юрійович",
        "Вікторович", "Степанович", "Андрійович", "Богданович", "Григорович",
        "Дмитрович", "Євгенович", "Максимович", "Олегович", "Романович",
        "Тарасович", "Ярославович"
    ]
    
    female_patronymics = [
        "Іванівна", "Петрівна", "Сергіївна", "Михайлівна", "Олександрівна",
        "Володимирівна", "Миколаївна", "Василівна", "Анатоліївна", "Юріївна",
        "Вікторівна", "Степанівна", "Андріївна", "Богданівна", "Григорівна",
        "Дмитрівна", "Євгенівна", "Максимівна", "Олегівна", "Романівна",
        "Тарасівна", "Ярославівна"
    ]

    # Генеруємо список статей: 200 жінок (40%), 300 чоловіків (60%)
    genders = ['Жіноча'] * 200 + ['Чоловіча'] * 300
    random.shuffle(genders)

    records = []
    
    for gender in genders:
        # Дата народження від 1946 до 2011
        birth_date = fake.date_between_dates(date_start=date(1946, 1, 1), date_end=date(2011, 12, 31))
        
        if gender == 'Жіноча':
            first_name = fake.first_name_female()
            last_name = fake.last_name_female()
            patronymic = random.choice(female_patronymics)
        else:
            first_name = fake.first_name_male()
            last_name = fake.last_name_male()
            patronymic = random.choice(male_patronymics)

        records.append({
            "Прізвище": last_name,
            "Ім’я": first_name,
            "По батькові": patronymic,
            "Стать": gender,
            "Дата народження": birth_date.strftime("%Y-%m-%d"),
            "Посада": fake.job(),
            "Місто проживання": fake.city(),
            "Адреса проживання": fake.street_address(),
            "Телефон": fake.phone_number(),
            "Email": fake.email()
        })

    # Запис у CSV
    headers = ["Прізвище", "Ім’я", "По батькові", "Стать", "Дата народження", 
               "Посада", "Місто проживання", "Адреса проживання", "Телефон", "Email"]
               
    with open("employees.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(records)

    print("Файл employees.csv успішно створено (500 записів).")

if __name__ == "__main__":
    main()