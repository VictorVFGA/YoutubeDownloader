from pytube import YouTube

# URL del video de YouTube
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Creamos una instancia de la clase YouTube y filtramos las secuencias de solo audio
yt = YouTube(url)
audio_streams = yt.streams.filter(only_audio=True)

# Seleccionamos la primera secuencia de audio disponible y descargamos el archivo
audio = audio_streams.first()
audio.download()

# Renombramos el archivo descargado para que tenga la extensión mp3
import os
default_filename = audio.default_filename
os.rename(default_filename, default_filename[:-4] + ".mp3")