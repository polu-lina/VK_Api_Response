import requests, json


class VK():

    def __init__(self, guid):
        self.id = guid
        self.user_response = 'https://api.vk.com/method/users.get?owner_id='
        self.albums_response = 'https://api.vk.com/method/photos.getAlbums?user_id='
        self.api_version = '&v=5.52&'
        self.token = 'access_token=1ab2373b1ab2373b1ab2373b7e1ac05fed11ab21ab2373b446a9e8be4eb934b1f10d96f'


    def get_albums(self):
        response = requests.get(self.albums_response + self.id + self.api_version + self.token)
        albums = json.loads(response.content)
        try:
            count = albums["response"]["count"]
            if count == 0:
                print("У этого пользователя нет открытых альбомов")
            else:
                for album in albums["response"]["items"]:
                    print("Название альбома: " + album["title"] + "\tКол-во фото: " + str(album["size"]))
        except Exception:
            print('Что-то пошло не так, возможно, вы ввели неправильный id')


if __name__ == '__main__':
    guid = input('Введите id пользователя:\n')
    vk = VK(guid)
    vk.get_albums()