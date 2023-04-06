
    {
                "id_provider": 2,
                "first_name_provider": "Семён",
                "last_name_provider": "Иванов",
                "day_of_birth": "07.12.1998",
                "gender_provider": "1",
                "path_im_provider": "",
                "phone_number": "88888888888",
                "city_provider": "Орск"
    }


API

/type-user

GET: Получение всех типов пользователя

    запрос:
            нет данных
    ответ:
            [
                {
                    "id": 3,
                    "title_type": "Admin"
                },
                {
                    "id": 9,
                    "title_type": "Admin1"
                }
            ]
POST: Добавление типа пользователя

    запрос:
            {
                "title": "Manager"
            }
    ответ:
            {
                "method": "POST",
                "response": "OK",
                "status": "успешно добавлен",
                "title_type": "Admin"
            }

DELETE: Удаление типа пользователя

    запрос:
            {
                "id": 10
            }
    ответ:
            {
                "method": "DELETE",
                "response": "OK",
                "status": "успешно удалён",
                "title_type": "Admi5n1"
            }

PUT: Изменение названия типа пользователя

    запрос:
            {
                "id": 12,
                "title": "Менеджер"
            }
    ответ:
            {
                "method": "PUT",
                "old_title_type": "Adsdvmi5n1",
                "response": "OK",
                "status": "успешно изменён",
                "title_type": "Менеджер"
            }

/providers

GET: Получение всех продавцов

    запрос:
            нет данных
    ответ:
            [
                {
                    "city_provider": "Орск",
                    "day_of_birth": "Mon, 07 Dec 1998 00:00:00 GMT",
                    "first_name_provider": "Алексей",
                    "gender_provider": "1",
                    "id_provider": 1,
                    "last_name_provider": "Горнеев",
                    "path_im_provider": "",
                    "phone_number": "89999999999"
                },
                {
                    "city_provider": "Орск",
                    "day_of_birth": "Mon, 07 Dec 1998 00:00:00 GMT",
                    "first_name_provider": "Семён",
                    "gender_provider": "1",
                    "id_provider": 2,
                    "last_name_provider": "Иванов",
                    "path_im_provider": "",
                    "phone_number": "88888888888"
                }
            ]

POST: Добавление продавца

    запрос:
            {
                "first_name_provider": "Семён",
                "last_name_provider": "Иванов",
                "day_of_birth": "07.12.1998",
                "gender_provider": "1",
                "path_im_provider": "",
                "phone_number": "88888888888",
                "city_provider": "Орск"
            }
    ответ:
            {
                "method": "POST",
                "response": "OK",
                "status": "200"
            }