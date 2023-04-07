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
def get_one_type_user(type_id):
    db_sess = db_session.create_session()
    type_user = db_sess.query(model.Type_users.Type_users).get(type_id)
    if not type_user:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'type': type_user.to_dict(only=(
                'id_type', 'title_type'))
        }
    )


@application.route('/type-user', methods=['GET'])
def get_type_user():
    db_sess = db_session.create_session()
    return jsonify(
        {
            'types':
                [item.to_dict(only=('id_type', 'title_type'))
                 for item in db_sess.query(model.Type_users.Type_users).all()]
        }
    )


@application.route('/type-user', methods=['POST'])
def post_type_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in ['title']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    type_user = model.Type_users.Type_users()
    if not db_sess.query(model.Type_users.Type_users).filter(
            model.Type_users.Type_users.title_type == request.json['title']).first():
        type_user.title_type = request.json['title']
        db_sess.merge(type_user)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    else:
        return jsonify({'error': 'The entity already exists'})


@application.route('/type-user/<int:id_type>', methods=['PUT'])
def put_type_user(id_type):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in ['title']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    if not db_sess.query(model.Type_users.Type_users).filter(
            model.Type_users.Type_users.title_type == request.json['title']).first():
        type = db_sess.query(model.Type_users.Type_users).get(id_type)
        if type:
            type.title_type = request.json['title']
            db_sess.merge(type)
            db_sess.commit()
            return jsonify({'success': 'OK'})
        else:
            return jsonify({'error': 'Bad request'})
    else:
        return jsonify({'error': 'The entity already exists'})


@application.route('/type-user/<int:id_type>', methods=['DELETE'])
def delete_type_user(id_type):
    db_sess = db_session.create_session()
    query = db_sess.query(model.Type_users.Type_users).get(id_type)
    if query:
        db_sess.delete(query)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    else:
        return jsonify({'error': 'Not found'})


@application.route('/providers/<int:id_provider>', methods=['GET'])
def get_one_provider(id_provider):
    db_sess = db_session.create_session()
    provider = db_sess.query(model.Providers.Providers).get(id_provider)
    if not provider:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'provider': provider.to_dict(only=(
                'id_provider', 'first_name_provider', 'last_name_provider', 'day_of_birth', 'gender_provider',
                'path_im_provider', 'phone_number', 'city_provider'))

        }
    )


@application.route('/providers', methods=['GET'])
def get_providers():
    db_sess = db_session.create_session()
    return jsonify(
        {
            'providers':
                [item.to_dict(only=(
                    'id_provider', 'first_name_provider', 'last_name_provider'))
                    for item in db_sess.query(model.Providers.Providers).all()]
        }
    )


@application.route('/providers', methods=['POST'])
def post_provider():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['first_name_provider', 'last_name_provider', 'day_of_birth', 'gender_provider',
                  'path_im_provider', 'phone_number', 'city_provider']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
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
    return jsonify({'success': 'OK'})


@application.route('/providers/<int:id_provider>', methods=['PUT'])
def put_provider(id_provider):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['first_name_provider', 'last_name_provider', 'day_of_birth', 'gender_provider',
                  'path_im_provider', 'phone_number', 'city_provider']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    provider = db_sess.query(model.Providers.Providers).get(id_provider)
    if provider:
        provider.first_name_provider = request.json['first_name_provider']
        provider.last_name_provider = request.json['last_name_provider']
        provider.day_of_birth = request.json['day_of_birth']
        provider.gender_provider = request.json['gender_provider']
        provider.path_im_provider = request.json['path_im_provider']
        provider.phone_number = request.json['phone_number']
        provider.city_provider = request.json['city_provider']
        db_sess.merge(provider)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    else:
        return jsonify({'error': 'Not found'})


@application.route('/providers/<int:id_provider>', methods=['DELETE'])
def delete_provider(id_provider):
    db_sess = db_session.create_session()
    provider = db_sess.query(model.Providers.Providers).get(id_provider)
    if provider:
        db_sess.delete(provider)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    else:
        return jsonify({'error': 'Not found'})


@application.route('/posts/<int:id_post>', methods=['GET'])
def get_one_post(id_post):
    db_sess = db_session.create_session()
    post = db_sess.query(model.Blog.Blog).get(id_post)
    if not post:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'provider': post.to_dict(only=(
                'id_post', 'title_post', 'author_post', 'data_time_post', 'path_im_post'))
        }
    )


@application.route('/posts', methods=['GET'])
def get_posts():
    db_sess = db_session.create_session()
    return jsonify(
        {
            'posts':
                [item.to_dict(only=('id_post', 'title_post', 'author_post', 'data_time_post', 'text_post'))
                 for item in db_sess.query(model.Blog.Blog).all()]
        }
    )


@application.route('/posts', methods=['POST'])
def post_posts():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['title_post', 'author_post', 'data_time_post', 'path_im_post',
                  'text_post']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    post = model.Blog.Blog()
    post.title_post = request.json['title_post']
    post.author_post = request.json['author_post']
    post.data_time_post = request.json['data_time_post']
    post.path_im_post = request.json['path_im_post']
    post.text_post = request.json['text_post']
    db_sess.merge(post)
    db_sess.commit()
    return jsonify({'success': 'OK'})


def main():
    db_session.global_init()


if __name__ == "__main__":
    main()
    application.run(host='0.0.0.0', port=8080)
