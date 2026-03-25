import string

# 2.2 Створення функції сортування 
def custom_sort(word):
    ukr_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    eng_alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    key = []
    for char in word.lower():
        if char in ukr_alphabet:
            key.append((0, ukr_alphabet.index(char)))
        elif char in eng_alphabet:
            key.append((1, eng_alphabet.index(char)))
        else:
            key.append((2, ord(char)))
    return key

def main():
    # 2.3 Програма читає текст із створеного в пункті 2.1 файлу
    with open("text.txt", "r", encoding="utf-8") as file:
        text = file.read()
        
    # Виводить його на екран
    print("--- Прочитаний текст ---")
    print(text)
    print("\n------------------------\n")
    
    # Виділення слів (прибираємо пунктуацію для чистого сортування)
    words = text.split()
    clean_words = [word.strip(string.punctuation) for word in words if word.strip(string.punctuation)]
    
    # Використовуючи функцію із пункта 2.2 сортує всі слова тексту
    sorted_words = sorted(clean_words, key=custom_sort)
    
    # Виводить відсортований текст на екран
    print("--- Відсортований список слів ---")
    print(sorted_words)

if __name__ == "__main__":
    main()