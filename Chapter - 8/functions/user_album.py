def make_album(title,album,track=''):                
    music_album = {
        'album':title.lower(),
        'artist':album.lower(),
        }
    
    if track:
        music_album['track']=track.lower()

     
    return music_album

while True:
    #getting the info
    print("\n enter the title ")
    title = input(">> ")
    print("\n enter the album name")
    album = input(">> ")
    print("\n enter the name of the track")
    track = input(">> ")
    
    #storing it in dictionary1
    value = make_album(title,album,track)
    print(value)
    
    #option for quiting
    print('\n do you need to continue this recoding press y/n ')
    quit = input(">> ")
    if quit == 'n':
        break

print("\tThanking for responding")
