# Reddit Video Downloader Using Links in txtFiles

## Introduction

#### What is this?

This repo is for my scripting for my yt channel in downloading reddit videos.

#### Why?

I noticed that when I am using a free reddit video downloader that I found on the internet. I have to enter the links one by one to download. It wastes a lot of time. So I thought of making a program / script that will read a text file full of links and automatically download the next video.

#### How?

Find videos in reddit and simply copy the link and paste in a text file within the folder of the repo. Change the variable `textFiles_Link` to your name of the file text. And run `py main.py` in the terminal and wait in the folder of `outputVideos` to show the downloaded videos.

## Documentaion

#### Why Python?

Python is designed for making a genral-purpose scripting language and it applicable to a lot of applications. It allows developers to write scritps that can automate tasks and others.
Plus, I most used Javascript in programming and I want to explore and test some language that why I used Python.

#### Steps and Problems Encounterd

1. Initialize python in vs code
2. Read a text file
3. Count how many lines in a text file
4. Execute a function every line
5. Make fnc to dl a video from Reddit
   - Output the video in specific path
   - Name the video through its content
6. Check first if the text file is not empty
7. Deploy fnc RedditVL to the while loop
   - loop the fnc depending how many the lines of a text file

##### Problems

    1. error encoutering in executing the reddit video downloader function `yt_dlp`
        - fixed by installing `ffmpeg` to the system and adding to the env variables
    2. what if the line in the text file is empty or invalid
        - fixed by catching error in fnc video downloader
        `'quiet':False,
        'ignoreerrors':True`
        - ignores the error and avoiding the loop to be break and continue the process to the next line

#### Future Ideas

1. filter the videos by their categories and download the video with a specfic folder for it
2. get the top videos in a subreddit and download it automatically
3. Make the program a application
