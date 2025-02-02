from pydub import AudioSegment
from pydub.playback import play
import simpleaudio as sa
import scanner
import time
import threading


def playSong(songPath):
    song = AudioSegment.from_file(songPath, format="mp3")

    rawData = song.raw_data
    sampleRate = song.frame_rate
    channels = song.channels
    sampleWidth = song.sample_width

    #play the audio
    waveObj = sa.WaveObject(rawData, num_channels=channels, bytes_per_sample=sampleWidth, sample_rate=sampleRate)

    return waveObj.play()

#recieves songname and filepath to play the music
def recieveMusicFiles(songName, songPath, songQueue):
    print("NOW PLAYING: " + songName + "\n")

    playObj = playSong(songPath)

    while playObj.is_playing():
        trackControl = input("Press 's' to skip or 'q' to quit: ").strip().lower()

        if trackControl == "s":
            playObj.stop()
            print("Skipping song...\n")
            break

        elif trackControl == "q":
            playObj.stop()
            print("quitting.\n")
            return
        else:
            print("invalid input, try again\n")
    
    #Move to next song in the queue if possible
    if songQueue:
        nextSong = songQueue.pop(0)
        recieveMusicFiles(nextSong[0], nextSong[1], songQueue)
    return

#searches for song in list of tuple (songname, filepath)
def songLookUp(mp3Files): #Need to convert this to an ITEM lookup so it can work for both SONGS and ALBUMS
    songNameQuery = input("Enter the song name you would like to play: ")

    query = songNameQuery.lower()
    results = []
    for song, path in mp3Files:
        songNameLower = song.lower()
        if query in songNameLower:
            results.append((song, path))
    if results:
        songName, songPath = results[0]
        recieveMusicFiles(songName, songPath, [])
    else:
        print("No matching songs found.")

    return results, songName, songPath

#Similar to songLookUp recieves a tuple of albumNames (AlbumName, path) for lookup
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
        print("Which album are you interested in playing?")
        for albumName, albumPath in results:
            print(albumName)
        print("\n")
        albumQuery = input("")

    
    elif len(results) == 1:
        albumName, albumPath = results[0] 
        _, songsInAlbum = scanner.listFolderContents(albumPath)

        songOrQueue = input("Type 1 if you want to play the whole album, or 2 if you want to list the songs").strip().lower()

        #if user wants to play whole album
        if songOrQueue =="1":
            recieveMusicFiles(songsInAlbum[0][0], songsInAlbum[0][1], songsInAlbum[1:])

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