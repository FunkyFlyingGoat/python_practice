#编写一个city_country的函数
def city_country(name,country):
    message = f"{name.title()},{country.title()}"
    return message
print (city_country('santiago','chile'))

#编写一个专辑的函数,它创建一个表述专辑的字典
def make_album(singer_name,album_name,):
    album = {
    'singer_name':singer_name,
    'album_name':album_name,
    }
    return album
yangyang_album = make_album('yangyang','beautiful world')
print (yangyang_album)

#编写一个默认值为空的函数
def make_album(singer_name,album_name,album_number=""):
    album = {
    'singer_name':singer_name,
    'album_name':album_name,
    }
    if album_number:
        album['album_numbers']=album_number
    return album
yangyang_album = make_album('yangyang','beautiful world',7)
print (yangyang_album)