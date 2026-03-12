import sys
from googletrans import Translator, LANGUAGES

if sys.version_info >= (3, 13):
    print("Помилка: Версія Python >= 3.13! Пакет googletrans==3.1.0a0 працює нестабільно.")
    sys.exit(1)

def CodeLang(lang: str) -> str:
    lang = lang.lower()
    if lang in LANGUAGES: return LANGUAGES[lang].capitalize()
    for code, name in LANGUAGES.items():
        if name.lower() == lang: return code
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
    except Exception as e: return f"Помилка перекладу: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        translator = Translator()
        res = translator.detect(text)
        if set == "lang": return res.lang
        elif set == "confidence": return str(getattr(res, 'confidence', 0.0))
        else: return f"Lang: {res.lang}, Confidence: {getattr(res, 'confidence', 0.0)}"
    except Exception as e: return f"Помилка: {e}"

def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        limit = 10 
        output_lines = [f"{'N':<4} | {'Language':<15} | {'ISO-639':<10} | {'Text' if text else ''}"]
        output_lines.append("-" * 60)
        for i, (code, name) in enumerate(list(LANGUAGES.items())[:limit], 1):
            translated = TransLate(text, 'auto', code) if text else ""
            output_lines.append(f"{i:<4} | {name.capitalize():<15} | {code:<10} | {translated}")
        result_text = "\n".join(output_lines)
        if out == "screen": print(result_text)
        elif out == "file":
            with open("languages_list_v3.txt", "w", encoding="utf-8") as f: f.write(result_text)
        return "Ok"
    except Exception as e: return f"Помилка: {e}"