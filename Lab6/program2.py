import urllib.parse
import pyperclip

def main():
    # 3.1 Отримує інтернет посилання у форматі (II)
    url_encoded = input("Введіть посилання у форматі Punycode: ")
    
    # Перетворює його до формату (I)
    url_decoded = urllib.parse.unquote(url_encoded)
    
    # Виводить результат на екран
    print("\nПеретворене посилання:")
    print(url_decoded)
    
    # Копіює перетворене посилання в буфер обміну операційної системи
    pyperclip.copy(url_decoded)
    print("\nПосилання успішно скопійовано в буфер обміну!")

if __name__ == "__main__":
    main()