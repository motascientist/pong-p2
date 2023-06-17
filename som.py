from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = "https://www.youtube.com/watch?v=qtZ0hl-unM4"
Download(link)

# Importar moviepy
from moviepy.editor import *

# Carregar o arquivo de vídeo
video = VideoFileClip("Pac-Man Theme (Remix).mp4")

# Extrair o áudio
audio = video.audio

# Salvar o áudio em formato mp3
audio.write_audiofile("audio.mp3")
