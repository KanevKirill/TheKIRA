from random import randrange
import vk as vk
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

token = input('Token: ')

vk_group = vk_api.VkApi(token="39eb96a8dbb0bf1cc8d3eb751aff7b7a0a3c43dde8d8693ebb411be12331bc9bd10e1a8547f54aa1127c4")
vk_user = vk_api.VkApi(token='')
longpoll = VkLongPoll(vk, "213825019")


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7), })


# сбор информации со страницы
def get_fields(user_id):
    fields = vk_user.method('users.get', {'user_ids': user_id, 'fields': 'bdate, sex, city, relation'})[0]
    return fields


# поиск людей по параметрам
def users_search(age, sex, city):
    age_from = age - 5
    age_to = age + 5
    if sex == 1:
        required_sex = 2
    elif sex == 2:
        required_sex = 1
    else:
        required_sex = 0
    matched_users = vk_user.method('users.search',
                                   {'age_from': age_from, 'age_to': age_to, 'sex': required_sex, 'city': city,
                                    'status': 6, 'fields': 'screen_name'})['items']  # список из словарей
    return matched_users


# фотографии пользователя
def get_photos(user_id):
    photos = vk_user.method('photos.getAll', {'owner_id': user_id, 'extended': 1})
    photos_dict = {}
    for photo in photos['items']:
        comments_count = get_comments(user_id, photo.get('id'))
        photos_dict[photo.get('id')] = (photo.get('likes').get('count') + comments_count)
    sorted_tuples = sorted(photos_dict.items(), key=lambda item: item[1])
    return sorted_tuples


# комментарии к каждой фотографии
def get_comments(user_id, photo_id):
    try:
        comments = vk_user.method('photos.getComments', {'owner_id': user_id, 'photo_id': photo_id})
        return comments['count']
    except:
        comments = 0
        return comments


# гоод пользователя
def get_city(city_from_msg):
    cities = vk_user.method('database.getCities', {'country_id': 1, 'q': city_from_msg})
    try:
        city = cities['items'][0]['id']
    except:
        city = 1
    return city


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text

            if request == "привет":
                write_msg(event.user_id, f"Хай, {event.user_id}")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")