import json
import os
import sys
from googletrans import LANGUAGES
from my_module import process_and_compare, translate_text

DATA_FILE = "MyData.json"

def format_number(num):
    return int(num) if num.is_integer() else num

def input_and_save():
    while True:
        try:
            user_input = input("Введіть три числа(через пробіл, в одному рядку) a, b, c: ")
            a, b, c = map(float, user_input.split())
            break
        except ValueError:
            print("Помилка вводу. Будь ласка, введіть рівно три числа через пробіл.")
            
    lang = input("Введіть мову інтерфейсу: ")
    
    new_data = {"a": a, "b": b, "c": c, "lang": lang}
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)
        
    print(f"Дані збережено в файл {DATA_FILE}")
    sys.exit(0)

def main():
    print("1 - Читати дані з уже наявного файлу")
    print("2 - Ввести дані з консолі щоб записати у файл")
    choice = input()

    if choice == '2':
        input_and_save()

    elif choice == '1':
        data = None
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if not all(k in data for k in ("a", "b", "c", "lang")):
                        data = None
            except (json.JSONDecodeError, ValueError):
                data = None

        if data is None:
            input_and_save()

        a, b, c = data["a"], data["b"], data["c"]
        lang = data["lang"].strip().lower()

        if lang not in LANGUAGES and lang != 'uk':
            print("Помилка: Некоректний код мови. Встановлено мову інтерфейсу за замовчуванням (Українська).")
            lang = 'uk'
            lang_display = "Українська"
        elif lang == 'uk':
            lang_display = "Українська"
        else:
            lang_display = lang

        text_lang = f"Мова: {lang_display}"
        text_nums = f"Три числа a, b, c: {format_number(a)} {format_number(b)} {format_number(c)}"
        text_desc = "Додатні возвести в квадрат, а від'ємні залишити без змін, порівняти модулі отриманих чисел."

        print(translate_text(text_lang, lang))
        print(translate_text(text_nums, lang))
        print()
        print(translate_text(text_desc, lang))

        processed_nums, comparison_result = process_and_compare(a, b, c)
        
        processed_str = " ".join(str(format_number(n)) for n in processed_nums)
        print(processed_str)
        print(comparison_result)
        
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()