file9_path = "file5.txt"
search_word = input("Введіть слово для пошуку: ")
replace_word = input("Введіть слово для заміни: ")

with open(file9_path, "r") as file:
    content = file.read()

updated_content = content.replace(search_word, replace_word)

with open(file9_path, "w") as file:
    file.write(updated_content)