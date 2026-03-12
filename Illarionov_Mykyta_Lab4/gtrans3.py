from translator_pkg import mod_gtrans3

def main():
    print("--- Демонстрація mod_gtrans3 (googletrans==3.1.0a0) в Docker ---")
    text = "Добрий день, як справи?"
    print(f"Оригінал: {text}")
    print(f"Переклад (de): {mod_gtrans3.TransLate(text, 'uk', 'de')}")
    print(f"Визначення мови: {mod_gtrans3.LangDetect(text, 'all')}")

if __name__ == "__main__":
    main()