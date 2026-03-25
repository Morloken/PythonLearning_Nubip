import asyncio
from googletrans import Translator, LANGUAGES

def CodeLang(lang: str) -> str:
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang].capitalize()
    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code
    return "Помилка: мову не знайдено"

async def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translator = Translator()
        src_code = CodeLang(scr) if scr != 'auto' else 'auto'
        if "Помилка" in src_code and scr != 'auto': src_code = scr
        
        dest_code = CodeLang(dest)
        if "Помилка" in dest_code: dest_code = dest
            
        result = await translator.translate(text, src=src_code, dest=dest_code)
        return result.text
        
    except Exception as e:
        return f"Помилка перекладу: {e}"

async def LangDetect(text: str, set_param: str = "all") -> str:
    try:
        translator = Translator()
        res = await translator.detect(text)
        
        if set_param == "lang": return res.lang
        elif set_param == "confidence": return str(getattr(res, 'confidence', 0.0))
        else: return f"Lang: {res.lang}, Confidence: {getattr(res, 'confidence', 0.0)}"
    except Exception as e:
        return f"Помилка визначення мови: {e}"

async def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        header = f"{'N':<3} {'Language':<15} {'ISO-639 code':<15}"
        if text:
            header += " Text"
            
        output_lines = [header, "-" * 50]
        
        if out == "screen":
            print(header)
            print("-" * 50)
        
        count = 1
        translator = Translator()
        for code, name in list(LANGUAGES.items())[:20]: # Обмежив до 20, щоб Google не забанив API
            row = f"{count:<3} {name.capitalize():<15} {code:<15}"
            if text:
                res = await translator.translate(text, src='auto', dest=code)
                row += f" {res.text}"
            output_lines.append(row)
            
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