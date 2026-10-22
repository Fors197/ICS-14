import os

folder = "TEXT"

print("Повний шлях до каталога:", os.path.abspath(folder))

doc_files = []
docx_files = []
txt_files = []

for file in os.listdir(folder):
    if file.endswith(".doc"):
        doc_files.append(file)
    elif file.endswith(".docx"):
        docx_files.append(file)
    elif file.endswith(".txt"):
        txt_files.append(file)

with open("my_files.txt", "w") as f:
    f.write("Файли з розширенням DOC:\n")
    for file in doc_files:
        f.write(file + "\n")

    f.write("\nФайли з розширенням DOCX:\n")
    for file in docx_files:
        f.write(file + "\n")

    f.write("\nФайли з розширенням TXT:\n")
    for file in txt_files:
        f.write(file + "\n")

print("Списки файлів записано у файл my_files.txt")
