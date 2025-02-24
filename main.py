import sys
import player
import scanner

musicDirectory = "C:/Users/mattb/Documents/Soulseek Downloads/complete"

def programStart():
    print("Scanning selected filepath...")
    albumNames, mp3Files = scanner.listFolderContents(musicDirectory)
    print("Scan complete.\n")

    while True:  # Input 
        songOrAlbumInput = input("Select 1 to search for an Album, 2 to search for a song, or 'q' to exit: ").strip().lower()
        
        if songOrAlbumInput == "1":
            player.itemLookUp(albumNames, songORalbum=False)
        elif songOrAlbumInput == "2":
            _, songName, songPath = player.itemLookUp(mp3Files, songORalbum=True)
            player.recieveMusicFiles(songName, songPath, [])
        elif songOrAlbumInput == "q":
            print("Exiting program.")
            break  # Exit the loop
        else: 
            print("Please enter a valid input.")

if __name__ == "__main__":
    programStart()