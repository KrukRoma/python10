file3_path = "file3.txt"
file4_path = "file4.txt"

with open(file3_path, "w") as file3, open(file4_path, "w") as file4:
    content1 = "1Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet quis consectetur dignissimos aut iste commodi, sint consequatur animi harum modi eaque obcaecati sapiente error corrupti voluptates, eius alias. Exercitationem, in."
    content2 = file4_path
    file3.write(content1)
    file4.write(content2)

char_count = len(content1)
line_count = content1.count('\n') +1
vowel_count = sum(1 for char in content1 if char.lower() in 'eyuioa')
consonant_count = sum(1 for char in content1 if char.isalpha() and char.lower() not in 'eyuioa')
digit_count = sum(1 for char in content1 if char.isdigit())

with open(file4_path, 'w') as output_file:
    output_file.write(f"Кількість символів: {char_count}\n")
    output_file.write(f"Кількість рядків: {line_count}\n")
    output_file.write(f"Кількість голосних літер: {vowel_count}\n")
    output_file.write(f"Кількість приголосних літер: {consonant_count}\n")
    output_file.write(f"Кількість цифр: {digit_count}\n")
