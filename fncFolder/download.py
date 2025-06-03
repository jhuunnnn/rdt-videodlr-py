import yt_dlp

def download_reddit_video(url):
    ydl_opts = {
        "format":'bv*+ba/b',
        'outtmpl': 'outputVideos/%(title)s.%(ext)s',  # Save file as video title
        'merge_output_format': 'mp4'     # Combine video and audio
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example Reddit post URL
reddit_video_url = 'https://www.reddit.com/r/funnyvideos/comments/1l1yxpz/im_in_when_we_going/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button'

 # replace with actual link
download_reddit_video(reddit_video_url)
