from pydub import AudioSegment
from pydub.playback import play
import simpleaudio as sa
import scanner
import sys


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


#recieves list of song tuples (songname, filepath)
def playQueue(SongQueue):
    for songName, songPath in SongQueue:
        recieveMusicFiles(songName, songPath)
    return

def albumLookUp(albumNames):
    albumNameQuery = input("Enter the album name you would like to look at: ")

    query = albumNameQuery.lower()
    results = []
    for album, path in albumNames:
        albumNameLower = album.lower()
        if query in albumNameLower:
            results.append((album, path))

    #change output depending on albums found
    if len(results) > 1:
        return
    
    elif len(results) == 1:
        albumName, albumPath = results[0] 
        _, songsInAlbum = scanner.listFolderContents(albumPath)

        songOrQueue = input("Type 1 if you want to play the whole album, or 2 if you want to list the songs").strip().lower()

        #if user wants to play whole album
        if songOrQueue =="1":
            playQueue(songsInAlbum)

        #play a specific song
        elif songOrQueue == "2":
            print("Songs found in " + albumName)
            for song, _ in songsInAlbum:
                print(song)
            #call songLookUp on this list of mp3 files
            songLookUp(songsInAlbum)

        else:
            print("please enter a valid input.")
            sys.exit()

    else:
        print("No albums found with that keyword.")
    return