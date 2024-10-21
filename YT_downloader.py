from pytube import YouTube
import os

url = 'https://youtu.be/zy4yzUjpnvA?si=aY9H-iGGkvrF7lpn'

video = YouTube(url)

print(f'Title: {video.title}')
print(f'Durata: {video.length} secunde')
print(f'Dimensiune video: {video.streams.get_highest_resolution().filesize / (1024 ** 2):.2f}MB')

dekstop_path = os.path.expanduser("C:\\Users\\Yerassyl\\Desktop")

video.streams.get_highest_resolution().download(output_path=dekstop_path)

print("saved")