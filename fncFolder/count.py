

line_number = 0
specific_line = 1
# count the lines of links in a txt files first
with open("redditFiles/link.txt", "r") as file:
    line_count = sum(1 for line in file)
    line_number=line_count



if line_number >0:
    with open("redditFiles/output/output.txt","w") as file:
        file.write(str(specific_line) + "\n") 
    while True:
        specific_line+=1
        # insert here to append the new files from comming lines
        with open("redditFiles/output/output.txt","a") as file:
             file.write(str(specific_line) + "\n") 
        if specific_line > line_number:
            print("sucessfully")
            break
else:
    print("link.txt is empty")