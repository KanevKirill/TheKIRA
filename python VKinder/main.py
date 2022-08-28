from urllib import request

from vk_api.longpoll import VkEventType, VkLongPoll
from datetime import date

import database
import api

if __name__ == "__main__":

    def get_age(request_user_id, files, waiting_age):
        if 'Base' in files:
            age = date.today().year - int((files['Base']).split('.')[2])
        else:
            if database.select(request_user_id)[0]:
                age = database.select(request_user_id)[0]
            else:
                if waiting_age:
                    age = request
                    database.update_age(request_user_id, age)
                else:
                    api.write_msg(request_user_id, 'Введите свой возраст')
                    return None
            return age


    def get_sex(files, request_user_id, waiting_sex):
        if 'sex' in files:
            sex = api.get_files(request_user_id)['sex']
        else:
            if database.select(request_user_id)[1]:
                sex = database.select(request_user_id)[1]
            else:
                if waiting_sex:
                    sex = request
                    database.update_sex(request_user_id, sex)
                else:
                    api.write_msg(request_user_id, 'Введите свой пол')
                    return None
        return sex


    def get_city(files, request_user_id, waiting_city):
        if 'city' in files:
            city = files['city']['id']
        else:
            if database.select(request_user_id)[2]:
                city = database.select(request_user_id)[2]
            else:
                if waiting_city:
                    city = api.get_city(request)
                    database.update_city(request_user_id, city)
                else:
                    api.write_msg(request_user_id, 'Введите свой город:')
                    return None
        return city

longpoll = VkLongPoll(api.vk_group)

waiting_age = False
waiting_sex = False
waiting_city = False

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:

        request = event.text.lower()
        request_user_id = event.user_id

        fields = api.get_fields(request_user_id)

        try:
            database.insert_fields(request_user_id)
        except:
            pass

        if get_age():
            age = get_age()
        else:
            waiting_age = True

        if get_sex():
            sex = get_sex()
        else:
            waiting_sex = True

        if get_city():
            city = get_city()
        else:
            waiting_city = True

        try:
            matched_users = api.users_search(age, sex, city)
        except:
            pass
        else:
            api.write_msg(request_user_id, 'Подбираю тебе пару...')

            for matched_user in matched_users:
                if not matched_user['is_closed']:
                    screen_name = matched_user['screen_name']
                    user_id = matched_user['id']

                    try:
                        database.insert_users(request_user_id, user_id, screen_name)
                    except:
                        pass
                    else:
                        link_user = 'https://vk.com/' + screen_name
                        sorted_tuples = api.get_photos(user_id)

                        try:
                            attachment = f'photo{user_id}_{sorted_tuples[-1][0]},photo{user_id}_{sorted_tuples[-2][0]},photo{user_id}_{sorted_tuples[-3][0]}'
                        except:
                            try:
                                attachment = f'photo{user_id}_{sorted_tuples[-1][0]},photo{user_id}_{sorted_tuples[-2][0]}'
                            except:
                                try:
                                    attachment = f'photo{user_id}_{sorted_tuples[-1][0]}'
                                except:
                                    pass

                        api.write_msg(request_user_id, link_user)
                        break
