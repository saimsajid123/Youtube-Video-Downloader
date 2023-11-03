from pytube import YouTube


link = "https://www.youtube.com/watch?v=ZFvuBQ-e7uA"

videodown = YouTube(link)

video=videodown.streams.all()
vid=list(enumerate(video))

for i in vid:
    print(i,"\n")

enter=int(input("Enter The Number You Want To Download"))

video[enter].download()
print("Video Downloaded Sucessfully")





