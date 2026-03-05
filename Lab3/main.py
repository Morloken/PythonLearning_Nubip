import asyncio
import time
import re
from googletrans import Translator, LANGUAGES

def CodeLang(lang):#-----------------CodeLang
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang].capitalize()
    
    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code
    return "Помилка: мову не знайдено"

def LangDetect(txt):#-----------------LangDetect
    async def _detect():
        translator = Translator()
        return await translator.detect(txt)
    
    try:
        result = asyncio.run(_detect())
        return result.lang, getattr(result, 'confidence', 0.0)
    except Exception as e:
        return "error", 0.0

def TransLate(text_str, lang):#-----------------TransLate
    async def _translate():
        translator = Translator()
        dest_code = CodeLang(lang)
        if "Помилка" in dest_code:
            dest_code = lang
        elif lang.lower() in LANGUAGES:
            dest_code = lang.lower()
            
        return await translator.translate(text_str, dest=dest_code)
        
    try:
        result = asyncio.run(_translate())
        return result.text
    except Exception as e:
        return f"Помилка перекладу: {e}"

async def async_translate(text, lang):
    translator = Translator()
    dest_code = CodeLang(lang)
    if "Помилка" in dest_code:
        dest_code = lang
    elif lang.lower() in LANGUAGES:
        dest_code = lang.lower()
    
    try:
        result = await translator.translate(text, dest=dest_code)
        return result.text
    except Exception as e:
        return f"Помилка перекладу: {e}"

async def async_process_all(sentences, lang):
    tasks = [async_translate(s, lang) for s in sentences]
    return await asyncio.gather(*tasks)

def main():
    filename = "steve_jobs.txt"
    
    print("--- Вибір мови перекладу ---")
    print("Популярні мови та їх коди:")
    print("  Англійська  - en")
    print("  Українська  - uk")
    print("  Німецька    - de")
    print("  Французька  - fr")
    print("  Іспанська   - es")
    print("(Ви можете ввести код будь-якої іншої підтримуваної мови)")
    print("-" * 40)
    
    while True:
        target_lang = input("Введіть код мови або її назву для перекладу: ").strip()
        
        if target_lang.lower() in LANGUAGES:
            target_code = target_lang.lower()
            target_lang_name = LANGUAGES[target_code].capitalize()
            break
        else:
            check_code = CodeLang(target_lang)
            if "Помилка" not in check_code:
                target_code = check_code
                target_lang_name = target_lang.capitalize()
                break
            else:
                print("Помилка: Такої мови не знайдено. Будь ласка, спробуйте ще раз (наприклад, 'uk' або 'ukrainian').")
    
    print("-" * 40)
    print(f"Обрано мову: {target_lang_name} (код: {target_code}). Починаємо читання файлу...")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено.")
        return
    except Exception as e:
        print(f"Помилка читання файлу: {e}")
        return

    char_count = len(text)
    TxtList = re.split(r'(?<=[.!?])\s+', text.strip())
    TxtList = [s for s in TxtList if s]
    sentence_count = len(TxtList)

    print(f"--- Аналіз файлу ---")
    print(f"Ім'я файлу: {filename}")
    print(f"Кількість символів: {char_count}")
    print(f"Кількість речень: {sentence_count}")
    print("-" * 40)

    orig_lang_code, confidence = LangDetect(text)
    orig_lang_name = CodeLang(orig_lang_code)
    print(f"Оригінал: мова - {orig_lang_name}, код - {orig_lang_code}, confidence - {confidence}")
    print("-" * 40)
    print("Оригінальний текст:")
    print(text)
    print("-" * 40)

    # --- 3.4.1. Синхронний режим ---
    print(f"Виконується синхронний переклад на {target_lang_name}...")
    start_sync = time.time()
    
    sync_translated_list = []
    for sentence in TxtList:
        sync_translated_list.append(TransLate(sentence, target_code))
        
    sync_time = time.time() - start_sync
    
    sync_joined_text = " ".join(sync_translated_list)
    sync_char_count = len(sync_joined_text)
    sync_sentence_count = len(sync_translated_list)
    
    print("Результат синхронного перекладу:")
    print("-" * 40)
    print(sync_joined_text)
    print("-" * 40)
    print(f"Кількість символів у перекладі: {sync_char_count}")
    print(f"Кількість речень у перекладі: {sync_sentence_count}")
    print("-" * 40)
    print()
    print()
    print()

    # --- 3.4.2. Асинхронний режим ---
    print(f"Виконується асинхронний переклад на {target_lang_name}...")
    start_async = time.time()
    
    async_translated_list = asyncio.run(async_process_all(TxtList, target_code))
    
    async_time = time.time() - start_async

    async_joined_text = " ".join(async_translated_list)
    async_char_count = len(async_joined_text)
    async_sentence_count = len(async_translated_list)
   
    print("Результат асинхронного перекладу:")
    print("-" * 40)
    print(async_joined_text)
    print("-" * 40)
    print(f"Кількість символів у перекладі: {async_char_count}")
    print(f"Кількість речень у перекладі: {async_sentence_count}")
    print("-" * 40)

    print(f"Час, затрачений на синхронний переклад (п. 3.4.1): {sync_time:.4f} сек")
    print(f"Час, затрачений на асинхронний переклад (п. 3.4.2): {async_time:.4f} сек")
    
    if async_time > 0:
        speedup = sync_time / async_time
        print(f"Асинхронний підхід швидший у {speedup:.2f} разів")

if __name__ == "__main__":
    main()