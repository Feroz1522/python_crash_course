def make_album(title,album,track=''):                
    music_album = {
        'album':title,
        'artist':album,
        }
    
    if track:
        music_album['track']=track

     
    return music_album

album = make_album('avatar','james cameron')
print(album)
album = make_album('ponninyin selavan','kalki',track='ponni nadhi pakanumey')
print(album)
album = make_album('pathuthala','simbu','nee singam dhan')
print(album)
