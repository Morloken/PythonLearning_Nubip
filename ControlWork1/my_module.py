from googletrans import Translator, LANGUAGES

def process_and_compare(a, b, c):
    processed = []
    for num in (a, b, c):
        if num > 0:
            processed.append(num ** 2)
        else:
            processed.append(num)
    
    mods = [(abs(n), n) for n in processed]
    mods.sort(key=lambda x: x[0])
    
    comparison_str = ""
    for i in range(len(mods)):
        if i == 0:
            comparison_str += f"|{mods[i][1]}|"
        else:
            if mods[i][0] == mods[i-1][0]:
                comparison_str += f" = |{mods[i][1]}|"
            else:
                comparison_str += f" < |{mods[i][1]}|"
                
    return processed, comparison_str

def translate_text(text, dest_language):
    if dest_language not in LANGUAGES:
        dest_language = 'uk'
        
    if dest_language == 'uk':
        return text

    translator = Translator()
    try:
        translation = translator.translate(text, dest=dest_language)
        return translation.text
    except Exception:
        return text