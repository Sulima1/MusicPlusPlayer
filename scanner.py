import os

musicDirectory = "C:/Users/mattb/Documents/Soulseek Downloads/complete"


def listFolderContents(musicDirectory):

    mp3Files = []
    albumNames = [] 
    for root, dirs, files in os.walk(musicDirectory):
        
        #list containing album names and paths
        albumNames.append((os.path.basename(root), os.path.join(root)))

        #mp3 files list containing tuple of filename and file path
        for name in files:
            mp3Files.append((os.path.basename(name), os.path.join(root + "/" + name)))
    
    return albumNames, mp3Files
    

albumNames, mp3Files = listFolderContents(musicDirectory)


