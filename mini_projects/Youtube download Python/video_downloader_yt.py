
#importing the module youtube to download the videos
from pytube import YouTube

#saving path
Save_path='C:/'

#open file to write all the relaevant info about the video
f = open("demofile2.txt", "a")

#link of the youtube video
link=input("Enter the link of the youtube video")

try:
    #object creation using youtube class
    yt=YouTube(link)

#to handle exeption
except:
    print("Connection Error")

"""Get all the relevant video data needed for the video"""

#get the video author
author = yt.author

#get the lenght of the video
length = yt.length

#get the date of publishing
date = yt.publish_date

#get the number o views
views = yt.views

#check if you only want the audio
a = input("you want only audio?")

#if only want audio
if (a):
    final = yt.streams.get_audio_only()
else:
    final = yt.streams.get_highest_resolution()

#Download the required file
final.download()

#print the details of video into the file

f.write("Author : "  + author + "\n")
f.write("Length :"  + str(length) + "\n")
f.write("Date of Publishing : "  + str(date) + "\n")
f.write("Views :"  + str(views) + "\n")
f.close()
#f.writelines(text_list)
print("Task Complete")        