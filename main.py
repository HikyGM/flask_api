from config import application
from static.database import db_session
import static.routes

'''
        Для создания комита изменения базы
        alembic revision --autogenerate -m "добавили признак публикации"
        
        Обновить базу
        alembic upgrade head
        
        Откатиться к предыдушей версии
        alembic downgrade head
        
        head означает, что мы хотим применить все миграции 
        друг за другом для приведения базы в самое актуальное 
        состояние. Вместо head можно указать номер ревизии
        или написать, например, +2, 
        чтобы обновиться только на 2 следующие версии.
'''


@application.route('/')
@application.route('/index')
def index():
    return '123445'


def main():
    db_session.global_init()


if __name__ == "__main__":
    main()
    application.run(host='0.0.0.0', port=8080)
