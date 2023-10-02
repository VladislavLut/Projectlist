text = input('Введіть текст: ')
reserved_words = input('Введіть список зарезервованих слів: ').split()

for word in text.split():
    if word in reserved_words:
        text = text.replace(word, word.upper())

print(text)