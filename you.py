import pytube

yt = pytube.YouTube('https://youtu.be/P1FEdfuI8CE')
stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
stream.download()