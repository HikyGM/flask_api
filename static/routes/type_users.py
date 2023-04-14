from flask import request, jsonify
from config import application
from static.database import db_session
import static.database.__all_models as model


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
    print(request.json)
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
        _type = db_sess.query(model.Type_users.Type_users).get(id_type)
        if _type:
            _type.title_type = request.json['title']
            db_sess.merge(_type)
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
