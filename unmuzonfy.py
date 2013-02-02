import os
import sys
import re
from mutagen.easyid3 import EasyID3
from mutagen import id3


ID3 = False


def readPath(path):
    for dirname, subdirs, files in os.walk(path):
        for subdir in subdirs:
            readPath(os.path.join(dirname, subdir))
        for file in files:
            if os.path.splitext(file)[1] == ".mp3":
                rename(dirname, file)

# rename the file
def rename(dirname, file):
    print "Renaming "+file
    newName = file.replace('Muzon.ws', '').replace('(muzon.ws)', "").replace('_', ' ') # muzon.ws
    newName = re.sub(r'(\(|\[)?(w{3}\.)?(\w|-)+(\.\w{2,3})+(\)|\])?\s*.mp3$','.mp3',newName) # [(www.somebullshit.com)]
    newName = re.sub(r'^\s+','', newName) # whitespaces
    newName = re.sub(r'\s+$','', newName) # whitespaces
    inPath = os.path.join(dirname, file)
    outPath = os.path.join(dirname, newName)
    os.rename(inPath, outPath)
    print "Renamed To "+newName
    if ID3:
        metadata(outPath, newName)
    print ""


# ID3
def metadata(file, name):
    meta = name.split('-')
    if len(meta) > 2:
        artist = re.sub(r'\s+$','', meta[0])
        title = re.sub(r'^\s+','', meta[1])
        title = re.sub(r'\.\w{3}$','', title)
        title = re.sub(r'\s+$','', title)
        try:
            audio = EasyID3(file)
            if not artist in audio:
                print "Changing ID3"
                print "artist: "+artist
                print "title: "+title
                audio["title"] = title
                audio["artist"] = artist
                audio.save()
        except id3.ID3NoHeaderError:
            print "ID3 changing failed"



if __name__ == "__main__":
    if sys.argv[1] == "-id3":
        ID3 = True
        path = sys.argv[2]
    else:
        path = sys.argv[1]
    readPath(path)
