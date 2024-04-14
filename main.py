import youtube_dl
import os
# Example script for youtube_dl
os.system('cls')

# Create the video directory
folder_name = "Videos"
if not os.path.exists(folder_name):
    print("Creating video directory")
    os.makedirs(folder_name)   
    print("Created video directory")
else:
    print("Video directory already exists")

# Create a YoutubeDL instance
ydl = youtube_dl.YoutubeDL({'format': 'bestvideo[ext=mp4]+bestaudio/best', 'outtmpl': '%(id)s.%(ext)s'})

# Change the path to the video directory
current = os.getcwd()
new = os.path.join(current, 'Videos')
os.chdir(new)

# Download the video (can be a list of videos)
ydl.download(['https://www.youtube.com/watch?v=oHg5SJYRHA0'])