
from pytube import YouTube

youtube = YouTube('https://www.youtube.com/watch?v=KUu6aZhkry4')

youtube.streams.get_highest_resolution().download()
