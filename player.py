from pydub import AudioSegment
from pydub.playback import play
import simpleaudio as sa


def recieveMusicFiles(songName, songPath):
    print("NOW PLAYING: " + songName)
    mp3File = AudioSegment.from_file(file=songPath, format="mp3") 
    play(mp3File)
    return

def songLookUp(mp3Files):
    songNameQuery = input("Enter the song name you would like to play: ")

    query = songNameQuery.lower()
    results = []
    for song, path in mp3Files:
        songNameLower = song.lower()
        if query in songNameLower:
            results.append((song, path))
    if results:
        songName, songPath = results[0]
        recieveMusicFiles(songName, songPath)
    else:
        print("No matching songs found.")

    return results, songName, songPath

def albumLookUp(albumNames):
    albumNameQuery = input("Enter the album name you would like to look at: ")

    query = albumNameQuery.lower()
    results = []
    for album, path in albumNames:
        albumNameLower = album.lower()
        if query in albumNameLower:
            results.append((album, path))
    if results:
        albumName, albumPath = results[0]
    else:
        print("No matching songs found.")
    return