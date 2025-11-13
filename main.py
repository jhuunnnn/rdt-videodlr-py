import asyncio
import yt_dlp
import os
# fnc to download reddit link
async def download_reddit_video(url,surePath):

    try:
        print("starting downlooading....")
        ydl_opts = {
            "format":'bv*+ba/b',
            'outtmpl': f'outputVideos/{surePath}/%(title)s.%(ext)s',  # Save file as video title #outputvideos/"folderName"
            'merge_output_format': 'mp4',     # Combine video and audio
            'quiet':False,
            'ignoreerrors':False #set True if not using try and except statement
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("finish downlooading....")
    except Exception as e:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",e)

# fnc to check txt_files is empty or not   
def check_txtFiles(link):
    line_number = 0 
    # count the lines of links in a txt files first
    with open(link, "r") as file:
        line_count = sum(1 for line in file)
        line_number=line_count
    if line_number >0:
        print(line_number)
        print("provided link txt is  not empty")
        
    else:
        print("provided link txt is empty")
    
    return line_number

# compile all links into a array 
def compile_links(linkFile):
    arrayLinks=[]
    with open(linkFile,"r") as file:
        lines = file.readlines()
        arrayLinks = [line.strip() for line in lines]
   
    return arrayLinks


async def main():
    current_Loop = 0
    txtFiles_Link = "fncFolder/testFile.txt"
    exit_Loop = check_txtFiles(txtFiles_Link)
    if exit_Loop >0:
        listOfLinks = compile_links(txtFiles_Link)
        
        #perform the fnc download within the loop range of the list of links     
        path_folder = ""
        while current_Loop < exit_Loop:
            print(f'Current index {current_Loop} ')
            if "reddit.com" in listOfLinks[current_Loop]:
                await download_reddit_video(listOfLinks[current_Loop],path_folder)
                print(f'Done index,{current_Loop} ')
            else:
                path_folder = listOfLinks[current_Loop]
                print(f'Done index,{current_Loop} ')
            current_Loop +=1
    else:
        print("exiting scripts")

    print("Scripts completed")

asyncio.run(main())
