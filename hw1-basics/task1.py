"""
Задание 1. Расшифровка.

ИИ-ассистент выгрузил маркетинговый отчёт зашифрованным шифром Цезаря -
теперь его нужно расшифровать вручную.
"""


def decode_caesar_cipher(text: str, shift: int) -> str:
    """
    Расшифровать text, зашифрованный шифром Цезаря со сдвигом shift.

    Каждая латинская буква в исходном (незашифрованном) тексте была сдвинута
    вперёд по алфавиту на shift позиций (с переходом с 'z' на 'a' и с 'Z' на 'A').
    Регистр буквы должен сохраняться. Все остальные символы - цифры, пробелы,
    знаки препинания - в тексте не менялись при шифровании и должны остаться
    как есть при расшифровке.

    Пример: decode_caesar_cipher("Khoor!", 3) -> "Hello!"
    """
    # TODO: ваш код здесь
    
    empty_string = ''
    for symbol in text:
        if 'A' <= symbol <= 'Z':
            symbol = chr((ord(symbol) - ord('A') - shift) % 26 + ord('A')) #обрабатываем случай с выходом из диапазона букв
        elif 'a' <= symbol <= 'z':
            symbol = chr((ord(symbol) - ord('a') - shift) % 26 + ord('a')) #аналогично для нижнего регистра

        empty_string += symbol

    return empty_string


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    with open("data/task1_encoded.txt", encoding="utf-8") as f:
        encoded_text = f.read().strip()

    shift = 7
    print(decode_caesar_cipher(encoded_text, shift))
