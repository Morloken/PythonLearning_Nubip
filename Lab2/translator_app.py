from googletrans import Translator, LANGUAGES


POPULAR_LANGS = {
    'uk': 'Українська',
    'en': 'English',
    'de': 'German',
    'pl': 'Polish',
    'fr': 'French'
}

def TransLate(text: str, lang: str) -> str:
    """Перекладає текст на задану мову."""
    try:
        translator = Translator()
        dest_code = lang
        
        for code, name in LANGUAGES.items():
            if name.lower() == lang.lower():
                dest_code = code
                break
                
        result = translator.translate(text, dest=dest_code)
        return result.text
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(txt: str):
    """Визначає мову тексту."""
    try:
        translator = Translator()
        result = translator.detect(txt)
        return f"Detected(lang={result.lang}, confidence={result.confidence})"
    except Exception as e:
        return f"Помилка визначення мови: {e}"

def CodeLang(lang: str) -> str:
    """Повертає код або назву мови."""
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang].capitalize()
    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code
    return "Мову не знайдено / Language not found"

def main():
    print("--- Програма перекладу текстів (Docker Edition) ---")
    
    txt = input("Введіть текст для перекладу: ").strip()
    
    if not txt:
        print("Ви не ввели текст. Завершення роботи.")
        return

    print(LangDetect(txt))
    
    #Формування рядка підказки (placeholder)
    #створить рядок типу: "uk, en, de, pl, fr"
    examples = ", ".join(POPULAR_LANGS.keys())
    
    print(f"\nДоступні приклади кодів: {examples}")
    dest_lang = input(f"Введіть мову (за замовчуванням 'en'): ").strip()
    
    #просто натиснув Enter - англійська
    if not dest_lang:
        dest_lang = 'en'
        print("Вибрано мову за замовчуванням: English (en)")

    
    lang_info = CodeLang(dest_lang)
    print(f"Мова призначення: {lang_info} ({dest_lang})")
    
    # Сам уже Переклад тексту
    translation = TransLate(txt, dest_lang)
    print("-" * 30)
    print(f"Переклад:\n{translation}")
    print("-" * 30)

if __name__ == "__main__":
    main()