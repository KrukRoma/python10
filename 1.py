#1
file1_path = "file1.txt"
file2_path = "file2.txt"

with open(file1_path, "w") as file1, open(file2_path, "w") as file2:
    content1 = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet quis consectetur dignissimos aut iste commodi, sint consequatur animi harum modi eaque obcaecati sapiente error corrupti voluptates, eius alias. Exercitationem, in."
    content2 = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa fugit dolore quasi quis odio, eaque deleniti dicta cumque quisquam. Ipsum, eligendi! Nulla vero reprehenderit non consectetur excepturi at, dolore corrupti."
    file1.write(content1)
    file2.write(content2)

with open(file1_path, "r") as file1, open(file2_path, "r") as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

min_len = min(len(lines1), len(lines2))

for i in range(min_len):
    if lines1[i] != lines2[i]:
        print(i + 1)
        print(lines1[i].strip())
        print(lines2[i].strip())

if len(lines1) > min_len:
    for i in range(min_len, len(lines1)):
        print(i + 1)
        print(lines1[i].strip())

if len(lines2) > min_len:
    for i in range(min_len, len(lines2)):
        print(i + 1)
        print(lines2[i].strip())



