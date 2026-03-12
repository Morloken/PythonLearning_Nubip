from translator_pkg import mod_deeptr

def main():
    print("--- Демонстрація mod_deeptr (deep-translator) ---")
    
    text = "Добрий день"
    print(f"Оригінал: {text}")
    print(f"Переклад (en): {mod_deeptr.TransLate(text, 'uk', 'en')}")
    print(f"Визначення мови: {mod_deeptr.LangDetect(text, 'all')}")
    
    print("\nВиведення таблиці мов (перші 10):")
    mod_deeptr.LanguageList("screen", "Сонце")

if __name__ == "__main__":
    main()