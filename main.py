from config import application
from static.database import db_session
import static.routes


@application.route('/')
@application.route('/index')
def index():
    return '123445'


def main():
    db_session.global_init()


if __name__ == "__main__":
    main()
    application.run(host='0.0.0.0', port=8080)
