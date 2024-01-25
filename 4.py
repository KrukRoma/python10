file7_path = "file7.txt"
file8_path = "file8.txt"
content = """Lorem ipsum dolor sit amet consectetur adipisicing elit. 
Eveniet quis consectetur dignissimos aut iste commodi, 
sint consequatur animi harum modi eaque obcaecati sapiente error corrupti voluptates, eius alias.
Exercitationem, in."""
with open(file7_path, "w") as file7:
    file7.write(content)
with open(file7_path, "r") as file7:
    lines = file7.readlines()

max_length = max(len(line) for line in lines)

longest_line = next((line for line in lines if len(line) == max_length), None)
with open("file8.txt", "w") as file8:
    file8.write(longest_line.strip())
