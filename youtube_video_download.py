import pytube

link =input("Enter Youtube Video URL:")
yt = pytube.YouTube(link)
yt.streams.first().download()
print('Downloaded',link)