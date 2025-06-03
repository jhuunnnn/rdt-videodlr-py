import asyncio
import yt_dlp


    #reddit_video_url = 'https://packaged-media.redd.it/lbuak5x33a1f1/pb/m2-res_854p.mp4?m=DASHPlaylist.mpd&v=1&e=1747548000&s=85801ae818bf3162abf366528973afe5e331129e'

# fnc to download reddit link
async def download_reddit_video(url):
    print("starting downlooading....")
    ydl_opts = {
        "format":'bv*+ba/b',
        'outtmpl': 'outputVideos/%(title)s.%(ext)s',  # Save file as video title
        'merge_output_format': 'mp4'     # Combine video and audio
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("finish downlooading....")

# fnc to check txt_files is empty or not   
def check_txtFiles(link):
    line_number = 0
    # count the lines of links in a txt files first
    with open(link, "r") as file:
        line_count = sum(1 for line in file)
        line_number=line_count
    if line_number >0:
        print(line_number)
        print("link.txt is not empty")
        
    else:
        print("link.txt is empty")
    
    return line_number

def compile_links(linkFile):
    arrayLinks=[]
    with open(linkFile,"r") as file:
        lines = file.readlines()
        arrayLinks = [line.strip() for line in lines]
   
    return arrayLinks

async def main():
    current_Loop = 0
    txtFiles_Link = "redditFiles/finalLink.txt"
    exit_Loop = check_txtFiles(txtFiles_Link)
    if exit_Loop >0:
        listOfLinks = compile_links(txtFiles_Link)
     
        while current_Loop < exit_Loop:
            await download_reddit_video(listOfLinks[current_Loop])
            print(listOfLinks[current_Loop])
            print("new")
            current_Loop +=1
    else:
        print("provide txt is empty")

asyncio.run(main())
