from flask import request, jsonify
from config import application
from static.database import db_session
import static.database.__all_models as model


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
