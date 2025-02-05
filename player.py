from pydub import AudioSegment
from pydub.playback import play
import simpleaudio as sa
import scanner
import time


def playSong(songPath, position=0):
    song = AudioSegment.from_file(songPath, format="mp3")
    songSegment = song[position:]

    rawData = songSegment.raw_data
    sampleRate = songSegment.frame_rate
    channels = songSegment.channels
    sampleWidth = songSegment.sample_width

    #play the audio
    waveObj = sa.WaveObject(rawData, num_channels=channels, bytes_per_sample=sampleWidth, sample_rate=sampleRate)

    return waveObj.play()

#recieves songname and filepath to play the music
def recieveMusicFiles(songName, songPath, songQueue):
    print("NOW PLAYING: " + songName + "\n")

    startTime = time.time()
    playObj = playSong(songPath)

    while playObj.is_playing():
        trackControl = input("Press 's' to skip or 'q' to quit: ").strip().lower()
        elapsedTime = (time.time() - startTime) * 1000
        position = int(elapsedTime)

        if trackControl == "s":
            playObj.stop()
            print("Skipping song...\n")
            break
        elif trackControl == "p":
            playObj.stop()
            print(f"pausing at {position / 1000:.2f} seconds. Press 'p' to resume.\n")
            
            while input().strip().lower() != "p":
                pass
            
            print(f"Resume from {position / 1000:.2f} seconds")
            playObj = playSong(songPath, position)
            startTime = time.time()

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
def itemLookUp(mp3Files, songORalbum): #Need to convert this to an ITEM lookup so it can work for both SONGS and ALBUMS
    if songORalbum:
        itemQuery = input("Enter the song name you would like to play: ")
    else:
        itemQuery = input("Enter the album name you would like to look at: ")

    query = itemQuery.lower()
    results = []
    for item, path in mp3Files:
        itemNameLower = item.lower()
        if query in itemNameLower:
            results.append((item, path))

    if songORalbum == False:
        albumHandler(results)
    else:
        if results:
            songName, songPath = results[0]
            recieveMusicFiles(songName, songPath, [])
        else:
            print("No matching songs found.")

        return results, songName, songPath

#Handles outputs of itemLookUp inputs as a tuple (AlbumName, path) for lookup
def albumHandler(albumNames):

    #change output depending on albums found
    if len(albumNames) > 1:
        print("Which album are you interested in playing?")
        for albumName, albumPath in albumNames:
            print(albumName)
        print("\n")
        albumQuery = input("")

    
    elif len(albumNames) == 1:
        albumName, albumPath = albumNames[0] 
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
            itemLookUp(songsInAlbum, songORalbum=True)

        else:
            print("please enter a valid input.")
            sys.exit()

    else:
        print("No albums found with that keyword.")
    return