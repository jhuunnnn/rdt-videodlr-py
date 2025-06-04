
#write and read files
with open("testFolder/first_text.txt","w") as file:
    file.write("first text to write in a text")


#count the lines of a txt files
with open("my_file.txt", "r") as file:
    line_count = sum(1 for line in file)
    print("Number of lines:", line_count)


#choose a specifc line in a txt files
line_number = 11
with open("redditFiles/testline.txt", "r") as file:
    lines = file.readlines()
    if line_number <= len(lines):
        print(f"Line {line_number}:", lines[line_number - 1].strip())
    else:
        print("That line doesn't exist.")