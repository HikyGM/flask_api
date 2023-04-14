from flask import request, jsonify
from config import application
from static.database import db_session
import static.database.__all_models as model


@application.route('/users/<int:id_user>', methods=['GET'])
def get_one_user(id_user):
    db_sess = db_session.create_session()
    user = db_sess.query(model.User.User).get(id_user)
    if not user:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'user': user.to_dict(only=(
                'id_user', 'login_user', 'email_user', 'first_name_user', 'last_name_user',
                'day_of_birth', 'gender_user', 'path_im_user', 'phone_number', 'city_user',
                'type_user'))
        }
    )


@application.route('/users', methods=['GET'])
def get_users():
    db_sess = db_session.create_session()
    return jsonify(
        {
            'users':
                [item.to_dict(only=('id_user', 'login_user', 'email_user',
                                    'first_name_user', 'last_name_user'))
                 for item in db_sess.query(model.User.User).all()]
        }
    )


@application.route('/register', methods=['POST'])
def register_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['login_user', 'email_user', 'first_name_user', 'last_name_user',
                  'day_of_birth', 'gender_user', 'phone_number', 'city_user',
                  'password_user', 'repeat_password_user']):
        return jsonify({'error': 'Bad request'})

    no_value = {key: 'No value' for key, value in request.json.items() if not value}
    if no_value:
        return jsonify(no_value)
    db_sess = db_session.create_session()
    user = model.User.User
    check_login = db_sess.query(user).filter(user.login_user == request.json['login_user']).first()
    check_email = db_sess.query(user).filter(user.email_user == request.json['email_user']).first()
    errors = {}
    if check_login:
        errors['login'] = 'Login is used'
    if check_email:
        errors['email'] = 'Email is used'
    if request.json['password_user'] != request.json['repeat_password_user']:
        errors['password'] = "Passwords don't match"
    if errors:
        return jsonify(errors)
    add_user = user(
        login_user=request.json['login_user'],
        email_user=request.json['email_user'],
        first_name_user=request.json['first_name_user'],
        last_name_user=request.json['last_name_user'],
        day_of_birth=request.json['day_of_birth'],
        gender_user=request.json['gender_user'],
        phone_number=request.json['phone_number'],
        city_user=request.json['city_user'],
    )
    add_user.set_password(request.json['password_user'])
    if 'path_im_user' in request.json:
        add_user.path_im_user = request.json['path_im_user']
    db_sess.add(add_user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@application.route('/login', methods=['POST'])
def login_user():
    print(request.data)
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['login', 'password']):
        return jsonify({'error': 'Bad request'})
    no_value = {key: 'No value' for key, value in request.json.items() if not value}
    if no_value:
        return jsonify(no_value)
    db_sess = db_session.create_session()
    check_user = db_sess.query(model.User.User).filter(model.User.User.login_user == request.json['login']).first()
    if not check_user:
        return jsonify({'errors': 'The user does not exist'})
    if not check_user.check_password(request.json['password']):
        return jsonify({'errors': 'The user does not exist'})
    return jsonify(check_user.to_dict(only=(
        'id_user', 'login_user', 'email_user', 'first_name_user', 'last_name_user',
        'day_of_birth', 'gender_user', 'path_im_user', 'phone_number', 'city_user',
        'type_user')))
