text = input("Введіть рядок символів: ")

unique_chars = set(text.replace(" ", ""))

letters = set()
digits = set()
punctuation = set()

for char in unique_chars:
    if char.isalpha():
        letters.add(char)
    elif char.isdigit():
        digits.add(char)
    elif char in ".,!?;:-()[]{}\"'…—":
        punctuation.add(char)

print("Рядок без повторів:", "".join(unique_chars))
print("Множина літер:", letters)
print("Множина цифр:", digits)
print("Множина розділових знаків:", punctuation)