import yt_dlp

def download_reddit_video(url):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  # Save file as video title
        'merge_output_format': 'mp4'     # Combine video and audio
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example Reddit post URL
reddit_video_url = 'https://packaged-media.redd.it/lbuak5x33a1f1/pb/m2-res_854p.mp4?m=DASHPlaylist.mpd&v=1&e=1747548000&s=85801ae818bf3162abf366528973afe5e331129e'

 # replace with actual link
download_reddit_video(reddit_video_url)
