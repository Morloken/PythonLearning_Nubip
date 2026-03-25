import json
import os
import re
import asyncio

def main():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
    except Exception as e:
        print(f"Помилка читання config.json: {e}")
        return

    txt_file = config.get("text_file")
    target_lang = config.get("target_language")
    mod_name = config.get("module_name")
    output_type = config.get("output")
    max_sentences = config.get("max_sentences")

    if not os.path.exists(txt_file):
        print(f"Файл {txt_file} не знайдено!")
        return

    if mod_name == "mod_gtrans4": 
        from translator_pkg import mod_gtrans4 as translator_mod
    elif mod_name == "mod_deeptr": 
        from translator_pkg import mod_deeptr as translator_mod
    else:
        print("Невідомий або непідтримуваний локально модуль!")
        return

    with open(txt_file, "r", encoding="utf-8") as f: text = f.read()

    file_size = os.path.getsize(txt_file)
    char_count = len(text)
    sentences = [s for s in re.split(r'(?<=[.!?])\s+', text.strip()) if s]
    
    # Виклик LangDetect залежно від модуля
    if mod_name == "mod_gtrans4":
        lang_info = asyncio.run(translator_mod.LangDetect(text, "lang"))
    else:
        lang_info = translator_mod.LangDetect(text, "lang")

    print(f"Файл: {txt_file}")
    print(f"Розмір: {file_size} байт")
    print(f"Символів: {char_count}")
    print(f"Речень: {len(sentences)}")
    print(f"Мова тексту: {lang_info}")
    print("-" * 40)

    text_to_translate = " ".join(sentences[:max_sentences])
    
    # Виклик TransLate залежно від модуля
    if mod_name == "mod_gtrans4":
        translated_text = asyncio.run(translator_mod.TransLate(text_to_translate, lang_info, target_lang))
    else:
        translated_text = translator_mod.TransLate(text_to_translate, lang_info, target_lang)

    if output_type == "screen":
        print(f"Мова перекладу: {target_lang}")
        print(f"Модуль: {mod_name}")
        print("Переклад:")
        print(translated_text)
    elif output_type == "file":
        name, ext = os.path.splitext(txt_file)
        new_filename = f"{name}_{target_lang}{ext}"
        with open(new_filename, "w", encoding="utf-8") as f:
            f.write(translated_text)
        print("Ok")

if __name__ == "__main__":
    main()