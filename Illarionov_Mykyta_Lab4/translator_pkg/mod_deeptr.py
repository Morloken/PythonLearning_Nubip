from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs

def CodeLang(lang: str) -> str:
    langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
    lang = lang.lower()
    for name, code in langs_dict.items():
        if code == lang: return name.capitalize()
        if name == lang: return code
    return "Помилка: мову не знайдено"

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        target = dest if dest in GoogleTranslator().get_supported_languages(as_dict=True).values() else CodeLang(dest)
        source = scr if scr == 'auto' else (scr if scr in GoogleTranslator().get_supported_languages(as_dict=True).values() else CodeLang(scr))
        
        translated = GoogleTranslator(source=source, target=target).translate(text)
        return translated
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        detection = detect_langs(text)[0]
        lang = detection.lang
        conf = round(detection.prob, 2)
        
        if set == "lang": return lang
        elif set == "confidence": return str(conf)
        else: return f"Lang: {lang}, Confidence: {conf}"
    except Exception as e:
        return f"Помилка: {e}"

def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
        
        header = f"{'N':<3} {'Language':<15} {'ISO-639 code':<15}"
        if text:
            header += " Text"
            
        output_lines = [header, "-" * 50]
        
        if out == "screen":
            print(header)
            print("-" * 50)
        
        count = 1
        for name, code in langs_dict.items():
            row = f"{count:<3} {name.capitalize():<15} {code:<15}"
            if text:
                translated = TransLate(text, 'auto', code)
                row += f" {translated}"
            output_lines.append(row)
            
            if out == "screen":
                print(row)
                
            count += 1
            
        output_lines.append("-" * 50)
        if out == "screen":
            print("-" * 50)
        elif out == "file":
            with open("languages_list_deep.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(output_lines))
        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"