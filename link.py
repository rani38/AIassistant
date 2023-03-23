# import os
# import pytube
# from playsound import playsound
# l = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# def play_song(l):
    
# # Download the audio file from the YouTube link
#     yt = pytube.YouTube(l)
#     audio = yt.streams.filter(only_audio=True).first()
#     audio.download(output_path='./', filename='song.mp3')
    
#     # Play the downloaded audio file
#     playsound('song.mp3')
#     # Remove the downloaded audio file

#     os.remove('song.mp3')

# print(play_song(l))
