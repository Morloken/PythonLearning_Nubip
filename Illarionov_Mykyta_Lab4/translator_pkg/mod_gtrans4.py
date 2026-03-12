from googletrans import Translator, LANGUAGES

def CodeLang(lang: str) -> str:
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang].capitalize()
    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code
    return "Помилка: мову не знайдено"

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translator = Translator()
        src_code = CodeLang(scr) if scr != 'auto' else 'auto'
        if "Помилка" in src_code and scr != 'auto': src_code = scr
        
        dest_code = CodeLang(dest)
        if "Помилка" in dest_code: dest_code = dest
            
        result = translator.translate(text, src=src_code, dest=dest_code)
        return result.text
        
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        translator = Translator()
        res = translator.detect(text)
        
        if set == "lang": return res.lang
        elif set == "confidence": return str(getattr(res, 'confidence', 0.0))
        else: return f"Lang: {res.lang}, Confidence: {getattr(res, 'confidence', 0.0)}"
    except Exception as e:
        return f"Помилка визначення мови: {e}"

def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        header = f"{'N':<3} {'Language':<15} {'ISO-639 code':<15}"
        if text:
            header += " Text"
            
        output_lines = [header, "-" * 50]
        
        # Друкуємо шапку одразу
        if out == "screen":
            print(header)
            print("-" * 50)
        
        count = 1
        for code, name in LANGUAGES.items():
            row = f"{count:<3} {name.capitalize():<15} {code:<15}"
            if text:
                translated = TransLate(text, 'auto', code)
                row += f" {translated}"
            output_lines.append(row)
            
            # Виводимо рядок по мірі його створення
            if out == "screen":
                print(row)
                
            count += 1
            
        output_lines.append("-" * 50) 
        if out == "screen":
            print("-" * 50)
        elif out == "file":
            with open("languages_list.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(output_lines))
        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"