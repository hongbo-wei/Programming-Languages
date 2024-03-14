# 8-7

def make_album(artist, album, number_of_songs=None):
    """Make a dictionart storing info of album"""
    dic = {'artist': artist.title(),
           'album': album.title()
           }
    if number_of_songs:
        dic['number_of_songs'] = number_of_songs

    return dic


dic_1 = make_album('Lana Del Ray', 'young and beautiful')
print(dic_1)

dic_2 = make_album('Halsey', 'without me')
print(dic_2)

dic_3 = make_album('Eminem', 'the singles', 35)
print(dic_3)

while True:
    print('\nPlease enter information in below: ')
    print('Enter q for quit')
    artist = input('Artist: ')
    if artist == 'q':
        break
    album = input('Album: ')
    if album == 'q':
        break

    user_album = make_album(artist, album)
    print(user_album)

