text = input('Введіть текст: ')

count = 0

for sentence in text.split("."):
        count += 1

print(f"Кількість речень у тексті: {count}")