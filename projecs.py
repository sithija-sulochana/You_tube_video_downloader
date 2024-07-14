from pytube import YouTube
import tkinter as tk

def download_video(url, output_path='/Users/YourUsername/Desktop/'):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print(f'Downloading {yt.title}...')
        stream.download(output_path)
        print('Downloaded successfully')
    except Exception as e:
        print(f'Error: {e}')

inurl = input("Enter your URL: ")
download_video(inurl)

