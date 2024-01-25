file5_path = "file5.txt"
file6_path = "file6.txt"
with open(file5_path, "w") as file5, open(file6_path, "w") as file6:
    content1 ="""Lorem ipsum dolor sit amet consectetur adipisicing elit. 
Eveniet quis consectetur dignissimos aut iste commodi, 
sint consequatur animi harum modi eaque obcaecati sapiente error corrupti voluptates, eius alias.
Exercitationem, in."""
    content2 = file6_path
    file5.write(content1)
    file6.write(content2)

with open(file5_path, "r") as file5:
    lines = file5.readlines()

if lines:
    lines.pop()

with open(file6_path, "w") as file6:
    file6.writelines(lines)

pop_count = content1.split()
