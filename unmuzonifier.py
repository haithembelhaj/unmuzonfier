import os
import sys
import re
from mutagen.easyid3 import EasyID3


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
    newName = file.replace('Muzon.ws', '').replace('(muzon.ws)', "").replace('_', ' ')
    newName = re.sub(r'\(?www\.\w+\.\w+\)?','',newName)
    newName = re.sub(r'^\s+','', newName)
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
    artist = re.sub(r'\s+$','', meta[0])
    title = re.sub(r'^\s+','', meta[1])
    title = re.sub(r'\.\w\w\w$','', title)
    title = re.sub(r'\s+$','', title)
    audio = EasyID3(file)
    if not artist in audio:
        print "Changing ID3"
        print "artist: "+artist
        print "title: "+title
        audio["title"] = title
        audio["artist"] = artist
        audio.save()


if __name__ == "__main__":
    if sys.argv[1] == "-id3":
        ID3 = True
        path = sys.argv[2]
    else:
        path = sys.argv[1]
    readPath(path)
