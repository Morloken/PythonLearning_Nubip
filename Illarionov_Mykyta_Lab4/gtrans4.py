from translator_pkg import mod_gtrans4, NAME, AUTHOR

def main():
    print(f"Пакет: {NAME} | Автор: {AUTHOR}")
    print("--- Демонстрація mod_gtrans4 (googletrans 4.0.0-rc1) ---")
    
    text = "Добрий день"
    print(f"Оригінал: {text}")
    print(f"Переклад (en): {mod_gtrans4.TransLate(text, 'uk', 'en')}")
    print(f"Визначення мови: {mod_gtrans4.LangDetect(text, 'all')}")
    
    print("\nВиведення таблиці мов (перші 10):")
    mod_gtrans4.LanguageList("screen", "Сонце")

if __name__ == "__main__":
    main()