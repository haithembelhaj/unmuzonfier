# Unmuzonfy

If you ever searched for some mp3 online, you propably stumbled upon muzon.ws or zippyshare. While I don't support that kind of websites and I think that everyone should buy something if he really likes it, sometimes it could be handy to try and listen to some music before puchasing it. The problem with muzon or zippy is the silly filenames.

Unmuzonfy changes this `Muzon.ws_Artist-Songtitle(muzon.ws)` or this `Artist-Songtitle(www.someCrappyWebsite.com)` into this `Artist-Songtitle`.

And if you pass it the `-id3` argument the it will adjust the ID3 of the file if some ID3 information is missing.

Awesome right :)

# Let's start unmuzonfying

It's a Python script so just install python and launch

    python unmuzonfy.py /path/to/your/music

and all the files in that directory will be renamed. Don't be afraid it will only detect websites strings in the filename so don't worry about your music files.

It handles files too

    python unmuzonfy.py /path/to/your/music/file.mp3

For the ID3 part I used a Module called [Mutagen](http://code.google.com/p/mutagen/) so intall it with [pip](http://pypi.python.org/pypi/pip) or whatever you like and type

    python unmuzonfy.py -id3 /path/to/your/music

to have the id3 also parsed.

> Enjoy your unmuzonfications :p