import asyncio
from translator_pkg import mod_gtrans4, NAME, AUTHOR

async def main():
    print(f"Пакет: {NAME} | Автор: {AUTHOR}")
    print("--- Демонстрація mod_gtrans4 (googletrans 4.0.2 АСИНХРОННО) ---")
    
    text = "Добрий день"
    print(f"Оригінал: {text}")
    
    translated = await mod_gtrans4.TransLate(text, 'uk', 'en')
    print(f"Переклад (en): {translated}")
    
    detected = await mod_gtrans4.LangDetect(text, 'all')
    print(f"Визначення мови: {detected}")
    
    print("\nВиведення таблиці мов (перші 20):")
    await mod_gtrans4.LanguageList("screen", "Сонце")

if __name__ == "__main__":
    asyncio.run(main())