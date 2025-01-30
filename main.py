import sys
import player, scanner

musicDirectory = "C:/Users/mattb/Documents/Soulseek Downloads/complete"

def programStart():
    print("Scanning selected filepath...")
    albumNames, mp3Files = scanner.listFolderContents(musicDirectory)
    print("Scan complete.\n")

    songOrAlbumInput = input("Select 1 to search for an Album and 2 to Search for a song directly\n")
    if songOrAlbumInput == "1":
        songName = player.albumLookUp(albumNames)
    elif songOrAlbumInput == "2":
        _, songName, songPath = player.songLookUp(mp3Files)
        player.recieveMusicFiles(songName, songPath)
    else: 
        print("Please enter a valid input\nExiting...")
        sys.exit()
    
    return

if __name__ == "__main__":
    programStart()