text = input("Введіть рядок (мінімум 3 слова через кому та пробіл): ")

words = text.split(", ")

result_words = [words[0], words[-1]]

result_text = ", ".join(result_words)

print("Результат:", result_text)