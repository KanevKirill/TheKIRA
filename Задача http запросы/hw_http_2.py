import requests

class YaUploader:
    host = 'https://cloud-api.yandex.net:443'

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = f'{self.host}/v1/disk/resources/upload/'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': file_path, 'overwrite': True}
        response = requests.get(url, params=params, headers=headers)
        href_json = response.json()
        href = href_json['href']
        upl_file = requests.put(href, data=open(path_to_file, 'rb'), headers=headers)
        upl_file.raise_for_status()
        if upl_file.status_code == 201:
            print(f"Файл {path_to_file} загружен. Success!")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'test.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)