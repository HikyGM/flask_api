from flask import request, jsonify
from config import application
from static.database import db_session
import static.database.__all_models as model


@application.route('/manufacturer-product/<int:id_manufacturer>', methods=['GET'])
def get_one_manufacturer_product(id_manufacturer):
    db_sess = db_session.create_session()
    manufacturer = db_sess.query(model.Manufacturer_product.Manufacturer_product).get(id_manufacturer)
    if not manufacturer:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'manufacturer': manufacturer.to_dict(only=('id_manufacturer', 'title_manufacturer',
                                                       'INN', 'phone_number', 'address'))
        }
    )


@application.route('/manufacturer-product', methods=['GET'])
def get_manufacturer_product():
    db_sess = db_session.create_session()
    return jsonify(
        {
            'manufacturer':
                [item.to_dict(only=('id_manufacturer', 'title_manufacturer'))
                 for item in db_sess.query(model.Manufacturer_product.Manufacturer_product).all()]
        }
    )


@application.route('/manufacturer-product', methods=['POST'])
def post_manufacturer_product():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['title', 'INN', 'address', 'phone']):
        return jsonify({'error': 'Bad request'})
    no_value = {key: 'No value' for key, value in request.json.items() if not value}
    if no_value:
        return jsonify(no_value)
    db_sess = db_session.create_session()
    manufacturer = model.Manufacturer_product.Manufacturer_product
    check_title = db_sess.query(manufacturer).filter(manufacturer.title_manufacturer == request.json['title']).first()
    check_INN = db_sess.query(manufacturer).filter(manufacturer.INN == request.json['INN']).first()
    errors = {}
    if check_title:
        errors['title'] = 'Title is used'
    if check_INN:
        errors['INN'] = 'INN is used'
    if errors:
        return jsonify(errors)
    add_manufacturer = manufacturer(
        title_manufacturer=request.json['title'],
        INN=request.json['INN'],
        address=request.json['address'],
        phone_number=request.json['phone']
    )
    db_sess.add(add_manufacturer)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@application.route('/manufacturer-product/<int:id_manufacturer>', methods=['PUT'])
def put_manufacturer_product(id_category):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in ['title']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    category = db_sess.query(model.Category_product.Category_product).get(id_category)
    if category:
        category.title_category = request.json['title']
        db_sess.merge(category)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    else:
        return jsonify({'error': 'Not found'})


@application.route('/manufacturer-product/<int:id_manufacturer>', methods=['DELETE'])
def delete_manufacturer_product(id_category):
    db_sess = db_session.create_session()
    category = db_sess.query(model.Category_product.Category_product).get(id_category)
    if category:
        db_sess.delete(category)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    else:
        return jsonify({'error': 'Not found'})
