from flask import request, jsonify
from config import application
from static.database import db_session
import static.database.__all_models as model


@application.route('/category-product/<int:id_category>', methods=['GET'])
def get_one_category_product(id_category):
    db_sess = db_session.create_session()
    category = db_sess.query(model.Category_product.Category_product).get(id_category)
    if not category:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'category': category.to_dict(only=('id_category', 'title_category'))
        }
    )


@application.route('/category-product', methods=['GET'])
def get_category_product():
    db_sess = db_session.create_session()
    return jsonify(
        {
            'category':
                [item.to_dict(only=('id_category', 'title_category'))
                 for item in db_sess.query(model.Category_product.Category_product).all()]
        }
    )


@application.route('/category-product', methods=['POST'])
def post_category_product():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in ['title']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    if not db_sess.query(model.Category_product.Category_product).filter(
            model.Category_product.Category_product.title_category == request.json['title']).first():
        category = model.Category_product.Category_product(
            title_category=request.json['title']
        )
        db_sess.add(category)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    else:
        return jsonify({'error': 'The entity already exists'})


@application.route('/category-product/<int:id_category>', methods=['PUT'])
def put_category_product(id_category):
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


@application.route('/category-product/<int:id_category>', methods=['DELETE'])
def delete_category_product(id_category):
    db_sess = db_session.create_session()
    category = db_sess.query(model.Category_product.Category_product).get(id_category)
    if category:
        db_sess.delete(category)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    else:
        return jsonify({'error': 'Not found'})
