from flask import Flask, request, jsonify
from flask_login import LoginManager
import static.database.__all_models as model

from static.database import db_session

application = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(application)
application.config['SECRET_KEY'] = 'bfy45ue7iuyilutgbkwycu4b7e46ytwu4etriuw34yiuitwyeiut54'


@application.route('/')
@application.route('/index')
def index():
    return '123445'


@application.route('/type-user/<int:type_id>', methods=['GET'])
def one_type_user(type_id):
    db_sess = db_session.create_session()
    type = db_sess.query(model.Type_users.Type_users).get(type_id)
    return jsonify([{"id": type.id_type, "title_type": type.title_type}])


@application.route('/type-user', methods=['GET', 'POST', 'DELETE', 'PUT'])
def type_user():
    db_sess = db_session.create_session()
    if request.method == 'GET':
        return jsonify([{"id": value.id_type, "title_type": value.title_type} for value in
                        db_sess.query(model.Type_users.Type_users).all()])

    elif request.method == 'POST':
        if not request.json['title']:
            return jsonify('Bed request')
        title = request.json['title']
        type = model.Type_users.Type_users()
        type.title_type = title
        db_sess.merge(type)
        db_sess.commit()
        return jsonify({'response': 'OK', 'method': request.method, 'title_type': title, 'status': 'успешно добавлен'})

    elif request.method == 'DELETE':
        id = request.json['id']
        if not id:
            return jsonify('Bed request')
        query = db_sess.query(model.Type_users.Type_users).get(id)
        db_sess.delete(query)
        db_sess.commit()
        return jsonify(
            {'response': 'OK', 'method': request.method, 'title_type': query.title_type, 'status': 'успешно удалён'})

    elif request.method == 'PUT':
        id = request.json['id']
        new_title = request.json['title']
        if not id:
            return jsonify('Bed request')
        type = db_sess.query(model.Type_users.Type_users).get(id)
        old_title = type.title_type
        type.title_type = new_title
        db_sess.merge(type)
        db_sess.commit()
        return jsonify(
            {'response': 'OK', 'method': request.method, 'title_type': type.title_type, "old_title_type": old_title,
             'status': 'успешно изменён'})


@application.route('/providers', methods=['GET', 'POST', 'DELETE', 'PUT'])
def providers():
    db_sess = db_session.create_session()
    if request.method == 'GET':
        res = []
        for value in db_sess.query(model.Providers.Providers).all():
            res.append({
                "id_provider": value.id_provider,
                "first_name_provider": value.first_name_provider,
                "last_name_provider": value.last_name_provider,
                "day_of_birth": value.day_of_birth,
                "gender_provider": value.gender_provider,
                "path_im_provider": value.path_im_provider,
                "phone_number": value.phone_number,
                "city_provider": value.city_provider
            })
        return jsonify(res)

    elif request.method == 'POST':
        if not request.json:
            return jsonify('Bed request')
        provider = model.Providers.Providers()
        provider.first_name_provider = request.json['first_name_provider']
        provider.last_name_provider = request.json['last_name_provider']
        provider.day_of_birth = request.json['day_of_birth']
        provider.gender_provider = request.json['gender_provider']
        provider.path_im_provider = request.json['path_im_provider']
        provider.phone_number = request.json['phone_number']
        provider.city_provider = request.json['city_provider']
        db_sess.merge(provider)
        db_sess.commit()
        return jsonify({'response': 'OK', 'method': request.method, 'status': '200'})

    elif request.method == 'PUT':
        if not request.json:
            return jsonify('Bed request')
        provider = db_sess.query(model.Providers.Providers).get(request.json['id_provider'])
        provider.first_name_provider = request.json['first_name_provider']
        provider.last_name_provider = request.json['last_name_provider']
        provider.day_of_birth = request.json['day_of_birth']
        provider.gender_provider = request.json['gender_provider']
        provider.path_im_provider = request.json['path_im_provider']
        provider.phone_number = request.json['phone_number']
        provider.city_provider = request.json['city_provider']
        db_sess.merge(provider)
        db_sess.commit()
        return jsonify({'response': 'OK', 'method': request.method, 'status': '200'})


def main():
    db_session.global_init()


if __name__ == "__main__":
    main()
    application.run(host='0.0.0.0', port=8080)
