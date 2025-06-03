from pytube import YouTube
print("YouTube Video Downloader v?.? - Beta")
url = input("Enter Video URL: ").strip()
yt = get_video(url)
print(f"\nTitle: {yt.title}")
print(f"Author: {yt.author}")
streams = 
