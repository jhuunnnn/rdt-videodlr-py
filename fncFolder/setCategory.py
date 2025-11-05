import os

# Open and read the file
with open("hello.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

for i in lines:
    if i[0] != "h":
        folder_path = i
        os.makedirs(i,exist_ok=True)
    else:
        file_name = i +".txt"
        file_path = os.path.join(folder_path,file_name)
        with open(file_path,"w") as f:
            f.write(i)
        print(i)


print(lines[0]) 

exampleString = "String"
print(exampleString[0])