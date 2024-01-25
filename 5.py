file9_path = "file2.txt"

with open(file9_path, "r") as file9:
    content = file9.read()

search_word = input("Введіть слово для підрахунку : ")

word_count = content.lower().split().count(search_word.lower())
print(word_count)